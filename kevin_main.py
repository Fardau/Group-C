print("hello")
print("this is a test #2")

abc(1)
print("testtt")

def abc(a):
    return a+1

#Functionality 1: Setup user
#Functionality 2: Make function
#Functionality 3: Get the data from API
#Functionality 4: Performance




response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=demo")
