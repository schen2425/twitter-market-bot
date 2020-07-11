# Required Imports
import datetime

# Function to get the day of week as string
# Returns: (string) The day of week
def getStringWeekday():
    today = datetime.datetime.today().weekday()
    if (today == 0):
        return "Monday"
    elif (today == 1):
        return "Tuesday"
    elif (today == 2):
        return "Wednesday"
    elif (today == 3):
        return "Thursday"
    elif (today == 4):
        return "Friday"
    elif (today == 5):
        return "Saturday"
    elif (today == 6):
        return "Sunday"

# Function that returns True if weekday
# Returns: (boolean) True if weekday
def isWeekday():
    return datetime.datetime.today().weekday() in range(0,5)

# Function that gets the current time
# Returns: (string) string of current time
def getCurrentTime():
    return datetime.datetime.now().strftime("%I:%M%p EST")

# Function that gets the date
# Returns: (string) Current date
def getCurrentDate():
    return datetime.date.today().strftime("%B %d, %Y")

# Function that gets the stock prices and returns a dict
# client: (finnhub client) Client that access API
# stockList: (array) array of strings of market tickers
# Returns: (dict) {ticker : quote object}
def getPrices(client, stockList):
    stockData = {}
    for stock in stockList:
        stockData[stock] = client.quote(stock)
    return stockData

# Function that calculates the price change in percentage
# price1: (float) new price
# price2: (float) old price
# Returns: (string) percentage change in the prices
def priceChange(price1, price2):
    return str(round(((100 * (price1 - price2)) / price2), 2))

# Function that posts the time and date
# client: (tweepy object) twitter client to make post
def postTime(client):
    time = getCurrentTime()
    date = getCurrentDate()
    weekday = getStringWeekday()
    client.update_status("Hi, it's " + time + " on " + weekday + ", " + date)

# Function that posts the stock updates for stock open
# twitterApi: (tweepy object) twitter api that makes post
# finnhubClient: (finnhub object) Finnhub api that gets data
# stockList: (array) strings of the market tickers to track
def postStartStock(twitterApi, finnhubClient, stockList):
    stockData = getPrices(finnhubClient, stockList)
    for key, value in stockData.items():
        change = priceChange(value.o, value.pc)
        twitterApi.update_status(key + " opened at $" + str(value.o) + " which is a " 
            + change + "% " + "difference than the previous close of $" + str(value.pc))

# Function that posts the stock updates for stock close
# twitterApi: (tweepy object) twitter api that makes post
# finnhubClient: (finnhub object) Finnhub api that gets data
# stockList: (array) strings of the market tickers to track
def postEndStock(twitterApi, finnhubClient, stockList):
    stockData = getPrices(finnhubClient, stockList)
    for key, value in stockData.items():
        change = priceChange(value.c, value.pc)
        twitterApi.update_status(key + " closed at $" + str(value.c) + " which is a " 
            + change + "% " + "difference than the previous close of $" + str(value.pc))