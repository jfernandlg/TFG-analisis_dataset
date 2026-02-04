

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import  WordNetLemmatizer
nltk.download('punkt_tab')
nltk.download('wordnet')

def download_nltk_data():
    try:
        nltk.data.find('tokenizers/punkt')
    except:
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('stopwords')
        print('datos nlkt necesarios ya descargados')

download_nltk_data()

# Hace que todas gráficas se puedan ver igual en todos los notebooks
plt.style.use('ggplot')




