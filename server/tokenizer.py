import re
import spacy
import docx
import pdfplumber

from optimizer import Optimizer

class Tokenizer:
    def __init__(self):
        self.text = ''

    def read_from_file(self, file):
        # self.text = textract.process(file)
        if '.docx' in file:
            doc = docx.Document(file)
            doc_text = '\n'.join(paragraph.text for paragraph in doc.paragraphs)
            self.text = doc_text
        elif '.pdf' in file:
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    self.text = page.extract_text() + '\n'
            # raw = parser.from_file(file)
            # self.text = raw['content']
        elif '.txt' in file:
            with open(file) as f:
                self.text = ' '.join(f.readlines())

    def reg_tokenize(self):
        # Create tokens by white space
        tokens = self.text.split()
        for index, token in enumerate(tokens):
            if re.findall(r'(?:[A-Z]\.)+', token) != []:
                tokens[index] = [token]
                continue
            if re.findall(r'^\d*[.,]?\d*$', token) != []:
                tokens[index] = [token]
                continue
            if re.findall(r'\$[1-9]\d*(?:\.\d{2})?(?=\s|$)', token):
                tokens[index] = [token]
                continue
            if re.findall(r'[0-9]{1,4}[\_|\-|\/|\|][0-9]{1,2}[\_|\-|\/|\|][0-9]{1,4}', token):
                tokens[index] = [token]
                continue
            if re.findall(r'(?<=°[FfCcKk])\.', token):
                tokens[index] = [token]
                continue

            if re.findall(r"\w+|[^\w\s]", token) != []:
                items = re.findall(r"\w+|[^\w\s]", token)
                tokens[index] = items
                
        flat_list = [item for sublist in tokens for item in sublist]
        return self.token_info(flat_list)
    
    def tokenize(self, text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        for token in doc:
            print(token.text)
    
    def token_info(self, tokens):
        nlp = spacy.load("en_core_web_sm")
        info = []
        for idx, token in enumerate(tokens):
            doc = nlp(token)
            info.append({
                'text': token,
                'index': idx,
                'lemma': doc[0].lemma_,
                'is_stop_word': doc[0].is_stop,
                'pos': doc[0].pos_,
                'shape': doc[0].shape_
            })
        return info
    
    def sent_tokenize(self):
        sentences = []
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(' '.join(self.text.split()))
        for sent in doc.sents:
            sentences.append(sent.text)
        return sentences
    
    def pos_freq(self, tokens):
        pos = {}
        for token in tokens:
            if (token['pos'] in pos):
                pos[token['pos']] += 1
            else:
                 pos[token['pos']] = 1
        return pos
    
    def stop_freq(self, tokens):
        stop_words = {}
        for token in tokens:
            if token['is_stop_word'] and (token['text'] in stop_words):
                stop_words[token['text']] += 1
            elif token['is_stop_word']:
                stop_words[token['text']] = 1
            
        return stop_words
    
    def optimized_text(self):
        optimizer = Optimizer()
        opt_text = optimizer.optimize(self.text)
        return ' '.join(opt_text) 
