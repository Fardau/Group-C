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

stocks_value = stocks['Time Series (5min)']
df = df.DataFrame(data).T.apply(pd.to_numeric)
df.into()
df.head()

# STEP 2: Purchase function

# User places an order to purchase stock

# Set up a user
print("Welcome to the Investment game. Please choose your user name: ", )

#Functionality 1: Setup user
users = {
        "Kevin" : {
            "balance"   : 1,
            "stocks"    : {"Google": 0, "MSFT": 0 }},
        "Lucie" : {
            "balance"   : 1,
            "stocks"    : {"Google": 0, "MSFT": 0}},
        "Fardau" : {
            "balance"  : 1,
            "stocks"   : {"Google": 0,"MSFT": 0}},
}
def userSetup():
    userx = input("What is your username?")
#   userxpw = input("EnterPW")
    if userx in users:
        print("Welcome","", userx)
        print("Your balance today is: ", users[userx]['balance'])
    else:
        print("Unknown user")
    return
print(userSetup())

#user[Fardau]
#userdata[user]['balance'] += 50
#userdata[user]['stock']['ibm'] = 20

#print(userdata['Fardau'])


def purchase():
    stock_purchase = input("Which stock do you want to buy? ")
    if stock_purchase in stocks['Meta Data']['2. Symbol']:
        print ("Do you want to buy:", stocks['Meta Data']['2. Symbol'],"?")
        num = int(input("How many stocks do you want to buy? "))
        # stock_purchase in users[userSetup()]['stocks']:
        users[userSetup()]['stock'][stock_purchase] += num
        users[userSetup()]['balance'] -= num * stocks_value['4. close'][1]
        # else:
            # users[userSetup()]['stock'][stock_purchase].append(stock_purchase) =+ num
        print("You purchased: ", stock_purchase)
        print("Your new balance is: ", users[userSetup()]['balance'])
    else:
        print('Stock not available', continue_purchase())

#print("What is your next action?", purchase())

#def print_portfolio():
    #for i in range(len(portfolio_user1)):
        #print(i, ":", portfolio_user1[i])

def continue_purchase():
    next_purchase = input("Do you want to buy another stock? ")
    if next_purchase.upper() == 'Y':
        purchase()
    else:
        print('Thank you for playing the Investment game. Your final balance is: ', users[userSetup()]['balance'])
        exit()


# STEP 4: Performance

# TASKS:



