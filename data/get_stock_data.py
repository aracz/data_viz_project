import sys

import yfinance as yf
import logging


class GetStockData:
    def __init__(self, symbol, start_date=None, end_date=None, period=None, ):
        self.title = 'Title'
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.period = period
        self.info = None
        self.sustainability = None

    def get_timeframe(self):
        if (self.start_date is None or self.end_date is None) & (self.period is None):
            logging.info('Timeframe parameters are set up incorrectly')
            return sys.exit(0)
        elif self.period is None:
            return self.start_date, self.end_date, None
        else:
            return self.start_date, self.end_date, self.period

    def get_stock_data_between_dates(self, mli=False):
        start_date, end_date, period = self.get_timeframe()
        logging.info(f'Fetching data between {start_date} and {end_date} for symbol {self.symbol}')
        stock_data = yf.download(self.symbol, start=start_date, end=end_date, multi_level_index=mli)
        logging.info(f'Successfully fetched {len(stock_data)} rows')
        return stock_data

    def get_stock_data_period(self):
        start_date, end_date, period = self.get_timeframe()
        logging.info(f'Fetching data for period {period} for symbol {self.symbol}')
        stock_data_period = yf.Ticker(self.symbol).history(period=period)
        logging.info(f'Successfully fetched {len(stock_data_period)} rows')
        return stock_data_period

    def get_stock_info(self, info):
        if self.info is None:  
            logging.info(f'Fetching info for symbol {self.symbol}')
            self.info = yf.Ticker(self.symbol).get_info()
            logging.info(f'Successfully fetched info for {self.symbol}')
        return self.info.get(info, f'Info {info} not available')

    def get_sustainability(self, info):
        if self.sustainability is None:
            logging.info(f'Fetching sustainability data for symbol {self.symbol}')
            self.sustainability = yf.Ticker(self.symbol).get_sustainability()
            logging.info(f'Successfully fetched sustainability data for {self.symbol}')
        return self.sustainability.loc[info]["esgScores"]
    
    def get_holders(self):
        logging.info(f'Fetching holders for symbol {self.symbol}')
        holders = yf.Ticker(self.symbol).get_institutional_holders()
        logging.info(f'Successfully fetched holders for {self.symbol}')
        return holders

