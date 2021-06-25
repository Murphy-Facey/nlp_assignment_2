import enchant
import json
import nltk
from nltk import word_tokenize, sent_tokenize
import spacy
import json
from nltk import sent_tokenize, word_tokenize
from collections import Counter


class Optimizer():
    def __init__(self):
        # self.text = text
        self.redundant_phrases = self.read_phrases_from_file()
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
        for paragraph in paragraphs:
            print("+++++---------------++++PARAGRAPH+++---------------")
            print(paragraph)
            sentences = self.sent_tokenizer(paragraph)
            for sentence in sentences:
                print("+++++---------------++++SENTENCE+++---------------+++++++++++++")
                print(sentence)
                # for j in range(len(sentences)):
                #     [unique_sents.append(x)
                #      for x in sentences if x not in unique_sents]

            unique_sents = str(paragraph)
            unique_sents = ' '.join(
                Removers().unique_list(unique_sents.split(".")))

            print(
                "+++++++++++++++++_________________without duplicates_____________+++++++++++++++")
            print(unique_sents)

    def sent_tokenizer(self, text):
        sentences = sent_tokenize(text)
        return sentences

    def word_tokenizer(self, text):
        words = word_tokenize(text)
        return words

    def unique_list(self, elemets):
        ulist = []
        [ulist.append(x) for x in elemets if x not in ulist]
        return ulist

# +*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+ word checker *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+


def englishChecker(token):
    d = enchant.Dict("en_US")
    res = d.check(token)
    if res == 1:
        print(d.suggest(token))
    elif res == 0:
        print("the word is okay")


# +*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+testing segment *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# Removers.testRemoval
# Removers.SpacySentencizer(text)
# Removers().wordRemover(rep)
# print(Removers().removeRedundantPhrasee(
#     "Will you cease and desist that infernal racket! We should plan ahead for Christmas."))
# Removers().sentenceRedundanceRemover1(text)
# Removers().paragrapher(text)
# Removers().repeatWordRemover(text)
# Removers().repeatSentRemover(text)
# Removers().duplicateSentRemover(text)
# englishChecker("bell")
