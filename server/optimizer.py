import enchant
import json
import nltk
from nltk import word_tokenize, sent_tokenize
import spacy
import json
import re
import string
from nltk import sent_tokenize, word_tokenize
from collections import Counter

from Additions import Removers


class Optimizer():
    def __init__(self):
        # self.text = text
        self.redundant_phrases = self.read_phrases_from_file()
        self.synonyms = self.read_synonyms_from_file()
        self.removers = Removers()
        self.phrase_counter = 0
        self.word_counter = 0
        self.sent_counter = 0

    def paragrapher(self, text):
        paragraphs = [para for para in text.split('\n') if para != ""]
        return paragraphs

    """ Separate a paragrapgh into word tokens. """

    def sent_tokenize(self, paragraph):
        sentences = [sent.strip() for sent in sent_tokenize(paragraph)]
        return sentences

    """ Separate a sentence into word tokens. """

    def word_tokenizer(self, sentence):
        words = word_tokenize(sentence)
        return words

    """ Reconstructs a sentences from a list of stirngs. """

    def sentence_reconstruct(self, words):
        end_punct = ['?', '.', ';', ':', ',', ',', '!']
        new_sent = ""
        for word in words:
            if word in end_punct or words.index(word) == 0 or "'" in word:
                new_sent += word
            else:
                new_sent += f" {word}"
        return new_sent

    # +*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+ Sentence remover *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+

    """ Reads redundant phrases and simplified versions from a json file. """

    def read_phrases_from_file(self):
        file = open("redundant_phrases.json", "r")
        return json.loads(file.read())
    

    """ Remove the redundant phrases from sentence and replaces it with simplified version. """

    def remove_redundant_phrases(self, sentence):
        for key in self.redundant_phrases:
            if key in sentence:
                self.phrase_counter += 1
                sentence = sentence.replace(
                    key, str(self.redundant_phrases[key]))
        return sentence

    """ Reads synonyms and idoims from json file. """

    def read_synonyms_from_file(self):
        file = open("synonyms.json", "r")
        return json.loads(file.read())
    
    """ Replace synonyms and idoims from sentence. """
    
    def replace_synonyms_and_idioms(self, sentence):
        for key in self.synonyms:
            if " " in key:
                if key in sentence:
                    sentence = sentence.replace(key, str(self.synonyms[key]))
            else:  
                tokens = sentence.split()
                for token in tokens:
                    if key == token:
                        tokens[tokens.index(token)] = str(self.synonyms[key])
                        sentence = ' '.join(tokens)
                    elif key == token.translate(str.maketrans('', '', string.punctuation)):
                        new_tokens = re.findall(r"\w+|[^\w\s]", token)
                        new_tokens[new_tokens.index(key)] = str(self.synonyms[key])
                        tokens[tokens.index(token)] = ''.join(new_tokens)
                        sentence = ' '.join(tokens)
        
        return sentence
            # if key in sentence:
            #     sentence = sentence.replace(
            #         key, str(self.synonyms[key]))
        # return sentence

    """ Removes duplicate sentences found within a given paragrapgh. """

    def remove_duplicate_sentences(self, sentences):
        uniq_sents = []
        counter = Counter(sentences)

        total = 0

        [total := total + counter[key] for key in counter]
        self.sent_counter = total

        [uniq_sents.append(sent)
         for sent in sentences if sent not in uniq_sents]
        return uniq_sents

    """ Removes duplicate words found within a given sentence. """

    def remove_repeat_words(self, sentence):
        words = self.word_tokenizer(sentence)
        buffer = words

        seen_words = {}
        uniq_words = []

        for word in buffer:
            if word.lower() in seen_words:
                self.word_counter += 1
                continue
            else:
                seen_words[word.lower()] = word.lower()
                uniq_words.append(word)
        return self.sentence_reconstruct(uniq_words)

    def optimize(self, text):
        paragraphs = self.paragrapher(text)
        # print("---------------- REGULAR PARAGRAPHS ----------------\n")
        # print(paragraphs)
        # print('\n\n\n\n\n')
        for paragraph in paragraphs:
            sentences = self.sent_tokenize(paragraph)
            uniq_sents = self.remove_duplicate_sentences(sentences)
            for sentence in uniq_sents:
                sent_first_phase = self.remove_redundant_phrases(sentence)
                sent_second_phase = self.removers.identifyAbrev(sent_first_phase)
                sent_third_phase = self.removers.identifyEmoji(sent_second_phase)
                sent_fourth_phase = self.replace_synonyms_and_idioms(sent_third_phase)
                sent_fifth_phase = self.sentence_reconstruct(self.removers.autoCorrect(sent_fourth_phase))
                uniq_sents[uniq_sents.index(sentence)] = self.remove_repeat_words(sent_fifth_phase)

            paragraphs[paragraphs.index(paragraph)] = ' '.join(uniq_sents)
        # print("---------------- OPTIMISED PARAGRAPHS ----------------\n")
        # print(paragraphs)
        return paragraphs
        
# text = """This sentence is one that contains contains repeated words words words.
# This is a sentence that matches with another. This is a sentence that matches with another. However, we check to see if it is removed.
# I am :-o to know persons can feel :D while I (: at them. Anyways, I will brb or ttyl.
# thss sentnces has speling erors whire nothng seims to be rigt.
# The new feature of the Apple's new phone is good. It sometimes makes Andriod look like it is between a rock and hard place. But with large amount of effort in the next years, Android can be on the ball again."""

# opt = Optimizer()
# print(opt.optimize(text))