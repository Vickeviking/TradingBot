# tradebot.py
from Model.wallet import tradeBotWallet
from Model.marketSignalLogic import marketSignalLogic
from resources.stock_enums import stock_types_enum as stock_types
from resources.app_enums import bot_states_enum as bot_states
import copy

#mostly a container class
class mySettings:
    def __init__(self, stocks = [], buy_rsi_range = [0,100], buy_percentage_dip = 0, buy_derivative_on_switch = False, buy_derivative_steps = 0, buy_quantity_at_atime = 0, sell_profit_exit = 0, sell_loss_exit = 0, sell_derivative_on_switch = False, sell_derivative_steps = 0, start_balance = 100):
        self.stocks = stocks
        #buy signals 
        self.buy_rsi_range = buy_rsi_range
        self.buy_percentage_dip = buy_percentage_dip
        self.buy_derivative_on_switch = buy_derivative_on_switch
        self.buy_derivative_steps = buy_derivative_steps
        self.buy_quantity_at_atime = buy_quantity_at_atime
        #sell signals
        self.sell_profit_exit = sell_profit_exit
        self.sell_loss_exit = sell_loss_exit
        self.sell_derivative_on_switch = sell_derivative_on_switch
        self.sell_derivative_steps = sell_derivative_steps
        #start balance
        self.start_balance = start_balance

class tradeBot:
    def __init__(self):
        self.implementedSettings = mySettings()
        self.market = None # set by main.py during init , passed as reference by default
        self.wallet = tradeBotWallet(settings=self.implementedSettings)
        self.marketSignalLogic = marketSignalLogic(settings=self.implementedSettings, market=self.market)
        self.state = bot_states.STOPPED


    def update(self):
        if (self.state == bot_states.STOPPED): #less demanding when off? 
            return
        self.wallet.update()
        self.marketSignalLogic.update()

    def switchState(self, botsStateParam):
        if botsStateParam.value == bot_states.STOPPED.value:
            self.state = bot_states.STOPPED
            self.marketSignalLogic.switchState(bot_states.STOPPED)

        else:   #switched on

            self.marketSignalLogic.updateSettings(self.implementedSettings)
            self.wallet.updateSettings(self.implementedSettings)
            self.state = bot_states.RUNNING
            self.marketSignalLogic.switchState(bot_states.RUNNING)

    
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

    # getter and setters

    def setMarket(self, market):
        self.market = market
        self.marketSignalLogic.setMarket(market)