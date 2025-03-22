import random

import requests
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_SID = "ACf94a2f699832425e79e33226b4c0388c"
auth_token = "3a10d181f21db58524b58eef6da8c3d1"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_api_key = "ZKBXKAY7YDYT8Z9F"
news_api_key = "69ef8dd7367a48aa8529af1d630abf18"

market_open = "09:00:00"
market_close = "19:00:00"

# date_today = datetime.datetime.today().date()
date_yesterday = str(datetime.datetime.today().date() - datetime.timedelta(days=1))
date_before_yesterday = str(datetime.datetime.today().date() - datetime.timedelta(days=2))

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key,
    "interval": "60min"

}
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "sortBy": "popularity",
    "apiKey": news_api_key,

}

# open_key = f"{date_before_yesterday} {market_open}"
# close_key = f"{date_yesterday} {market_close}"

stock_request = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
print(stock_request.json())
#
stock_data = stock_request.json()["Time Series (Daily)"]
data_list = [value for (key,value) in stock_data.items()]
print(data_list)
print(date_yesterday)

print(stock_data)
stock_open = 1200
stock_close = 1100
# print(stock_data["2024-06-18"])
stock_open = float(stock_data[date_before_yesterday]["4. close"])
stock_close = float(stock_data[date_yesterday]["4. close"])

stock_difference = round((stock_close - stock_open) / stock_open * 100)
print(f"{stock_difference}%")

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

if stock_difference > 5 or stock_difference < -5:
    news_request = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_data = news_request.json()["articles"][:3][random.randint(0,2)]
    print(news_data)
    news_description = news_data["description"]
    news_title = news_data["title"]
    news_url = news_data["url"]
    if stock_difference > 0:
        sent_message = (f"{STOCK} 🔺{stock_difference}%\n"
                        f"Headline: {news_title}\n"
                        f"Brief: {news_description}\n")
    else:
        sent_message = (f"{STOCK} 🔻{abs(stock_difference)}%\n"
                        f"Headline: {news_title}\n"
                        f"Brief: {news_description}\n")
    print("sending message\n",sent_message)

    client = Client(account_SID, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=sent_message,
        to='whatsapp:+19723458736'
    )

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
