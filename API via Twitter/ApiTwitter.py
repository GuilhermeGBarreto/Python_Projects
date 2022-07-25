import tweepy
import pandas as pd

consumer_key = 'insira aqui os seus dados'
consumer_secret = 'insira aqui os seus dados'
access_token = 'insira aqui os seus dados'
access_token_secret = 'insira aqui os seus dados'

# Authentication

'''auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acess_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()'''
client = tweepy.Client(consumer_key= consumer_key,consumer_secret= consumer_secret,access_token= access_token,access_token_secret= access_token_secret)
query = 'news'
tweets = client.search_recent_tweets(query=query, max_results=10)
for tweet in tweets.data:
    print(tweet.text)
