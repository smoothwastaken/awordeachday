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
            "consumer_key": "y99UGUcnIzaab5wBclpnDMB4v",
            "consumer_secret": "VzhNnNKsbP02bKOnsoHX8OhmuoM66JSsWSGoQhiYu8VnCDJRgh",
            "access_token": "1347838409843351552-TmR2XWCLPSjMODz6cU7iTnmjn2uoEo",
            "access_token_secret": "sub42qLbTwfCDmv49uqxhugu14HaExSj0JEitifzBJauY"
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