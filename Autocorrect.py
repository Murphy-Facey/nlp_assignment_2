from nltk import word_tokenize
from textblob import TextBlob
import enchant

text = """the sdxzsdf is blak"""
def spellCheck( element):
        correction = TextBlob(element)
        correct = str(correction.correct())
        print("corrected text: "+correct)

        return correct

def normalize(element):
    return str(element).lower()

def autoCorrect(text):
    list = word_tokenize(text)
    d = enchant.Dict("en_US")
    print(list)

    print(" Try out section ")
    for i in range(len(list)):
        print(list[i])
        rec = spellCheck(list[i])
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
autoCorrect(text)