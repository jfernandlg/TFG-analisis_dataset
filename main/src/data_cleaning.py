

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import  WordNetLemmatizer


def preprocess_column(column):
    stop_words = set(stopwords.words('english'))
    # column = column.str.lower()
    tokens = word_tokenize(column)
    filtered_tokens = [token for token in tokens if token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    preprocesed_text = ' '.join(lemmatized_tokens)
    return preprocesed_text