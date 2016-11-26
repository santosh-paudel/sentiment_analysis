from pymongo import MongoClient
import os

###################    Mongodb ############################
#create mongodb client on localhost
client=MongoClient(os.environ.get('MONGO_URL'))
#creating the instance object of database 
mongo=client.mongo_tweets

####################### end  ####################


####################### Tweepy Secrets ###################
consumer_key=os.environ.get('consumer_key')
consumer_secret=os.environ.get('consumer_secret')
access_token=os.environ.get('access_token')
access_token_secret=os.environ.get('access_token_secret')

#################### end ###################################