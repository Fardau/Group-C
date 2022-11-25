# The INVESTMENT game

# Import packages
import requests
import pandas as pd

# STEP 1: Get the data from API
response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=demo")

# Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
if response.status_code != 200:
    raise ValueError("Could not retrieve data, code:", response.status_code)

# The service sends JSON data, we parse that into a Python datastructure
raw_data = response.json()
raw_data['Meta Data']

# STEP 2: Purchase function
# User places an order to purchase stock
# Function
def print_portfolio():
    for i in range(len(stocks)):
        print(i, ":", stocks[i])

portfolio_user1 = {
    "Google": 0,
    "Apple": 0
}


def purchase():
    stock_purchase = input("Which stock do you want to buy? ")
    if stock_purchase in stocks:
        stock_price = stocks[stock_purchase]['value']
        portfolio_user1.append(stock_price)
        print(portfolio_user1)
    else:
        print('Stock not available')

balance = 10000
stock_purchase = input("Which stock do you want to buy? ")
    if stock_purchase in stocks:
        print ("the price is", stock[stock_purchase]['value'])
        num = int(input("How many do you want to buy? "))
        portfolio[stock_purchase] =+ num
        balance -= value * num
        print(portfolio_user1)
    else:
        print('Stock not available')

next_purchase = input("Do you want to buy another stock? ")
if next_purchase.upper() == 'N':
    exit()

# Set up a user


# STEP 4: Performance

# TASKS:
#Functionality 1: Setup user


Users = [
        {"username" : "Kevin",
        "balance"   : 1,
        "stocks"    : []},
        {"username" : "Lucie",
        "balance"   : 1,
        "stocks"    : []},
        {"username" : "Fardau",
         "balance"  : 1,
         "stocks"   : []},
]
def userSetup():
    userx = input("EnterUsername")
#    userxpw = input("EnterPW")
    if userx is userx:
        print("Welcome","", userx)
        #print("Your balance today is", Users(balance)) # To ask RJ
    else:
        print("unknown user")
    return
print(userSetup())


