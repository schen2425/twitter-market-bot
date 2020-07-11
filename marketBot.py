# Required Imports
from dotenv import load_dotenv
import os
import tweepy
import datetime
from marketBotHelper import *
import finnhub
load_dotenv()

# Loads the API keys from .env file
API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
FINNHUB_KEY = os.getenv("FINNHUB_KEY")

# Authenticate with Twitter
auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Creates API object for twitter
twitterApi = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Creates API object for Finnhub
configuration = finnhub.Configuration(
    api_key={
        'token': FINNHUB_KEY
    }
)
finnhub_client = finnhub.DefaultApi(finnhub.ApiClient(configuration))

# List of stocks to track
trackedStocks = ["SPY", "DIA", "QQQ"]

# Function to post daily start price
def postStartStock():
    time = getCurrentTime()
    date = getCurrentDate()
    weekday = getStringWeekday()
    twitterApi.update_status("Hi, its " + time + " on " + weekday + ", " + date)

# Function to post daily end price
def postEndStock():
    time = getCurrentTime()
    date = getCurrentDate()
    weekday = getStringWeekday()
    twitterApi.update_status("Hi, its " + time + " on " + weekday + ", " + date)

# Checks what time it is and runs appropate method
if ((datetime.datetime.now().hour < 12) and isWeekday()):
    postStartStock()
elif ((datetime.datetime.now().hour > 14) and isWeekday()):
    postEndStock()
