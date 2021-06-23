# Modules for the API
from flask_cors import CORS
from flask_restful import Api, Resource
from flask import Flask, request
from binascii import a2b_base64

from glob import glob
import os
from urllib.parse import urlparse

# Modules for parsing binary data
import ast

# Modules for nlp
from parser_file import Parser
from tokenizer import Tokenizer
from tts import TTS

# Create an instanace of Flask
app = Flask(__name__)
api = Api(app)
cors = CORS(app)

t = Tokenizer()


class Files(Resource):
    def get(self):
        files = []
        result = []

        for file_type in ['*.pdf', '*.docx', '*.txt']:
            files.extend(glob('files/' + file_type))

        for file in files:
            result.append({
                'name': file.replace('files\\', ''),
                'ext': os.path.splitext(file)[1],
                'info': os.stat(file).st_size})

        with open('urls.txt', 'r') as f:
            for line in f.readlines():
                result.append({
                    'name': urlparse(line.replace('\n', '')).netloc,
                    'ext': 'url',
                    'info': line.replace('\n', '')})

        return result

    def put(self):
        data = ast.literal_eval(request.data.decode("UTF-8"))
        # print(data['type'])
        if data['type'] == 'url':
            file = open('urls.txt', 'a')
            file.write('\n' + data['url'])
            file.close()
        else:
            binary_data = a2b_base64(data['data_url'])
            fd = open('files\\' + data['file_name'], 'wb')
            fd.write(binary_data)
            fd.close()
        return {"success": True}


class Tokenize(Resource):
    def get(self):
        pass

    def put(self):
        data = ast.literal_eval(request.data.decode("UTF-8"))
        tk = Tokenizer()
        if 'http' in data['name']:
            tk.read_from_file(data['name'])
        else:
            tk.read_from_file('files\\' + data['name'])
        tokens = tk.reg_tokenize()
        optimized = tk.optimized_text()
        return {
            'tokens': tokens,
            'stop_words': tk.stop_freq(tokens),
            'pos': tk.pos_freq(tokens),
            'raw_text': optimized['text'],
            'pc': optimized['phrase_counter'],
            'sc': optimized['sent_counter'],
            'wc': optimized['word_counter']
        }


class Audios(Resource):
    def put(self):
        pass

    def post(self):
        tts = TTS()
        data = ast.literal_eval(request.data.decode("UTF-8"))
        if t.text == '':
            t.read_from_file('files\\' + data['filename'])
        tts.init_sentences(t.sent_tokenize())
        tts.generate_audio(data['folder'], data['index'], data['play'])

# class Parse(Resource):
#     def put(self):
#         print(request.data)
#         data = ast.literal_eval(request.data.decode("UTF-8"))
#         parser = Parser()
#         token = Tokenizer()
#         token.read_from_file(data['file'])
#         # parser.read_from_file(data['file'])
#         return {
#             'cfg': parser.cfg(token.text)
#         }


api.add_resource(Files, "/files")
api.add_resource(Tokenize, "/tokenize")
# api.add_resource(Audios, "/audios")
# api.add_resource(Parse, "/parse")

if __name__ == "__main__":
    app.run(debug=True)
