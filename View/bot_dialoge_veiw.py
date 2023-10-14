from tkinter import LabelFrame
from resources.colorpalete import colorPalette


#configure label frames to show within bot_dialoge_veiw
# header 
class bot_dialoge_view_header(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=colorPalette.smoothblack):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
# dialogesettings
class bot_dialoge_view_dialoge_settings(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=colorPalette.lightbrown):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
# dialoge
class bot_dialoge_view_dialoge(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=colorPalette.brown):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
class bot_dialoge_veiw(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg="white"):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        # configure grid 
        self.grid_columnconfigure(0, weight=304)
        self.grid_columnconfigure(1, weight=150)
        self.grid_rowconfigure(0, weight=51)
        self.grid_rowconfigure(1, weight=350)
        # create instance of each view 
        self.header = bot_dialoge_view_header(self, self.controller)
        self.header.configure(border=0,borderwidth=0)
        self.dialoge_settings = bot_dialoge_view_dialoge_settings(self, self.controller)
        self.dialoge_settings.configure(border=0,borderwidth=0)
        self.dialoge = bot_dialoge_view_dialoge(self, self.controller)
        self.dialoge.configure(border=0,borderwidth=0)
        # pack each view in the grid
        self.header.grid(row=0, column=0,columnspan= 3,sticky="nsew", padx=0, pady=0)
        self.dialoge.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        self.dialoge_settings.grid(row=1, column=1, sticky="nsew", padx=0, pady=0)

