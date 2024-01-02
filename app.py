import streamlit as st
import tweepy

def authenticate_twitter_api(api_key, api_secret_key, access_token, access_token_secret):
    try:
        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api
    except tweepy.TweepError as e:
        st.error(f"Twitter API authentication failed: {str(e)}")
        return None

def fetch_tweets(api, query, count=10):
    try:
        tweets = api.search(q=query, count=count)
        return tweets
    except tweepy.TweepError as e:
        st.error(f"Error fetching tweets: {str(e)}")
        return []

def main():
    st.title("Twitter Sentiment Analysis App")

    # Input for Twitter API credentials
    api_key = st.text_input("Enter Twitter API Key:")
    api_secret_key = st.text_input("Enter Twitter API Secret Key:")
    access_token = st.text_input("Enter Twitter Access Token:")
    access_token_secret = st.text_input("Enter Twitter Access Token Secret:")

    # Authenticate Twitter API
    api = authenticate_twitter_api(api_key, api_secret_key, access_token, access_token_secret)

    if api:
        # Input for Twitter query
        query = st.text_input("Enter a search query:")

        if query:
            # Fetch tweets
            tweets = fetch_tweets(api, query)

            # Display tweets
            st.write(f"## Tweets for '{query}':")
            for tweet in tweets:
                st.write(f"{tweet.user.screen_name}: {tweet.text}")

if __name__ == '__main__':
    main()
