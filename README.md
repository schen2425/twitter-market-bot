# twitter-market-bot
A Twitter bot giving updates about the stock market

# Setup
Make sure dependencies are installed

Create a .env file in the root directory of this project
```
API_KEY = "Your API KEY"
API_KEY_SECRET = "Your Secret API KEY"
ACCESS_TOKEN = "Your Access Token"
ACCESS_TOKEN_SECRET = "Your Secret Access Token"
FINNHUB_KEY = "Your Finnhub key"
```

Create a cron job to run code at 9:30 AM EST and 4:30 PM EST
Do this with "crontab -e" and add the following to the end of file
```
30 9 * * * CMD TO RUN marketBot.py
0 16 * * * CMD TO RUN marketBot.py
```