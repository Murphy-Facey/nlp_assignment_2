import enchant
import json
import nltk
from nltk import word_tokenize, sent_tokenize
import spacy
nlp = spacy.load('en_core_web_sm')


text = """It's not only writers who can benefit from this free online tool. It's not only writers who can benefit from this free online tool. If you're a programmer who's working on a project where blocks of text are needed, this tool can be a great way to get that. It's a good way to test your programming and that the tool being created is working well."""

rep = """ I I I i love you you You this is something else """

class Removers:
    def __init__(self):
        self.phrases = {}

    # should remove replicated from whatever list that is sent - but it curretly lets leaves reminants of the item that should be removed
    def SpacySentencizer(self, text):
        about_doc = nlp(text)
        sentences = list(about_doc.sents)

        for sentence in sentences:
            str(sentence).lower().replace(" ", "")
            print(sentence)
        print("-------------------------Stuff from the sentences---------------------------------")
        a = ''.join(Removers.removesrepeated(str(sentences).split())).lower()
        print(a)

    def sentenceRemover(self, text):  # removes repeated sentences from tokens
        sentences = sent_tokenize(text)
        print(sentences)
        return sentences

    def removesrepeated(self, sentences):
        ulist = []
        [ulist.append(x) for x in sentences if x not in ulist]
        # ulist = [x for x in sentences if x not in ulist]
        return ulist

    # def sentenceLength(sentence):
    #     if len(sentence) <= 1:
    #         print(sentence)

# +*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+Word Remover *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# removes repeating words
    # -----------------------------------Word Remover-------------------------------
    # should removes the next word in the  duplicate it the system
    def wordRemover(self, text):
        sentences = Removers().sent_tokenizer(
            text)  # does the sentencing of the text
        buffer = []
        # splits text into sentences then splits the sentences into tokens
        for i in range(len(sentences)):
            # the sentence we are dealin g with the sentence3 number
            print("Sentence", i)
            print(sentences[i])
            print("Tokens in sentence", i)  # the tokens in the sentence
            words = word_tokenize(sentences[i])
            print(words)  # words is a list
            # -------------------------------------------------
            buffer = words  # assigns the tokens to another list for manipulation
            print("items in buffer")
            print(buffer)  # show the items in the buffer

            # set the previous element being checked
            # to an first token
            prev_elem = buffer[0]

            # for all the elements in the buffer
            for curr_elem in buffer:
                # if the current element is the same as
                # the previous element, then remove the
                # previous element

                if prev_elem.lower() == curr_elem.lower():
                    buffer.remove(prev_elem)
                else:
                    # Otherwise, upate the previous
                    # element to current element
                    prev_elem = curr_elem
            print("++++++++++++++++++buffer now ++++++++++++++++++++++++")
            print(buffer)

# +*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+Redundancy Remover *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# removes redundant phrases

    def readRedundantPhrases(self):
        file = open("redundant_phrases.json", "r")  # added r to the brging of the string to fix a unicode error
        self.phrases = json.loads(file.read())

    def removeRedundantPhrasee(self, sentence):
        self.readRedundantPhrases()

        print(sentence)
        for key in self.phrases:
            if key in sentence:
                sentence = sentence.replace(key, str(self.phrases[key]))
        return sentence
    # rule : we know have a paragraph when the text hits a next line sentences

    def paragrapher(self, text):
        paragraph = str(text).split('\n')
        # print(paragraph)
        return paragraph

    def normalizer(self, text):
        return str(text).lower()


# +*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+Sentence remover *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# removes duplicate sentences in same paragraph

    def sent_remover(self, text):
        # this is the list of unique sentences 
        unique_sents = []
        paragraphs = self.paragrapher(text)

        for paragraph in paragraphs:
            print("+++++---------------++++PARAGRAPH+++---------------")
            print(paragraph)
            sentences = self.sent_tokenizer(paragraph)
            # for sentence in sentences:
            #     print("+++++++++++++---------------++++SENTENCE+++---------------+++++++++++++")
            #     print(sentence, sentences.count(sentence))
            
            unique_sents = ' '.join(self.unique_list(sentences))
            for sent in unique_sents:
                self.removeRedundantPhrasee(sent)
                self.remove_duplicate_words(sent)

            print("+++++++++++++++++_________________without reduncdancies_____________+++++++++++++++")
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


d = enchant.Dict("en_US")
d.check("Hello")
d.check("Helo")
d.suggest("Helo")


# +*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+testing segment *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+
# Removers.testRemoval
# Removers.SpacySentencizer(text)
# Removers().wordRemover(rep)
# print(Removers().removeRedundantPhrasee(
#     "Will you cease and desist that infernal racket! We should plan ahead for Christmas."))
# Removers().sentenceRedundanceRemover1(text)
# Removers().paragrapher(text)
Removers().sent_remover(text)
