import sys
import json

#set the path to the raw tweets file
tweets_data_path = './tweets_raw_Pokemon_Complete'

#initialize an array and open the raw tweets file for reading
tweets_data = []
tweets_file = open(tweets_data_path, "r")
tweets_jp = ""

#process each line in raw tweets file
for line in tweets_file:
    try:
        tweet = json.loads(line)
        try:
            lang = tweet['lang']
            if lang == 'ja':
                text = tweet['text']
                tweets_jp = tweets_jp + text + ";"
        except:
            continue
        
        tweets_data.append(tweet)
        
    except:
        continue

print(tweets_jp)
        
