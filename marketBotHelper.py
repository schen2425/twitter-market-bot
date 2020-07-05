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

