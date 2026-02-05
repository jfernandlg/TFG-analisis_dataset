# main/src/config.py


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def ensure_nltk_resource(path: str, download_module: str):
    """"Comprueba sin un modulo de la librería NLTK existe en local,
    en caso de que no exista realizará un llamada al metodo download_nltk_data para que sea descargado
    """
    try:
        nltk.data.find(path)
    except LookupError:
        nltk.download(download_module)


def download_nltk_data():
    ensure_nltk_resource("tokenizer/punkt", "punkt")
    ensure_nltk_resource("corpora/wordnet", "wordnet")
    ensure_nltk_resource("corpora/stopwords", "stopwords")
    ensure_nltk_resource("sentiment/vader_lexicon", "vader_lexicon")


def setup_environment():
    download_nltk_data()
    # Hace que todas gráficas se puedan ver igual en todos los notebooks
    plt.style.use('ggplot')


if __name__ == '__main__':
    setup_environment()
