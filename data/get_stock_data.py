import yfinance as yf

# Define the stock symbol (e.g., Apple)
stock_symbol = 'AAPL'

# Download stock data for a specified period
start_date = '2023-01-01'
end_date = '2024-01-01'
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Another way to get stock data for a period of time
stock_data_1y = yf.Ticker(stock_symbol).history(period="1y")


