# Stocks and values

stock_prices ={
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

stock= input("Enter a stock name(AAPL,TSLA,GOOGL,MSFT,AMZN):").upper()
total_stocks=int(input("Enter the Quantity of stocks:"))

if stock in stock_prices:
    stock_price = stock_prices[stock]  
    investment = stock_price * total_stocks
    print("each stock price:",stock_price)
    print("Total investment:", investment)
 
else:
    print("Stock not found!")
    