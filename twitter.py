import tweepy

def api(twitter_config):
    auth = tweepy.OAuthHandler(twitter_config['consumer_key'], twitter_config['consumer_secret'])
    auth.set_access_token(twitter_config['access_token'], twitter_config['access_token_secret'])
    api = tweepy.API(auth_handler=auth, api_root='/1.1', secure=True)
    
    return api