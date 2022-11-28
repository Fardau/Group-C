# The INVESTMENT game

# Import packages
import requests
import pandas as pd

# Welcome screen:
print("Welcome to the Investment game. Please choose your user name: ", )

# Users database:
users = {
        'Kevin': {
            "user_name" : "Kevin",
            "balance"   : 1000,
            "stocks"    : {"Google": 0, "MSFT": 0 }},
        'Lucie': {
            "user_name": "Lucie",
            "balance"   : 900,
            "stocks"    : {"Google": 0, "MSFT": 0}},
        'Fardau': {
            "user_name": "Fardau",
            "balance"  : 5000,
            "stocks"   : {"Google": 0,"MSFT": 0}},
}


# STEP 1: Define the main functions
# Functionality 1: Setup a user
def user_setup():
    while True:
        userx = input("What is your username?")
    #   userxpw = input("EnterPW")
        if userx in users:
            print("Welcome ", users[userx]['user_name'],'!')
            print("Your balance today is: ", users[userx]['balance'])
            return userx
        else:
            print("Unknown user")
            # Future functionality: pick another user or end the game


current_user = user_setup()


# Functionality 2: Stock purchase
def purchase():
    stock_purchase = input("Which stock do you want to buy? ")
    # STEP 1: Get the data from API
    response = requests.get(
        "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + stock_purchase + "&interval=5min&outputsize=full&apikey=D19M5YGAB9KUZ8V1")
    stocks = response.json()
    stocks_value = stocks['Time Series (5min)']
    df = pd.DataFrame(stocks_value).T.apply(pd.to_numeric)

    print("Do you want to buy:", stock_purchase, "?")
    num = int(input("How many stocks do you want to buy?"))
    # Conditions:
    if stock_purchase in users[current_user]['stocks']:
        # stock_purchase in users[userSetup()]['stocks']:
        users[current_user]['stocks'][stock_purchase] += num
        users[current_user]['balance'] -= num * df['4. close'][1]
    elif stock_purchase in stocks['Meta Data']['2. Symbol']:
        users[current_user]['stocks'][stock_purchase] = 0
        users[current_user]['stocks'][stock_purchase] += num
        users[current_user]['balance'] -= num * df['4. close'][1]
        print("You purchased: ", stock_purchase)
        print("Your new balance is: ", users[current_user]['balance'])
        print() # -->> Future functionality: show current holdings
    else:
       print('Stock not available')


# Functionality 3: Stock sell
def sell():
    stock_sell = input("Which stock do you want to sell? ")
    # STEP 1: Get the data from API
    response = requests.get(
        "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + stock_sell + "&interval=5min&outputsize=full&apikey=D19M5YGAB9KUZ8V1")
    stocks = response.json()
    stocks_value = stocks['Time Series (5min)']
    df = pd.DataFrame(stocks_value).T.apply(pd.to_numeric)

    # Step 2: Conditions
    if stock_sell in users[current_user]['stocks']:
        print ("Do you want to sell:", stock_sell,"?")
        num_sell = int(input("How many stocks do you want to sell? "))
        # stock_purchase in users[userSetup()]['stocks']:
        users[current_user]['stocks'][stock_sell] -= num_sell
        users[current_user]['balance'] += num_sell * df['4. close'][1]
        print("You sold: ", stock_sell, "in quantity of ", num_sell, "and sell price of ", df['4. close'][1],".")
        print("Your new balance is: ", users[current_user]['balance'])
    else:
        print('Stock not available')


# Functionality 4: Exit the game
def exit():
    print('Thank you ',current_user, ' for playing the Investment game. Your final balance is: ', users[current_user]['balance'])


# Functionality 5: Game menu
while True:
    choice = input("What do you want to do? (press P for purchase, press S for sale, press E to end the game)")
    if choice.upper() == "P":
        purchase()
    elif choice.upper() == "S":
        sell()
    elif choice.upper() == "E":
        exit()
        break




