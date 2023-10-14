# bot_dialogue_controller.py
from View.bot_settings_view import bot_settings_veiw
from Model.bot_settings_model import bot_settings_model

class bot_settings_controller:
    def __init__(self, master=None):
        self.master = master
        # Create a frame for the label frame
        self.label_frame = bot_settings_veiw(master) 
        self.label_frame.grid(row=0, column=0, sticky="nsew")  
        #create model
        self.model = bot_settings_model(self)


    def get_label_frame(self):
        return self.label_frame