import os
from urllib import request
from dotenv import load_dotenv
from requests import get
from datetime import date, timedelta
from twilio.rest import Client

load_dotenv()   
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

STOCK_NAME = "IVV"
COMPANY_NAME = "Vanguard Total Stock Market ETF"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# havinig issues with "" being needed for API key in .env but not for Aplha key. Strange. Ran out of API calls testing oops. 
NEWS_PARAMS = {
    "q":COMPANY_NAME,
    "apiKey": "4f4fbf3c336c422b99f1d055c06b6282",
}

# detect 5% change in stock price over last 2 days
stock_data = get(f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={ALPHA_VANTAGE_API_KEY}").json()

today = date.today()

yesterday = today - timedelta(days=1)
yesterday_str = yesterday.strftime("%Y-%m-%d")

day_before_yesterday = today - timedelta(days=2)
day_before_yesterday_str = day_before_yesterday.strftime("%Y-%m-%d")

yesterday_close = float(stock_data["Time Series (Daily)"][yesterday_str]["4. close"])
day_before_yesterday_close = float(stock_data["Time Series (Daily)"][day_before_yesterday_str]["4. close"])

percent_change = (yesterday_close - day_before_yesterday_close)/day_before_yesterday_close

# get last 3 news if 5% or greater change in price
if abs(percent_change) > .000005:
    news_data = get(NEWS_ENDPOINT, NEWS_PARAMS).json()
    articles = news_data["articles"]
    three_articles = articles[:3]
    
    # format articles for sending 
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)

    # send message via twilio (can't test until approved)
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            to=TWILIO_PHONE_NUMBER,
            from_=TWILIO_PHONE_NUMBER,
            body=article
        )




    


