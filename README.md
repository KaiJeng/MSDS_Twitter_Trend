# MSDS_Twitter_Trend

This project looks into top twitter trends by examining top users, urls, hashtags, words, and other metrics. Data is gathered through the tweepy package and twitter API then loaded into Spark clusters for analysis.

Since twitter is very popular in Japan, Japanese tweets were isloated to be analyzed. Due to the nature of the packaged used to split Japanese phrases, R had to be used instead to analyze those tweets.
