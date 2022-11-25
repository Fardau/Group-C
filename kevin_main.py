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
stocks = response.json()
stocks['Meta Data']

# STEP 2: Purchase function
# User places an order to purchase stock

# Set up a user
print("Welcome to the Investment game. Please choose your user name: ")

print("Your starting balance is: ")


balance_user1 = 10000
portfolio_user1 = {
    "Google": 0,
    "Apple": 0
}

def purchase():
    stock_purchase = input("Which stock do you want to buy? ")
    if stock_purchase in stocks['Meta Data']['2. Symbol']:
        print ("Do you want to buy:", stocks['Meta Data']['2. Symbol'])
        num = int(input("How many do you want to buy? "))
        portfolio_user1[stock_purchase] =+ num
        # balance_user1 -= value * num #change to stock price
        print("You purchased: ", purchase())
        print("Your balance is: ", balance_user1())
    else:
        print('Stock not available', continue_purchase())

print("What is your next action?", purchase())

def print_portfolio():
    for i in range(len(portfolio_user1)):
        print(i, ":", portfolio_user1[i])

def continue_purchase():
    next_purchase = input("Do you want to buy another stock? ")
    if next_purchase.upper() == 'Y':
        purchase()
    else:
        exit()


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


