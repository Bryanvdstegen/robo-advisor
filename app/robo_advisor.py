# app/robo_advisor.py

import csv
import json
import os

import requests
import datetime

from dotenv import load_dotenv
load_dotenv()

# utility function to convert float or integer to USD-formatted string (for printing)
# 

def to_usd(my_price):
    return "${0:,.2f}".format(my_price) #>12,000.71


#
# INFO REQUESTS
#

api_key = os.environ.get("ALPHAVANTAGE_API_KEY") #"demo"
symbol = input("Please specify a stock symbol (e.g. AMZN) and press enter: ") # This works

# def get_response(symbol):
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
#     response = requests.get(request_url)
#     parsed_response = json.loads(response.text)
#     return parsed_response # Not sure about this symbol code

# request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo" # API = ALPHAVANTAGE_API_KEY="LJK9HOM2QV3DGSJP"

response = requests.get(request_url)
# print(type(response)) #> class 'requests.models.Response'>
# print(response.status_code) #> 200
# print(response.text) # dictionary, string

# quit()

parsed_response = json.loads(response.text)

if 'Meta Data' in parsed_response:
    last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

# breakpoint()

    tsd = parsed_response["Time Series (Daily)"]

    dates = list(tsd.keys())

    latest_day = dates[0] # "2019-02-20" TODO: Sort this so that the lastest day is first

    latest_close = tsd[latest_day]["4. close"]

# get high price for each day
# high_prices = [10, 30, 20, 5]

    high_prices = []
    low_prices = []


    for date in dates:
        high_price = tsd[date]["2. high"]
        high_prices.append(float(high_price))
        low_price = tsd[date]["3. low"]
        low_prices.append(float(low_price))


    # maximum of all the high prices
    recent_high = max(high_prices)
    recent_low = min(low_prices)


    time_now = datetime.datetime.now()
    formatted_time_now = time_now.strftime("%Y-%m-%d %H:%M:%S")

#
#

# csv-mgmt/write_teams.py

# csv_file_path = "data/prices.csv" # a relative filepath
    csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

    csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

    with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader() # uses fieldnames set above
        for date in dates:
            daily_prices = tsd[date]
            writer.writerow({
                "timestamp": date,
                "open": daily_prices["1. open"],
                "high": daily_prices["2. high"],
                "low": daily_prices["3. low"],
                "close": daily_prices["4. close"],
                "volume": daily_prices["5. volume"]
            })

    def toBuyOrNotToBuy(recent_low, latest_close):
        if(((latest_close/recent_low)-1)*100 < 20):
            return("BUY!",((latest_close/recent_low)-1)*100)
        else:
            return("DON'T BUY.",((latest_close/recent_low)-1)*100)


        
    decision, change = toBuyOrNotToBuy((float(recent_low)), (float(latest_close)))
    print("-------------------------")
    print(f"SYMBOL: {symbol}")
    print("-------------------------")
    print("REQUESTING STOCK MARKET DATA")
    print(f"REQUEST AT: {formatted_time_now}") #TODO: Program the daytime module
    print("-------------------------")
    print(f"LATEST DAY: {last_refreshed}")
    print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
    print(f"RECENT HIGH: {to_usd(float(recent_high))}")
    print(f"RECENT LOW: {to_usd(float(recent_low))}")
    print("-------------------------")
    print(f"RECOMMENDATION: {decision}")
    print("RECOMMENDATION REASON: The Latest close to recent low change is: {0:,.2f}%".format(change))
    print("Note: anything below 20.00% is a BUY.")
    print("-------------------------")
    print(f"WRITING DATA TO CSV: {csv_file_path}...")
    print("-------------------------")
    print("HAPPY INVESTING!")
    print("-------------------------")

else:
    print("There was an error. Please make sure your ticker symbol is correct.")
