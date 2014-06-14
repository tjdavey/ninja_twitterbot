import webapp2
import logging
import json

from google.appengine.ext.webapp.util import run_wsgi_app

from ninja import NinjaLiveData
import twitter

config = json.loads(open('config.json').read())

twapi = twitter.api(config.get('twitter', {}))	
	
class TweetHandler(webapp2.RequestHandler):

	def get(self):
		
		tweet_config = config.get("tweet", {})
		ninja_data = NinjaLiveData(config.get("ninja", {}))
		sensor_data = ninja_data.get_data()
		
		message = tweet_config.get("template").format(**sensor_data)
		lat = tweet_config.get("lat")
		long = tweet_config.get("long")
		place_id = tweet_config.get("place_id")
		
		twapi.update_status(message, lat = lat, long = long, place_id = place_id);
		
		self.response.headers['Content-Type'] = 'application/json'   
		output = {
			'message': message
		} 
		self.response.out.write(json.dumps(output))

app = webapp2.WSGIApplication([
    ('/tweet', TweetHandler)
])

def main():
	run_wsgi_app(app)

if __name__ == '__main__':
	main()
