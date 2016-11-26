from flask import Blueprint, render_template,Flask, url_for
from flask_bootstrap import Bootstrap
import tweepy
import sys
import os

#import database information from the configuration file
from .. import config


#authentication for tweepy
auth=tweepy.OAuthHandler(config.consumer_key,config.consumer_secret)
auth.set_access_token(config.access_token,config.access_token_secret)
api=tweepy.API(auth)

app=Flask(__name__)
Bootstrap(app)



class MyStreamListener(tweepy.StreamListener):
    def on_status(self,status):
        #establish database connection
        tweet=config.mongo.tweets   #this has to go away to another file
        #print(status.text) #this prints tweets to the screen
        tweet.insert({'tweet':status.text})

    
    def on_error(self,status_code):
        if status_code==420:
            #returning False in on_data disconnects the stream
            return False

#now its time for the stream
def stream_tweets():
    myStreamListener=MyStreamListener()
    myStream=tweepy.Stream(auth=api.auth,listener=myStreamListener).filter(track=['#music'],async=True)


#tweets_now=Blueprint('/',__name__,template_folder='templates')
#@tweets_now.route('/',defaults={'page':'index'})
#@tweets_now.route('/<page>')
@app.route('/')
def twe():
    aa=stream_tweets() #live stream tweets
    user_tweets=config.mongo.tweets #establish connection to database
    user_tweets=list(user_tweets.find({},{"tweet":1})) #query databae for tweets
    for items in user_tweets:
        print(items['tweet'])
    return render_template('stream.html',user_tweets=user_tweets)




