# The INVESTMENT game

# Import packages


# Get the data from API

response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=demo")


# Set up a user


# Performance


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


#Functionality 2: Make function
#Functionality 3: Get the data from API
#Functionality 4: Performance


raw_data = response.json()


