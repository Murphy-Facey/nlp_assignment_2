import nltk
from nltk import sent_tokenize, Tree
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeView
from PIL import Image
import string
import os

class Parser:
    def __init__(self):
        self.text = ''

    def cfg(self, filename):
        grammar = r"""
        NP: {<.*>*}             
            }<[\.VI].*>+{       
            <.*>}{<DT>
        PP: {<IN><NP>}
        VP: {<VB.*><NP|PP>*}
        """

        counter = 0
        os.mkdir("/parse")
        sentences = sent_tokenize(self.text)

        for sentence in sentences:
            sent_without_punctuations = sentence.translate(str.maketrans('', '', string.punctuation))
            words = nltk.word_tokenize(sent_without_punctuations)
            tagged = nltk.pos_tag(words)
            parser = nltk.chunk.RegexpParser(grammar)
            for parsed in parser.parse(tagged):
                tree_canvas = TreeView(parsed)
                tree_canvas._cframe.print_to_file(f'parse/{filename}_{counter}.ps')
                counter += 1
        return counter
        
    def convert_to_png(self, filename, index):
        img = Image.open(f"parse/{filename}_{index}.ps")
        img.save(f"img/{filename}_{index}.png")
        return f"img/{filename}_{index}.png"

            # os.system(f"convert parse/{file} img/{file.replace('.ps', '.png')}")

