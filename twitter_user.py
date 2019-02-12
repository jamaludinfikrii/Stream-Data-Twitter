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
# Jenis Koneksi
twitter = Twitter(auth=oauth)

tweets = twitter.statuses.user_timeline(screen_name='BaronHartono')

print(json.dumps(tweets,indent=4))
