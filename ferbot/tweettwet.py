import tweepy
import time
auth = tweepy.OAuthHandler('ecdQeDb5rfjFLh6rBPH7VqEtn',
                           'ltg50ms4R4yv7wYoxvh7lBw1OyI1MaM7sKkZM18cKWPLoyhckD')
auth.set_access_token('236809758-0LWqwWGWFxBtutMDcQcqXgJdZFUdTvIN1yj39E9p',
                      'fGezw4ElEIyc5dfa1PcJGtBLteHg1ejbFq9nvwV2cfgWr')

api = tweepy.API(auth)
user = api.me()

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()

    except tweepy.RateLimitError:
        time.sleep(1000)
# genrous bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     follower.follow()
#     break

search_string = 'Math Rock'
numberOfTweets = 10

for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(numberOfTweets)):
    try:
        tweet.favorite()
        print('I like that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break