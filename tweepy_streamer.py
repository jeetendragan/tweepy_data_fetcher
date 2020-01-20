from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import credentials
import json

class StdOutLinstener(StreamListener):
    
    def on_data(self, data):
        data_json = json.loads(data)
        print("___________________")
        print(data_json['text'])

        f = open('output.txt', "a")
        f.write("\n"+ json.dumps(data_json))
        f.close()

        return True        
    
    def on_error(self, status):
        print(status)
        return True

if __name__ == '__main__':
    listener = StdOutLinstener()
    auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
    stream = Stream(auth, listener)
    stream.filter(track = ['Trump'])