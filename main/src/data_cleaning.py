# main/src/data_cleaning.py

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

STOP_WORDS = set(stopwords.words("english"))
LEMMATIZER = WordNetLemmatizer()


# def preprocess_column(column):
#
#
#     STOP_WORDS = set(stopwords.words('english'))
#     # column = column.str.lower()
#     tokens = word_tokenize(column)
#     filtered_tokens = [token for token in tokens if token not in STOP_WORDS]
#     LEMMATIZER = WordNetLemmatizer()
#     lemmatized_tokens = [LEMMATIZER.lemmatize(token) for token in filtered_tokens]
#     preprocesed_text = ' '.join(lemmatized_tokens)
#     return preprocesed_text

def preprocess_column(text: str) -> str:
    if not isinstance(text, str):
        return ""

    tokens = word_tokenize(text.lower())
    tokens = [
        LEMMATIZER.lemmatize(token)
        for token in tokens
        if token.isalpha() and token not in STOP_WORDS
    ]

    return ' '.join(tokens)
