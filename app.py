#!/usr/bin/python3
# ----------------------------------------------------- #
#                      Imports                          #
# ----------------------------------------------------- #
import tweepy
from tweepy import Cursor
from time import sleep as time
import json
import colorama

# ----------------------------------------------------- #
#                     Dotenv Settings                   #
# ----------------------------------------------------- #
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

# ----------------------------------------------------- #
#                     Application code                  #
#                         (class)                       #
# ----------------------------------------------------- #
class App():

    ## Set the parameters in variable usable through the class
    def __init__(self, apikey, apikeysecret, accesstoken, accesstokensecret):
        self.apikey = apikey
        self.apikeysecret = apikeysecret
        self.accesstoken = accesstoken
        self.accesstokensecret = accesstokensecret

    ## Function that will check if the API Keys credentials are right
    def check(self):
        auth = tweepy.OAuthHandler(f"{self.apikey}", f"{self.apikeysecret}")
        auth.set_access_token(f"{self.accesstoken}", f"{self.accesstokensecret}")
        self.api = tweepy.API(auth)
        try:
            if self.api.verify_credentials():
                print(f"Auth is OK !")
            else:
                print("Bad credentials")
        except:
            print("Error during authentication.")

## Function that will checks and likes every mentions and RTs
    def like_mentions_rts(self):
        api = self.api
        last_mention = ""
        while True: # Infinite loop
            try:
                # Here it will check the last mention id and
                # if it is another one than the one stored in "last_mention"
                # it will like it and store again it in the variable for.
                for status in Cursor(api.mentions_timeline).items(1):
                    if status.id_str != last_mention: # Verify for the last status id
                        last_mention = status.id_str # Store the last id in the variable
                        api.create_favorite(last_mention) # Like the status

                        # Like the message
                    else:
                        print("Last mention already liked")
                time(60)

                # Only one error can append: Twitter mention-timeline rate limit.
                # So if there's an error I notify it and pass to continue.
                # It send too a private message to my personnal account to notify me that the errors occurs.
            except:
                print(f'Twitter mention-timeline rate limit has been broken (180 requests each 15min)')
                time(60)
                pass

## Function that start all the app
    def start(self):
        api = self.api
        me = api.me() # Define bot instace as "me"
        print(f"Your Twitter Bot '{me.name}' has been started !") # Message confirmation that the bot is working
        self.like_mentions_rts() # Start like_mentions_rts() function
# ----------------------------------------------------- #
#                     Api Keys to change                #
# ----------------------------------------------------- #
## Dictionnary that set the API Keys
keys = {

    "apikey":os.getenv("API_KEY"), # API Key

    "apikeysecret":os.getenv("API_KEY_SECRET"), # API Key Secret

    "accesstoken":os.getenv("ACCESS_TOKEN"), # Access Token

    "accesstokensecret":os.getenv("ACCESS_TOKEN_SECRET") # Access Token Secret

}

## Set App() class with app with keys as setting
app = App(apikey=keys["apikey"], apikeysecret=keys["apikeysecret"], accesstoken=keys["accesstoken"], accesstokensecret=keys["accesstokensecret"])

# ----------------------------------------------------- #
#                     Launch Application                #
# ----------------------------------------------------- #
## Check if the keys are good
app.check()

## Start the app
app.start()