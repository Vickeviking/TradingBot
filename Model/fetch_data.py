import yahoo_fin.stock_info as yf
from resources.stock_enums import stock_tickets as st
import time

class fetchData:
    def __init__(self):
        self.last_execution_time = 0

    def getStockInfoArray(self, ticket):
        # Calculate the time elapsed since the last execution
            stockData = yf.get_live_price(ticker=ticket[0])
            return stockData
