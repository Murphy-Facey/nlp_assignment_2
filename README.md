# LIZ Text to Speech Engine

This is text to speech engine created using ReactJS for the frontend and Python for the backend. 

## How to install

I would recommend creating a virtual environment for python. This allows you to have all the necessary packages one place and allows you to easily remove them. Learn more about virtual environment in python [here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/).You need navigate to the server folder after creating and activating the virtual environment, and run the following command to download all the python packages:

If the command above doesn't work, you can run the following code to install most of the dependencies:
```
pip install pygame python_docx Flask gTTS Flask_RESTful Flask_Cors spacy pdfplumber nltk docx pyenchant textblob
python -m spacy download en_core_web_sm
```

You are required to create two folders in the server folder
- files/ 
- audios/

Please note the NLTK packages, you are erequired to download some files. Run the following code in your terminal:
```python
python
import nltk
nltk.download()
```

You will have to run the server first by executing the following command from the server folder:
```
python main.py
```

Then you can navigate the client folder, ann run the following commands from the terminal:
```cmd
yarn install
yarn start
```

## Things to do

- [ ] Update the UI 
- [x] Change the TTS to be handled on the client side
- [x] Create the optimizer.py file 
    - [x] Add the remove repeated words function
    - [x] Add the remove repeated sentences function
    - [x] Add the remove redundant phrases 
