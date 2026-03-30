# main/src/data_cleaning.py

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

STOP_WORDS = set(stopwords.words("english"))                # variable global para cargar las stopwords inglesas (the, of, at, ...)
LEMMATIZER = WordNetLemmatizer()                            # variable gloabal que carga la instancia del lematizador WordNet

def preprocess_column(text: str) -> str:
    if not isinstance(text, str):                           # comprueba que el texto pasado por parámetro no es un text
        return ""

    tokens = word_tokenize(text.lower())                    # convierte el texto a minúsculas y separa las palabras en tokens (p.ej ["this", "movie", "is", "good"])
    tokens = [
        LEMMATIZER.lemmatize(token)                         # reduce cada token a su base forma base (lemma), si es posible (p.ej "movies" -> "movie")
        for token in tokens
        if token.isalpha() and token not in STOP_WORDS      # revisa los tokens y elimina signos de puntuación, números o símbolos (token.isalpha)
                                                            # y con la variable global (STOPWORDS) elimina las palabras frecuentes que no dan significado al texto
    ]

    return ' '.join(tokens)                                 # devuelve la lista de tokens a un único string separando cada token por un espacio
