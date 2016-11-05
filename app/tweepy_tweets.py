#Flask-Tweepy would be more uniform approach since we are using 
#flask extension for most of the app
#But we will only use tweepy here for convenience. We can revise this code later
import tweepy
import os

consumer_key=os.environ.get('consumer_key')
consumer_secret=os.environ.get('consumer_secret')
access_token=os.environ.get('access_token')
access_token_secret=os.environ.get('access_token_secret')

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self,status):
        print(status.text) #this prints tweets to the screen
    
    def on_error(self,status_code):
        if status_code==420:
            #returning False in on_data disconnects the stream
            return False

#now its time for the stream
def stream_tweets():
    myStreamListener=MyStreamListener()
    myStream=tweepy.Stream(auth=api.auth,listener=myStreamListener).filter(track=['#music'],async=True)
