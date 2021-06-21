import nltk
from nltk import word_tokenize, sent_tokenize
import spacy
nlp = spacy.load('en_core_web_sm')


text = """I would recommend creating a virtual environment for python. This allows you to have all the necessary packages one place and allows you to easily remove them. Learn more about virtual environment in python here.You need navigate to the server
 folder after creating and activating the virtual environment. I would recommend creating a virtual environment for python ."""

rep = """ I I love you """


class Removers:

    def SpacySentencizer(text):
        about_doc = nlp(text)
        sentences = list(about_doc.sents)

        for sentence in sentences:
            print(sentence)
        print("-------------------------Stuff from the sentences---------------------------------")
        a = ' '.join(Removers.removesrepeated(str(sentences).split()))
        print(a)

    def sentenceRemover(text):  # removes repeated sentences from tokens
        sentences = sent_tokenize(text)
        print(sentences)
        print("-------------------------Stuff from the sentences---------------------------------")
        a = ' '.join(Removers.removesrepeated(str(sentences).split()))
        print(a)
        return a

    def wordRemover(text):
        sentences = Removers.sentenceRemover(text)
        buffer = []
        # splits text into sentences then splits the sentences into tokens
        for i in range(len(sentences)):
            print("Sentence", i)
            print(sentences[i])
            print("Tokens in sentence", i)
            words = word_tokenize(sentences[i])
            print(words)  # words is a list
            # -------------------------------------------------
            buffer = words
            print("items in buffer")
            print(buffer)

            for index, elem in enumerate(buffer):
                if (index+1 < len(buffer) and index - 1 >= 0):

                    prev_el = str(buffer[index-1])
                    curr_el = str(elem)
                    next_el = str(buffer[index+1])

                print(prev_el, curr_el, next_el)
            print("++++++++++++++++++++++++++++++++++++++++++")

        # print(buffer)
        # removes repeated words or phrases from tokenizer text
        # words = word_tokenize(text)
        # print(words)
        return

    def removesrepeated(sentences):
        ulist = []
        [ulist.append(x) for x in sentences if x not in ulist]
        return ulist

    def sentenceLength(sentence):
        if len(sentence) <= 1:
            print(sentence)


# Removers.sentenceRemover(text)
# Removers.wordRemover(rep)
# Removers.SpacySentencizer(text)

# for i in range(0,len(words)):

#     print("buffer content", buffer[i])
#     if buffer[i] == buffer[i+1]:
#         print("repeated")
#         #buffer[i+1] = buffer[i+2]
# words = buffer


# ----------------------------------------------------------------------------
# string = "big black bug bit a big black dog on his big black nose"
# # Converts the string into lowercase
# string = string.lower()

# # Split the string into words using built-in function
# words = string.split(" ")
def remover2(string):
    string = string.lower()

    # Split the string into words using built-in function
    words = string.split(" ")

    print("Duplicate words in a given string : ")
    for i in range(0, len(words)):
        count = 1
        for j in range(i+1, len(words)):
            if(words[i] == (words[j])):
                count = count + 1
                # Set words[j] to 0 to avoid printing visited word
                words[j] = "0"

        # Displays the duplicate word if count is greater than 1
        if(count > 1 and words[i] != "0"):
            print(words[i])


remover2(rep)
