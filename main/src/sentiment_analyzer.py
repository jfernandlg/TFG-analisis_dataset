from src.config import setup_environment

from nltk.sentiment import SentimentIntensityAnalyzer

setup_environment()

analyzer = SentimentIntensityAnalyzer()


def get_sentiment(text: str) -> float:
    if not isinstance(text, str) or text.strip() == "":
        return 0

    value = analyzer.polarity_scores(text)
    # sentiment = 1 if value['pos'] > 0 else 0
    compound = value["compound"]
    if compound >= 0.05:
        sentiment = 1
    elif compound <= -0.05:
        sentiment = -1
    else:
        sentiment = 0
    return sentiment
