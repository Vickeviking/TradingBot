
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
        self.fetchDataModule = fetchData()
        self.stockViewModel = None
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
        self.stockViewModel.showStocks = self.showStocks
        self.stockViewModel.updateStockPointer(self.stocks)
    
        if not self.showStocks: # if we aint showing stocks, dont update
            return
        if len(self.stocks) == 0:   #if no stocks are selected
            return
        
        if self.stockViewModel is not None:
            for stock in self.stocks:
                newStockPrice = self.fetchDataModule.getStockInfoArray(stock.stockTicket)
                stock.update(newStockPrice)
        
     

