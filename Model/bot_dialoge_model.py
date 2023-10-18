# bot_dialoge_model.py

class settings:
    def __init__(self, showStock = True, showQuantity = True, showPrice = True, showTotPrice = True):
        self.showStock = showStock
        self.showQuantity = showQuantity
        self.showPrice = showPrice
        self.showTotPrice = showTotPrice

class message:
    def __init__(self,model_parent = None,  stock = None, quantity = None, price = None, totPrice = None, customMessage = None, customMessage_color = None, bought = True):
        self.stock = stock
        self.quantity = quantity
        self.price = price
        self.totPrice = totPrice
        self.customMessage = customMessage
        self.customMessage_color = customMessage_color
        self.model_parent = model_parent
        self.bought = bought
        self.message_string = ""
        self.update_message_string()
    def update_message_string(self):
        if self.customMessage != None:
            self.message_string = self.customMessage
            return
        else:
            message_settings = self.model_parent.getSettings()
            self.message_string = ""
            if self.bought:
                self.message_string += "Bought "
            else:
                self.message_string += "Sold "
            if message_settings.showQuantity != False :
                self.message_string += " " + self.quantity + "x "
            if message_settings.showStock != False:
                self.message_string += self.stock + " "
            if message_settings.showPrice != False:
                self.message_string += "| Value: " + self.price + "$ "
            if message_settings.showTotPrice != False:
                self.message_string += "| Tot: " + self.totPrice + "$ "
    def get_message_string(self):
        self.update_message_string() # update before returning
        return self.message_string
    def get_is_custom_message(self):
        return self.customMessage != None
    def set_parent(self, parent):
        self.pamodel_parentrent = parent
        
    
class bot_dialoge_model:
    def __init__(self, controller=None):
        self.controller = controller
        self.settings = settings()
        self.dialoge = []
        self.nmbrOfMessages_lastUpdate = 0

    def setSettings(self, settings):
        self.settings = settings
    def setSettings(self, showStock = True, showQuantity = True, showPrice = True, showTotPrice = True):
        self.settings = settings(showStock, showQuantity, showPrice, showTotPrice)
    def getSettings(self):
        return self.settings
    def addMessage(self, paramMessage):
        # check that message is of type message
        if type(paramMessage) != message:
            raise TypeError("paramMessage must be of type message")
        self.dialoge.append(paramMessage)
    def getDialoge(self):
        return self.dialoge
