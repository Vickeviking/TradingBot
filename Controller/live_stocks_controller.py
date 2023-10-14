# bot_dialogue_controller.py
from View.live_stocks_view import live_stocks_veiw
from Model.live_stocks_model import live_stocks_model

class live_stocks_controller:
    def __init__(self, master=None):
        self.master = master
        # Create a frame for the label frame
        self.label_frame = live_stocks_veiw(master) 
        self.label_frame.grid(row=0, column=0, sticky="nsew")  
        #create model
        self.model = live_stocks_model(self)


    def get_label_frame(self):
        return self.label_frame