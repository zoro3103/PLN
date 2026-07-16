import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER Lexicon
nltk.download('vader_lexicon')

# Initialize Analyzer
sia = SentimentIntensityAnalyzer()

# Online Reviews
reviews = [
    "This mobile phone is amazing. I absolutely love it!",
    "The battery is terrible and I am very disappointed.",
    "The product is okay. Nothing special.",
    "Excellent service! Fast delivery and great quality.",
    "Worst purchase ever. Waste of money."
]

print("Sentiment Analysis using Lexicon-Based and Rule-Based Approach\n")

for review in reviews:
    scores = sia.polarity_scores(review)

    print("Review :", review)
    print("Scores :", scores)

    compound = scores['compound']

    # Sentiment Classification
    if compound >= 0.05:
        sentiment = "Positive 😊"
        emotion = "Joy"
    elif compound <= -0.05:
        sentiment = "Negative 😞"
        emotion = "Anger / Sadness"
    else:
        sentiment = "Neutral 😐"
        emotion = "Neutral"

    print("Sentiment :", sentiment)
    print("Emotion   :", emotion)
    print("-" * 60)