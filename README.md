# LIZ Text to Speech Engine

## How to install



I would recommend creating a virtual environment for python. This allows you to have all the necessary packages one place and it allow you to easily remove them. Learn more about virtual environment in python [here]('https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/').You need navigate to the server folder, and run the following command to download all the python packages:
```
pip install requirements.txt
```

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
yarn add
yarn start
```

