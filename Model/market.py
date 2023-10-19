
from Model.fetch_data import fetchData
from resources.app_enums import bot_states_enum as bot_states
from Model.stock import stock



class market:
    def __init__(self):
        self.bot_state = bot_states.STOPPED
        self.showStocks = False
        self.live_stocks_model = None # each update of the market will update info in that model
        self.settings = None
        self.stocks = [stock(), stock(), stock(), stock()]
    def update(self):
        if self.bot_state == bot_states.STOPPED.value: #TODO could cause error, double check compatinbility
            return
        self.updateStocks()
    def updateStocktypes(self, stocktypes):
        self.stocks = []
        for stocktype in stocktypes:
            self.stocks.append(stock(stockTicket=stocktype.value))

    def switchState(self, botStateParam):
        if botStateParam == bot_states.STOPPED.value: # switched off
            self.bot_state = bot_states.STOPPED
            self.showStocks = False
        else: # switched on
            self.bot_state = bot_states.RUNNING
            self.showStocks = True
            pass

    def updateStocks(self):
        #TODO update stocks inside the model
        pass