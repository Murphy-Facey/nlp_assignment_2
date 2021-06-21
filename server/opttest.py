import nltk
from nltk import word_tokenize, sent_tokenize
import spacy
nlp = spacy.load('en_core_web_sm')


text = """I would recommend creating a virtual environment for python. This allows you to have all the necessary packages one place and allows you to easily remove them. Learn more about virtual environment in python here.You need navigate to the server
 folder after creating and activating the virtual environment. I would recommend creating a virtual environment for python."""

rep = """ I I love you """


class Removers:
    # should remove replicated from whatever list that is sent - but it curretly lets leaves reminants of the item that should be removed
    # r
    def SpacySentencizer(text):
        about_doc = nlp(text)
        sentences = list(about_doc.sents)

        for sentence in sentences:
            str(sentence).lower().replace(" ", "")
            print(sentence)
        print("-------------------------Stuff from the sentences---------------------------------")
        a = ''.join(Removers.removesrepeated(str(sentences).split())).lower()
        print(a)

    def sentenceRemover(text):  # removes repeated sentences from tokens
        sentences = sent_tokenize(text)
        print(sentences)
        return sentences

    def removesrepeated(sentences):
        ulist = []
        [ulist.append(x) for x in sentences if x not in ulist]
        # ulist = [x for x in sentences if x not in ulist]
        return ulist

    # def sentenceLength(sentence):
    #     if len(sentence) <= 1:
    #         print(sentence)

    # ----------------------------------------------------------------------------------
    # -----------------------------------Word Remover-------------------------------
    # should removes the next word in the  duplicate it the system
    def wordRemover(text):
        sentences = Removers.sentenceRemover(
            text)  # does the sentencing of the text
        buffer = []
        nwWord = []
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

            for elem in buffer:
                curr_el = elem

                # this checks if the items is not currently
                # at the end of the list
                if buffer.index(elem) < len(buffer):
                    next_el = buffer[buffer.index(curr_el)+1]
                if next_el == curr_el:
                    buffer.remove(next_el)

            print("++++++++++++++++++buffer now ++++++++++++++++++++++++")
            print(buffer)

    def testRemoval():
        list = ["boom", "bam", "bomb"]
        list. pop(2)  # error
        print(list)


# Removers.testRemoval
# Removers.SpacySentencizer(text)
Removers.wordRemover(rep)


# def normalise():
#     return [''.join(x.split()).lower() for x in tests]

# def remove_sentence():
#     norm_sents = normalise()
#     for sent in norm_sents:
#         curr_elem = sent

#         # this checks if the items is not currently
#         # at the end of the list
#         if norm_sents.index(sent) < len(norm_sents):
#             # if not, set the next item
#             next_elem = norm_sents[norm_sents.index(sent) + 1]

#         if next_elem == curr_elem:
#             norm_sents.remo
