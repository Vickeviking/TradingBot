
from Model.bought_stock import tradeBotBoughtStock

class tradeBotWallet:
    def __init__(self, settings = None):
        self.start_value = settings.start_balance
        self.bought_stocks = []
        self.money = 0
        self.total_value = 0
        self.settings = settings
    def update(self):
        # bought_stocks doesnt need update, constant values
        pass
        #TODO self.total_value = self.getTotalValue()
    def getTotalValue():
        #TODO need to implement stock first, some get live value from market for each stock x amount of stock
        pass