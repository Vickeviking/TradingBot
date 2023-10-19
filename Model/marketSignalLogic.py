from resources.stock_enums import stock_types_enum as stock_types
from resources.app_enums import bot_states_enum as bot_states

class signal:
    def __init__(self, isSignaling = False, stock = None):
        self.isSignaling = isSignaling
        self.stock = stock

# -------- Buy Signal Logic -------- #

class buyRSISignalLogic:
    def __init__(self, market, settings):
        self.market = market
        self.settings = settings
        self.signal = signal()
        self.isSignaling = False
    def update(self):
        #TODO
        pass

class buyPercentageDipSignalLogic:
    def __init__(self, market, settings):
        self.market = market
        self.settings = settings
        self.signal = signal()
        self.isSignaling = False
    def update(self):
        #TODO
        pass

class buyDerivativeSignalLogic:
    def __init__(self, market, settings):
        self.market = market
        self.settings = settings
        self.signal = signal()
        self.isSignaling = False
    def update(self):
        #TODO
        pass

class buySignalLogic:
    def __init__(self, market, settings):
        self.market = market
        self.settings = settings
        self.rsiSignalLogic = buyRSISignalLogic(market, settings)
        self.percentageDipSignalLogic = buyPercentageDipSignalLogic(market, settings)
        self.derivativeSignalLogic = buyDerivativeSignalLogic(market, settings)
        self.signal = signal()
        self.isSignaling = False
    def update(self):
        self.rsiSignalLogic.update()
        self.percentageDipSignalLogic.update()
        self.derivativeSignalLogic.update()
    def checkForBuySignal(self):
        if self.rsiSignalLogic.isSignaling:
            self.isSignaling = True
            self.signal = self.rsiSignalLogic.signal
            return True
        elif self.percentageDipSignalLogic.isSignaling:
            self.isSignaling = True
            self.signal = self.percentageDipSignalLogic.signal
            return True
        elif self.derivativeSignalLogic.isSignaling:
            self.isSignaling = True
            self.signal = self.derivativeSignalLogic.signal
            return True
        else:
            return False



# -------- Sell Signal Logic -------- #

class profitPercentageSignalLogic:
    def __init__(self, market, settings):
        self.market = market
        self.settings = settings
        self.signal = False
    def update(self):
        #TODO
        pass

class exitPercentageSignalLogic:
    def __init__(self, market, settings):
        self.market = market
        self.settings = settings
        self.signal = False
    def update(self):
        #TODO
        pass

class sellDerivativeSignalLogic:
    def __init__(self, market, settings):
        self.market = market
        self.settings = settings
        self.signal = False
    def update(self):
        #TODO
        pass

class sellSignalLogic:
    def __init__(self, market, settings):
        self.market = market
        self.settings = settings
        self.profitPercentageSignalLogic = profitPercentageSignalLogic(market, settings)
        self.exitPercentageSignalLogic = exitPercentageSignalLogic(market, settings)
        self.derivativeSignalLogic = sellDerivativeSignalLogic(market, settings)
        self.signal = signal()
        self.isSignaling = False
    def update(self):
        self.profitPercentageSignalLogic.update()
        self.exitPercentageSignalLogic.update()
        self.derivativeSignalLogic.update()
    def checkForSellSignal(self):
        if self.profitPercentageSignalLogic.isSignaling:
            self.isSignaling = True
            self.signal = self.profitPercentageSignalLogic.signal
            return True
        elif self.exitPercentageSignalLogic.isSignaling:
            self.isSignaling = True
            self.signal = self.exitPercentageSignalLogic.signal
            return True
        elif self.derivativeSignalLogic.isSignaling:
            self.isSignaling = True
            self.signal = self.derivativeSignalLogic.signal
            return True
        else:
            return False


# -------- Market Signal Logic -------- #

class marketSignalLogic:
    def __init__(self, market, settings):
        self.buySignalLogic = buySignalLogic(market, settings)
        self.sellSignalLogic = sellSignalLogic(market, settings)
        self.signal = signal()
        self.isSignaling = False
        self.state = bot_states.STOPPED
        self.settings = settings
    def checkForBuySignal(self):
        if self.buySignalLogic.isSignaling:
            self.signal = self.buySignalLogic.signal
            self.isSignaling = True
            return True
    def checkForSellSignal(self):
        if self.sellSignalLogic.isSignaling:
            self.signal = self.sellSignalLogic.signal
            self.isSignaling = True
            return True
    def resetSignal(self):
        self.signal = signal()
        self.isSignaling = False
        self.buySignalLogic.isSignaling = False
        self.buySignalLogic.signal = signal()
        self.sellSignalLogic.isSignaling = False
        self.sellSignalLogic.signal = signal()
    def switchState(self, botsStateParam):
        if botsStateParam.value == bot_states.STOPPED.value: # switched off
            self.state = bot_states.STOPPED
            self.buySignalLogic.isSignaling = False
            self.sellSignalLogic.isSignaling = False
            self.resetSignal()
        else: #switched on
            self.state = bot_states.RUNNING
            self.buySignalLogic.isSignaling = False
            self.sellSignalLogic.isSignaling = False
            self.resetSignal()


    def update(self):
        if (self.state == bot_states.STOPPED.value): #TODO can cause errors check compatability with rest
            return
        self.buySignalLogic.update()
        self.sellSignalLogic.update()
        self.checkForBuySignal()
        self.checkForSellSignal()
