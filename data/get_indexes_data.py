import yfinance as yf

# S&P 500: ^GSPC
# Dow Jones Industrial Average: ^DJI
# NASDAQ Composite: ^IXIC

# Define index symbols
indexes = ['^GSPC', '^DJI', '^IXIC']

# Download historical data for the indexes
start_date = '2023-01-01'
end_date = '2024-01-01'

index_data = yf.download(indexes, start=start_date, end=end_date)