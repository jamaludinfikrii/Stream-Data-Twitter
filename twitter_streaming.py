# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '745194669227675648-etvZyzqrO3FOCQL3IWMhgWwsKMJOZEs'
ACCESS_SECRET = 'aprCaqeVgtUQ9wnakmmp0wDlLpDvKTpqjeQgOF5gJsu37'
CONSUMER_KEY = 'DUxByjeZpIPV1OHMUIThrNR0P'
CONSUMER_SECRET = 'RXTh0XbGnsYS4drN8XPYpmbudO6EqPFCaW8yxZeKEiYhLpW36O'

oauth = OAuth(ACCESS_TOKEN,ACCESS_SECRET,CONSUMER_KEY,CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)

iterator = twitter_stream.statuses.filter(track = 'jokowi' , language='id')

tweet_count = 10

print('[')
for tweet in iterator:
    tweet_count -= 1

    print(json.dumps(tweet,indent=4), ',')

    if tweet_count <= 0:
        break

print(']')
