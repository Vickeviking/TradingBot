# bot_dialogue_controller.py
from View.bot_graph_view import bot_graph_veiw
from Model.bot_graph_model import bot_graph_model

class bot_graph_controller:
    def __init__(self, master=None):
        self.master = master
        # Create a frame for the label frame
        self.view = bot_graph_veiw(master=self.master, controller=self) 
        self.view.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)  
        #create model
        self.model = bot_graph_model(self)


    def get_label_frame(self):
        return self.view
    
    def update(self):
        self.view.update()