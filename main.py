import webapp2
import os
import json
import logging
import httplib2
import tweepy

from google.appengine.api import urlfetch
from google.appengine.ext.webapp.util import run_wsgi_app

config = json.loads(open('config.json').read())

twitter_conf = config['twitter']
ninja_conf = config['ninja']


try:
	auth = tweepy.OAuthHandler(twitter_conf['consumer_key'], twitter_conf['consumer_secret'])
	auth.set_access_token(tw_access_token, tw_access_token_secret)
	api = tweepy.API(auth_handler=auth, api_root='/1.1', secure=True)
except Exception as e:
	logging.error(e)
	service = None
	api = None
class TweetHandler(webapp2.RequestHandler):

	def get(self):
		temp = self.retrieve(ninja_temp_sensor, ninja_api_key)
		humid = self.retrieve(ninja_humidity_sensor, ninja_api_key)
		self.tweet(temp, humid)

	def retrieve(self, sensor, api_key):
		url = "https://a.ninja.is/rest/v0/device/%{sensor}/data?interval=1min&fn=mean&user_access_token={api_key}".format(sensor=sensor, api_key=api_key)
		logging.info(url)
		fetch_result = urlfetch.fetch(url, deadline=20)
		result = json.loads(fetch_result.content)
		
		if ['last_data'] in result and ['DA'] in result['last_data']:
			data_point = result['data'][(len(result['data'])-1)]['v']
		else:
			data_point = None
			
		return last_point

	def tweet(self, temperature, humidity):
		api.update_status("Current Temperature and Humidity: %s degrees Celcius, %s%% relative humidity" % (temperature, humidity))


app = webapp2.WSGIApplication([
    ('/tweet', TweetHandler)
])

def main():
	run_wsgi_app(app)

if __name__ == '__main__':
	main()
