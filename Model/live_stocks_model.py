#live_stocks_model.py
from Model.stock import stock
from resources.stock_enums import stock_tickets

class live_stocks_model:
    def __init__(self, controller=None):
        self.controller = controller
        self.stocks = [stock(), stock(), stock(), stock()]
    def setStocks(self, stockTypes): # called during settings 
        for i in range(len(stockTypes)):
            self.stocks[i].setStockTicket(stockTypes[i])
        
    

