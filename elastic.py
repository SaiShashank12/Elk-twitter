import tweepy
import sys
import json
from textwrap import TextWrapper
from datetime import datetime
from elasticsearch import Elasticsearch


consumer_key="LXigtID0j2zI4e8B8ZVDigLo9"
consumer_secret="7i24vfy5FVZxfq0bqxnjUMqwstOHi37GqNlxZK5RXDESRW2tdb"

access_token="3802591333-DOb1COgnH0XkFPhZEX3UIm7VOVWIzjzAwWlDtNY"
access_token_secret="wUcONiXzrenx9Delb6IbMCPJlx96d9c5j9MTmi3iUjr2s"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

es = Elasticsearch()

class StreamListener(tweepy.StreamListener):
    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        try:
            #print 'n%s %s' % (status.author.screen_name, status.created_at)

            json_data = status._json
            #print json_data['text']

            es.create(index="idx_twp",
                      doc_type="twitter_twp",
                      body=json_data
                     )

        except:
            print("Something went wrong when writing to the file")
            pass

streamer = tweepy.Stream(auth=auth, listener=StreamListener(), timeout=3000000000 )

#Fill with your own Keywords bellow
terms = ['obiee','oracle']

streamer.filter(None,terms)
#streamer.userstream(None)
