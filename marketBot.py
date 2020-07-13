# Required Imports
from dotenv import load_dotenv
import os
import tweepy
import datetime
from marketBotHelper import postStartStock, postEndStock, postTime, isWeekday
import finnhub
import time

# Loads the API keys from .env file
load_dotenv()
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
trackedStocks = ["DIA", "SPY", "QQQ"]

# Function to post daily start price
def openPost():
    postTime(twitterApi)
    postStartStock(twitterApi, finnhub_client, trackedStocks)

# Function to post daily end price
def closePost():
    postTime(twitterApi)
    postEndStock(twitterApi, finnhub_client, trackedStocks)

# Checks what time it is and runs appropate method
# Sleeps for 65 seconds since API seems to lag by 1 min
if ((datetime.datetime.now().hour < 12) and isWeekday()):
    time.sleep(65)
    openPost()
elif ((datetime.datetime.now().hour > 14) and isWeekday()):
    time.sleep(65)
    closePost()
