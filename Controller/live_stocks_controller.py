# bot_dialogue_controller.py
from View.live_stocks_view import live_stocks_veiw
from Model.live_stocks_model import live_stocks_model

class live_stocks_controller:
    def __init__(self, master=None):
        self.master = master
        self.market = None
        # Create a frame for the label frame
        self.view = live_stocks_veiw(master=self.master, controller=self) 
        self.view.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)  
        #create model
        self.model = live_stocks_model(self)

    def get_label_frame(self):
        return self.view
    
    def setMarket(self, market):
        self.market = market
        self.view.market = market

    def update(self):
        self.view.update()