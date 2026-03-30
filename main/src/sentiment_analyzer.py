from src.config import setup_environment

from nltk.sentiment import SentimentIntensityAnalyzer

setup_environment()

analyzer = SentimentIntensityAnalyzer()   # Diccionario de palabras con polaridad (positivas/negativas)


# 1: positvo
# -1: negativo
# 0: neutral

def get_sentiment(text: str) -> float:
    if not isinstance(text, str) or text.strip() == "":         # Comprueba que el texto pasado por parámetro no es un tipo text
        return 0

    value = analyzer.polarity_scores(text)                      # analiza el texto mediante el diccionario midiendo
                                                                # la polaridad devolviendo un dict con 4 proporciones:
                                                                    #neg, pos, neu, compound -> (-1, 1)
                                                                # compound es el indicador general para medir si el
                                                                # texto analizado es positivo/negativo/neutral a partir
                                                                # de un único valor

    # sentiment = 1 if value['pos'] > 0 else 0
    compound = value["compound"]                                # extremos la proporción del compound
    if compound >= 0.05:                                        # si >= 0.05 entonces el texto es positivo
        sentiment = 1
    elif compound <= -0.05:                                     # si es <= -0.05 entonces el texto es negativo
        sentiment = -1
    else:
        sentiment = 0                                           # sino es neutral
                                                                # (-0.05, 0.05) umbrales de compound para clasificar
                                                                # la polaridad en ambos extremos
    return sentiment                                            # devuelve el sentimiento obtenido del texto
