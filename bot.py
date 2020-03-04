from twython import Twython, TwythonStreamer
from pcpolice import siren
from gtts import gTTS
import os


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
            if(username == 'realDonaldTrump'):
                siren()
                print("@{}: {}".format(username, tweet))
                tts_text = str(username) + "says, " + str(tweet)
                language = 'en'
                myobj = gTTS(text=tts_text, lang=language, slow=False)
                myobj.save("readthis.mp3")
                os.system("mpg321 readthis.mp3")


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
    except Exception:
        print("error, but its handled")
        continue
