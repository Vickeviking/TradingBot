# bot_dialogue_controller.py
from View.bot_settings_view import bot_settings_veiw

class bot_settings_controller:
    def __init__(self, master=None):
        self.master = master
        # Create a frame for the label frame
        self.label_frame = bot_settings_veiw(master) 
        self.label_frame.grid(row=0, column=0, sticky="nsew")  
        #todo add model to controller


    def get_label_frame(self):
        return self.label_frame