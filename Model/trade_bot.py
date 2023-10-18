# tradebot.py
from Model.wallet import tradeBotWallet
from Model.marketSignalLogic import marketSignalLogic
from resources.stock_enums import stock_types_enum as stock_types

#mostly a container class

class tradeBot:
    def __init__(self):
        self.settings = None # set by main.py during init , passed as reference by default
        self.market = None # set by main.py during init , passed as reference by default
        self.wallet = tradeBotWallet()
        self.marketSignalLogic = marketSignalLogic(settings=self.settings, market=self.market)
        self.powered = False
    def update(self):
        self.settings.update()
        self.wallet.update()
        self.marketSignalLogic.update()
        
    def lookForPurchase(self):
        if self.marketSignalLogic.buySignalLogic.isSignaling:
            self.initPurchase(self.marketSignalLogic.buySignalLogic.signal.stock)
    def lookForSale(self):
        if self.marketSignalLogic.sellSignalLogic.isSignaling:
            self.initSale(self.marketSignalLogic.sellSignalLogic.signal.stock)

    def initPurchase(self, stock_type):
        #money = self.wallet.getMoney()
        #TODO check if wallet has enough money
        #TODO based on setting % of wallet to spend, calculate how much to spend
        #TODO buy stock, update necessary values
        #TODO turn off flag in marketSignalLogic
        pass
    def initSale(self, stock_type):
        #TODO check if wallet has stock
        #Todo sell stock, update necessary values
        #TODO turn off flag in marketSignalLogic
        pass