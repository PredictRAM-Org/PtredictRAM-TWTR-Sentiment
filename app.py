import tweepy
from textblob import TextBlob
import streamlit as st

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    return analysis.sentiment.polarity

def main():
    st.title("Stock Sentiment Analyzer")

    # User input for stock symbol
    stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL):")

    if st.button("Analyze Sentiment"):
        if not stock_symbol:
            st.warning("Please enter a valid stock symbol.")
            return

        # Fetch tweets related to the stock
        tweets = api.search(q=f"{stock_symbol} stock", count=100, lang="en")

        if not tweets:
            st.warning("No tweets found for the given stock symbol.")
            return

        # Analyze sentiment of each tweet
        sentiments = [analyze_sentiment(tweet.text) for tweet in tweets]

        # Calculate overall sentiment
        overall_sentiment = sum(sentiments) / len(sentiments)

        # Display results
        st.subheader(f"Sentiment Analysis for {stock_symbol} Stock:")
        st.write(f"Overall Sentiment: {overall_sentiment:.2f}")

        # Display individual tweet sentiments
        st.subheader("Individual Tweet Sentiments:")
        for i, tweet in enumerate(tweets):
            st.write(f"{i + 1}. {tweet.text}")
            st.write(f"Sentiment: {sentiments[i]:.2f}")
            st.write("----")

if __name__ == "__main__":
    main()
