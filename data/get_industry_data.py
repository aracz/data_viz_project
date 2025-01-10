import yfinance as yf

# Define the stock symbol
ticker_symbol = 'GE'  # Example: General Electric

# Get the industry information
industry = yf.Ticker(ticker_symbol).info.get('industry', 'Industry information not available')
