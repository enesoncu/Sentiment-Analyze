import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

def analyze_sentiment(text):

    scores = sid.polarity_scores(text)
    

    if scores['compound'] >= 0.05:
        return 'Positive'
    elif scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

while True:
    
    text = input("Enter a sentence to analyze sentiment (Enter 'exit' to quit): ")

    if text.lower() == 'exit':
        print("Exiting...")
        break

    sentiment = analyze_sentiment(text)
    print("Sentiment:", sentiment)
