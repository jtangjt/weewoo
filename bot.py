from twython import Twython, TwythonStreamer
from pcpolice import siren

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            if(username == 'realDonaldTurmp'):
                siren()
                print("@{}: {}".format(username, tweet))


print("listening for trump tweets now")

stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
while True:
    try:
        stream.statuses.filter(follow='25073877') #This is @realDonaldTrump
    except:
        print("error, but its handled")
        continue
