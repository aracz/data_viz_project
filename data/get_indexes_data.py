import yfinance as yf
import logging


# S&P 500: ^GSPC
# Dow Jones Industrial Average: ^DJI
# NASDAQ Composite: ^IXIC

class GetIndexesData:

    def __init__(self, start_date, end_date, indexes):
        self.title = 'Title'
        self.start_date = start_date
        self.end_date = end_date
        self.index_list = indexes

    def get_index_data(self):
        indexes = self.index_list
        logging.info(f'Fetching data for {indexes}')
        index_data = yf.download(indexes, start=self.start_date, end=self.end_date)
        logging.info(f'Successfully fetched {len(indexes)} rows')
        return index_data
