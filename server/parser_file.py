import nltk
from nltk import CFG, parse
import docx
from tika import parser as ps


class Parser:
    def __init__(self):
        self.text = ''

    def read_from_file(self, file):
        # self.text = textract.process(file)
        if '.docx' in file:
            doc = docx.Document(file)
            doc_text = '\n'.join(
                paragraph.text for paragraph in doc.paragraphs)
            self.text = doc_text
        elif '.pdf' in file:
            raw = ps.from_file(file)
            self.text = raw['content']
        elif '.txt' in file:
            with open(file) as f:
                self.text = ' '.join(f.readlines())

    def cfg(self):
        grammar = r"""
        NP: {<.*>*}             
            }<[\.VI].*>+{       
            <.*>}{<DT>
        PP: {<IN><NP>}
        VP: {<VB.*><NP|PP>*}
        """
        words = nltk.word_tokenize(self.text)
        tagged = nltk.pos_tag(words)

        parser = nltk.chunk.RegexpParser(grammar)
        return parser.parse(tagged)

#parser = Parser()
# parser.read_from_file("files\\apl.pdf")
# parser.cfg()
