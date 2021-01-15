#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import tweepy
from time import *
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

class PostTweet:
    def __init__(self, word):
        self.word = word

    def post(self):
        twitter_auth_keys = {
            "consumer_key":os.getenv("API_KEY"),
            "consumer_secret":os.getenv("API_KEY_SECRET"),
            "access_token":os.getenv("ACCESS_TOKEN"),
            "access_token_secret":os.getenv("ACCESS_TOKEN_SECRET")
        }

        auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
        )
        auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
        )
        api = tweepy.API(auth)

        status = api.update_status(status=self.word)

def tweet_it():
    url = "https://www.palabrasaleatorias.com/random-words.php"
    reponse = requests.get(url)
    if reponse.ok:
        s = BeautifulSoup(reponse.text, 'html.parser')
        word = s.find("div", {"style": "font-size:3em; color:#6200C5;"}).get_text()
        word = word.lower()
        print(word)
        tweet = PostTweet(word)
        tweet.post()

        f = open("logs.txt", "a")
        f.write(f'Tweet of the word(s) "{word}" has been succesfuly sent !\nDate & Time:{ctime()}\n\n\n')
        f.close()

tweet_it()