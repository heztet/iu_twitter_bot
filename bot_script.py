import tweepy
import pushover
import time
from datetime import datetime, timedelta

# Validate that Twitter API keys can be imported
try:
	from twitter_keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
except ImportError:
	print('Could not get required keys from twitter_keys.py')
# Check if we're using Pushover
try:
	from pushover_keys import PUSHOVER_USER, PUSHOVER_APP_TOKEN
	use_pushover = True
except ImportError:
	use_pushover = False

def get_connection():
	'''Returns an authenticated Tweepy API object'''
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

	# Validate keys
	if not api.verify_credentials():
		raise IOError('Twitter API keys are invalid')
	return api

def send_tweet(string):
	'''Creates a tweet <string>'''
	api = get_connection()	
	# Send tweet
	try:
		status = api.update_status(string)
		print('Tweet "{}" sent at {}'.format(string, status.created_at))
	except tweepy.TweepError as ex:
		if (hasattr(ex, 'message')) and (ex.message[0]['code'] != 187): # Duplicate status/tweet
			raise Exception('Tweet "{}" could not be sent. Error below:\n{}'.format(string, ex))

def get_tweet():
	'''Returns the tweet to send'''
	return "It's Novemeber 18, 2017 AND IU STILL SUCKS"

if __name__ == '__main__':
	try:
		tweet = get_tweet()
		send_tweet(tweet)
	except Exception as ex:
		# Pushover alert if something goes wrong
		if use_pushover:
			timestr = time.strftime('%d/%m/%Y %H:%I %p')
			pushover.init(PUSHOVER_APP_TOKEN)
			pushover.Client(PUSHOVER_USER).send_message('Error:\n{}'.format(ex),
														title='{} error {}'.format(__file__, timestr))
		# Re-raise the exception for any logs
		raise ex
