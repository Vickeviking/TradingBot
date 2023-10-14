# bot_dialogue_controller.py
from View.bot_dialoge_veiw import bot_dialoge_veiw
from Model.bot_dialoge_model import bot_dialoge_model

class bot_dialoge_controller:
    def __init__(self, master=None):
        self.master = master
        # Create a frame for the label frame
        self.label_frame = bot_dialoge_veiw(master) 
        self.label_frame.grid(row=0, column=0, sticky="nsew")  
        #create model
        self.model = bot_dialoge_model(self) 
        

    def get_label_frame(self):
        return self.label_frame
        
    