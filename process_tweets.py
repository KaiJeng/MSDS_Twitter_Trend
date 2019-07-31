import sys
import json

#set the path to the raw tweets file
tweets_data_path = './tweets_raw_backup copy'

#initialize an array and open the raw tweets file for reading
tweets_data = []
tweets_file = open(tweets_data_path, "r")

#process each line in raw tweets file
for line in tweets_file:
    try:
        tweet = json.loads(line)
        #Get "real" name then user name
        try: 
            real_name = (tweet['user']['name'])
        except:
            real_name = "UNKNOWN"
        try:
            user_name = (tweet['user']['screen_name'])
        except:
            user_name = "UNKNOWN"
        #Get follower count to determine top users    
        try:
            followers_count = (tweet['user']['followers_count'])
        except:
            followers_count = "UNKNOWN"
        #Get Verified flag for context
        try:
            verified_status = (tweet['user']['verified'])
        except:
            verified_status = "UNKNOWN"
        #Get tweet as well as identify possible retweet and mark it as such
        try:
            text = tweet['text']
            text_form = []
            text_form.append(text)
            if text[0:4] == "RT @":
                re_tweet = "YES"
            else:
                re_tweet = "NO"
        except:
            text_form = []
            re_tweet = "UNKNOWN"
        #Get language of tweet
        try:
            lang = tweet['lang']
        except:
            lang = "UNKNOWN"
        #Get hashtags of tweet 
        try:
            hashtags = ([tweet['entities']['hashtags'][i]['text'] for i in range(0,len(tweet['entities']['hashtags']))])      
        except:
            hashtags = "UNKNOWN"
        #Get url from tweet
        try:
            url = (tweet['entities']['urls'][0]['url'])
        except:
            url = "UNKNOWN"

        #Print all metrics into tab separated line
        #print([real_name,user_name,followers_count,verified_status,text,lang,hashtags,url])
        print(real_name + "\t" + user_name + "\t" + str(followers_count) + "\t" + str(text_form) + "\t" + re_tweet + "\t" + lang + "\t" + str(hashtags) + "\t" + url)
        #print(str(text_form))
        tweets_data.append(tweet)
        
    except:
        continue
        
        
#print how many tweets were processed
print (len(tweets_data))
