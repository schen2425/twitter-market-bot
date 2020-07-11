# Required Imports
import datetime

# Function to get the day of week as string
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
def isWeekday():
    return datetime.datetime.today().weekday() in range(0,5)

# Returns string of current time
def getCurrentTime():
    return datetime.datetime.now().strftime("%I:%M%p EST")

# Returns string of current date
def getCurrentDate():
    return datetime.date.today().strftime("%B %d, %Y")

# Gets the stock prices and returns a dict
def getPrices(client, stockList):
    stockData = {}
    for stock in stockList:
        stockData[stock] = client.quote(stock)
    return stockData

# Calculates the price change in percentage
def priceChange(price1, price2):
    return str(round(((100 * (price1 - price2)) / price2), 2))

# Posts the time and date
def postTime(client):
    time = getCurrentTime()
    date = getCurrentDate()
    weekday = getStringWeekday()
    client.update_status("Hi, it's " + time + " on " + weekday + ", " + date)

# Posts the stock updates for stock open
def postStartStock(twitterApi, finnhubClient, stockList):
    stockData = getPrices(finnhubClient, stockList)
    for key, value in stockData.items():
        change = priceChange(value.o, value.pc)
        twitterApi.update_status(key + " opened at $" + str(value.o) + " which is a " 
            + change + "% " + "difference than the previous close of $" + str(value.pc))

# Posts the stock updates for stock open
def postEndStock(twitterApi, finnhubClient, stockList):
    stockData = getPrices(finnhubClient, stockList)
    for key, value in stockData.items():
        change = priceChange(value.c, value.pc)
        twitterApi.update_status(key + " closed at $" + str(value.c) + " which is a " 
            + change + "% " + "difference than the previous close of $" + str(value.pc))