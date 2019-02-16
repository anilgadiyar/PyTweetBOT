import tweepy
import ReplyTweet
import threading
import time


def retweet_few_users(api,trendtopic):
   for keyword in trendtopic:
        time.sleep(30)
        search = keyword
        numberOfTweets = 2
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            t3 = threading.Thread(target=ReplyTweet.replyUser(api,search,numberOfTweets), daemon=True)
            t3.start()
            t3.join()
            try:
                tweet.retweet()
                print('Retweeted the tweet')
            except tweepy.TweepError as e:
                 print(e.reason)
            except StopIteration:
                break
