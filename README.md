-Sentiment Analysis with NLTK and VADER-

This Python project performs sentiment analysis on input sentences using the NLTK library with VADER (Valence Aware Dictionary and Sentiment Reasoner). 
It provides a simple interface for users to input sentences and receive sentiment analysis results.

*Requirements*

-NLTK library

*Installation*

1- Clone the repository to your local machine:
git clone https://github.com/enesoncu/sentiment-analysis.git

2-Install the required dependencies using pip:
pip install nltk

3-Download the VADER lexicon for sentiment analysis:
python -m nltk.downloader vader_lexicon

*Usage*

Run the script sentiment_analysis.py:
python sentiment_analysis.py

Type 'exit' to quit the program.

*How it Works*

The sentiment_analysis.py script uses the NLTK library to perform sentiment analysis on input sentences. 
It utilizes the VADER (Valence Aware Dictionary and Sentiment Reasoner) module from NLTK, which is specifically designed for analyzing sentiments expressed in social media and other informal texts.

The script prompts the user to enter a sentence for analysis. It then calculates the sentiment score using VADER and classifies the sentiment as 'Positive', 'Negative', or 'Neutral' based on the compound score provided by VADER.
