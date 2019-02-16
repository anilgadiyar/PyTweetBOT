import  tweepy
import time


def replyUser(api,search,numberOfTweets):
    phrase = "Hello, Thats interesting"
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        time.sleep(30)
        try:
            tweetId = tweet.user.id
            username = tweet.user.screen_name
            api.update_status("@" + username + " " + phrase, in_reply_to_status_id=tweetId)
            print("Replied with " + phrase)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break