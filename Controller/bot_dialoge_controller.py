# bot_dialogue_controller.py
from View.bot_dialoge_veiw import bot_dialoge_veiw
from Model.bot_dialoge_model import *

class bot_dialoge_controller:
    def __init__(self, master=None):
        self.master = master
        # Create a frame for the label frame
        self.view = bot_dialoge_veiw(master=self.master, controller=self) 
        self.view.grid(row=0, column=0, sticky="nsew")  
        #create model
        self.model = bot_dialoge_model(self) 
        self.convoCleared = False

    def get_label_frame(self):
        return self.view
        
    def addMessage(self, message):
        self.model.addMessage(message)
        self.update()
    
    def addMessage(self, stock = None, quantity = None, price = None, totPrice = None, customMessage = None, customMessage_color = None):
        self.model.addMessage(message(stock, quantity, price, totPrice, customMessage, customMessage_color))

    def clearConvo(self):
        self.model.dialoge = []
        self.setNmbrOfMessages_lastUpdate(0)
        self.convoCleared = True

    def showStockClicked(self):
        self.model.settings.showStock = not self.model.settings.showStock
        self.update()
    
    def showQuantityClicked(self):
        self.model.settings.showQuantity = not self.model.settings.showQuantity
        self.update()
    
    def showPriceClicked(self):
        self.model.settings.showPrice = not self.model.settings.showPrice
        self.update()

    def showTotPriceClicked(self):
        self.model.settings.showTotPrice = not self.model.settings.showTotPrice
        self.update()
    
    def setSettings(self, settings):
        self.model.setSettings(settings)
    
    def setSettings(self, showStock = True, showQuantity = True, showPrice = True, showTotPrice = True):
        self.model.setSettings(settings(showStock, showQuantity, showPrice, showTotPrice))

    def getSettings(self):
        return self.model.getSettings()
    
    def getDialoge(self):
        return self.model.getDialoge()
    
    def getNmbrOfMessages_lastUpdate(self):
        return self.model.nmbrOfMessages_lastUpdate 
    
    def setNmbrOfMessages_lastUpdate(self, nmbrOfMessages_lastUpdate):
        self.model.nmbrOfMessages_lastUpdate = nmbrOfMessages_lastUpdate

    def update(self):
        self.view.update()


    