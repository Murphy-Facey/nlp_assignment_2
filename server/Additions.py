from textblob import TextBlob
import enchant
import json
import nltk
from nltk import word_tokenize, sent_tokenize
import spacy
nlp = spacy.load('en_core_web_sm')

text = """the housei is blak"""


class Removers:
    def __init__(self):
        self.abrs = {}
        self.emoji = {}

# +*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+does auto correction omiss spel items*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# identifies abbreviations

    def spellCheck(self, element):
        correction = TextBlob(element)
        correct = str(correction.correct())
        print("corrected text: "+correct)

        return correct

    def normalize(self, element):
        return str(element).lower()

    def autoCorrect(self, text):
        list = word_tokenize(text)
        d = enchant.Dict("en_US")
        print(list)

        print(" Try out section ")
        for i in range(len(list)):
            print(list[i])
            rec = self.spellCheck(list[i])
            if rec == list[i]:
                print("equals")
                suggest = ""
            else:
                print("not equal")
                list[i] = rec
                suggest = d.suggest(list[i])
                print(suggest)
        print(list)
        return suggest
# +*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+Identify Abreviationa*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# identifies abbreviations

    def readAbrev(self):
        file = open(  # this file location might need to change to accomodate the mache it is running on
            r"C:\Users\johne\Desktop\assignment3\nlp_assignment_2\server\abreviations.json", "r")  # added r to the brging of the string to fix a unicode error
        self.abrs = json.loads(file.read())

    def identifyAbrev(self, sentence):
        self.readAbrev()

        print(sentence)
        for key in self.abrs:
            if key in sentence:
                sentence = sentence.replace(key, str(self.abrs[key]))
        return sentence

    # rule : we know have a paragraph when the text hits a next line sentences


# +*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+Emojis *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+


    def reademoji(self):
        file = open(  # this file location might need to change to accomodate the mache it is running on
            r"C:\Users\johne\Desktop\assignment3\nlp_assignment_2\server\emojis.json", "r")  # added r to the brging of the string to fix a unicode error
        self.emoji = json.loads(file.read())

    def identifyEmoji(self, sentence):
        self.reademoji()

        print(sentence)
        for key in self.emoji:
            if key in sentence:
                sentence = sentence.replace(key, str(self.emoji[key]))
        return sentence


# autoCorrect(text)
print(Removers().identifyAbrev("lol"))
print(Removers().identifyEmoji("=-D"))
