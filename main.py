import tweepy
import time
# Authentication stuff
# Replace the below stuff with your own
# consumer_key, consumer_secret, access_token, access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.me()
print(user.name)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'enter_name_here':
        follower.follow()
        break