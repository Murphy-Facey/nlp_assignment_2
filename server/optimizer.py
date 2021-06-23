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
        end_punct = ['?','.',';',':',',',',','!']
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
                sentence = sentence.replace(key, str(self.redundant_phrases[key]))
        return sentence
    
    """ Removes duplicate sentences found within a given paragrapgh. """
    def remove_duplicate_sentences(self, sentences):
        uniq_sents = []
        counter = Counter(sentences)
        
        total = 0

        [total := total + counter[key] for key in counter]
        self.sent_counter = total
        
        [uniq_sents.append(sent) for sent in sentences if sent not in uniq_sents]
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
            sentences = self.sent_tokenize(paragraph)
            uniq_sents = self.remove_duplicate_sentences(sentences)
            for sentence in uniq_sents:
                sent_first_phase = self.remove_redundant_phrases(sentence)
                uniq_sents[uniq_sents.index(sentence)] = self.remove_repeat_words(sent_first_phase)
                # print(sentence)
            paragraphs[paragraphs.index(paragraph)] = ' '.join(uniq_sents)
        # print(paragraphs)
        return paragraphs
        
        
text = """ It's not only writers who can benefit from this free online tool. It's not only writers who can benefit from this free online tool. If you're a programmer who's working on a project where blocks of text are needed, this tool can be a great way to get that. It's a good way to test your programming and that the tool being created is working well.

Above are a few examples of how the random paragraph. I wish that I would plan ahead some times or even reverse back. The best way to see if this random paragraph picker will be useful for your intended purposes is to give it a try. Generate a number of paragraphs to see if they are beneficial to your current project."""


# opt = Optimizer()
# print(opt.optimize(text))
# print(opt.sent_counter)
# print(opt.word_counter)
# print(opt.phrase_counter)