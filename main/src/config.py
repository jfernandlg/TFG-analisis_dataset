
#main/src/config.py


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import  WordNetLemmatizer

def download_nltk_data():
    try:
        nltk.data.find('tokenizers/punkt')
    except:
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('stopwords')
        print('datos nlkt necesarios ya descargados')

def setup_environment():
    download_nltk_data()
    # Hace que todas gráficas se puedan ver igual en todos los notebooks
    plt.style.use('ggplot')

if __name__ == '__main__':
    setup_environment()





