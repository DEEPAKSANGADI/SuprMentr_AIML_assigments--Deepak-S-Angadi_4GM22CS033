from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze sentiment of text and return polarity and subjectivity.
    Polarity: -1 (negative) to 1 (positive)
    Subjectivity: 0 (objective) to 1 (subjective)
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment, polarity, subjectivity

# Test on 5 reviews
reviews = [
    "This product is absolutely amazing! I love it.",
    "Terrible quality. Very disappointed with this purchase.",
    "It's okay, nothing special but it works.",
    "Best purchase ever! Highly recommend to everyone.",
    "Waste of money. Broke after one day."
]

print("Sentiment Analysis Results:\n")
for i, review in enumerate(reviews, 1):
    sentiment, polarity, subjectivity = analyze_sentiment(review)
    print(f"Review {i}: {review}")
    print(f"Sentiment: {sentiment} | Polarity: {polarity:.2f} | Subjectivity: {subjectivity:.2f}\n")