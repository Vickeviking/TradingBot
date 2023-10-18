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

    def get_label_frame(self):
        return self.view
        
    def addMessage(self, message):
        self.model.addMessage(message)
        self.update()
    
    def addMessage(self, stock = None, quantity = None, price = None, totPrice = None, customMessage = None, customMessage_color = None):
        self.model.addMessage(message(stock, quantity, price, totPrice, customMessage, customMessage_color))
        self.update()
    
    def setSettings(self, settings):
        self.model.setSettings(settings)
        self.update()
    
    def setSettings(self, showStock = True, showQuantity = True, showPrice = True, showTotPrice = True):
        self.model.setSettings(settings(showStock, showQuantity, showPrice, showTotPrice))
        self.update()

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


    