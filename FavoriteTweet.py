import tweepy
import time

def favTweet(api,trendtopic):
    for keyword in trendtopic:
        time.sleep(30)
        search = "Keyword"
        numberOfTweets = 2
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweet.favorite()
                print('favorite the tweet')
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break