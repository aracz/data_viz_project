import yfinance as yf
import logging


class GetIndustryData:

    def __init__(self, ticker):
        self.title = 'Title'
        self.ticker = ticker

    def get_industry_data(self):
        ticker_symbol = self.ticker
        logging.info(f'Fetching industry data for ticker {self.ticker}')
        industry = yf.Ticker(ticker_symbol).info.get('industry', 'Industry information not available')
        logging.info(f'Successfully fetched {len(industry)} rows')
        return industry
