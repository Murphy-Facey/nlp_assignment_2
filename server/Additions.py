from textblob import TextBlob
import enchant
import json
import nltk
from nltk import word_tokenize, sent_tokenize
import spacy
import string
import re

nlp = spacy.load('en_core_web_sm')

text = """the housei is blak."""


class Removers:
    def __init__(self):
        self.abrs = {}
        self.emoji = {}

# +*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+does auto correction omiss spel items*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# identifies abbreviations

    def spellCheck(self, element):
        correction = TextBlob(element)
        correct = str(correction.correct())
        # print("corrected text: "+correct)
        return correct

    def normalize(self, element):
        return str(element).lower()

    def autoCorrect(self, text):
        list_words = word_tokenize(text)
        d = enchant.Dict("en_US")
        # print(list)

        # print(" Try out section ")
        for i in range(len(list_words)):
            # print(list[i])
            if list_words[i].lower() != "this":
                rec = self.spellCheck(list_words[i])
                if rec == list[i]:
                    # print("equals")
                    suggest = ""
                else:
                    # print("not equal")
                    list_words[i] = rec
                    suggest = d.suggest(list_words[i])
                # print(suggest)
        return list_words
# +*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+Identify Abreviationa*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# identifies abbreviations

    def readAbrev(self):
        file = open(  # this file location might need to change to accomodate the mache it is running on
            "abreviations.json", "r")  # added r to the brging of the string to fix a unicode error
        self.abrs = json.loads(file.read())
    
    def seperate_tokens(self, token):
        return re.findall(r"\w+|[^\w\s]", token)

    def identifyAbrev(self, sentence):
        self.readAbrev()
        # print(sentence)
        tokens = sentence.split()

        for key in self.abrs:
            for token in tokens:
                if key == token:
                    tokens[tokens.index(token)] = str(self.abrs[key])
                elif key == token.translate(str.maketrans('', '', string.punctuation)):
                    new_tokens = self.seperate_tokens(token)
                    new_tokens[new_tokens.index(key)] = str(self.abrs[key])
                    tokens[tokens.index(token)] = ''.join(new_tokens)
                    
        return ' '.join(tokens)

    # rule : we know have a paragraph when the text hits a next line sentences

# +*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+Emojis *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+


    def reademoji(self):
        file = open(  # this file location might need to change to accomodate the mache it is running on
            "emojis.json", "r")  # added r to the brging of the string to fix a unicode error
        self.emoji = json.loads(file.read())

    def identifyEmoji(self, sentence):
        self.reademoji()

        # print(sentence)
        for key in self.emoji:
            if key in sentence:
                sentence = sentence.replace(key, str(self.emoji[key]))
        return sentence


# print(Removers().autoCorrect(text))
# print(Removers().identifyAbrev("lol"))
# print(Removers().identifyEmoji("=-D"))
# print(Removers().seperate_tokens("ttyl."))