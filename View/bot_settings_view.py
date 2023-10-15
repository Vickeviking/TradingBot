from tkinter import LabelFrame
from resources.colorpalete import colorPalette as cp

class bot_settings_view_header(LabelFrame):
    def __init__(self, master=None,controller=None, text="header", bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)

class bot_settings_view_settings_panel_left(LabelFrame):
    def __init__(self, master=None,controller=None, text="Left", bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)


class bot_settings_view_settings_panel_border(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=cp.smoothblack):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)

class bot_settings_view_settings_panel_borderContainer(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=10)
        self.grid_rowconfigure(3, weight=1)
        #create border instance
        self.border = bot_settings_view_settings_panel_border(self, self.controller)
        #add to grid
        self.border.grid(row=2, column=0, sticky="nsew")


class bot_settings_view_settings_panel_right(LabelFrame):
    def __init__(self, master=None,controller=None, text="Right", bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
class bot_settings_view_settings_panel(LabelFrame):
    def __init__(self, master=None,controller=None, text="panel", bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        self.grid_columnconfigure(0, weight=237)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=289)
        self.grid_rowconfigure(0, weight=1)
        # create class instance
        self.left = bot_settings_view_settings_panel_left(self, self.controller)
        self.borderContainer = bot_settings_view_settings_panel_borderContainer(self, self.controller)
        self.right = bot_settings_view_settings_panel_right(self, self.controller)
        # add to grid
        self.left.grid(row=0, column=0, sticky="nsew")
        self.borderContainer.grid(row=0, column=1, sticky="nsew")
        self.right.grid(row=0, column=2, sticky="nsew")
class border(LabelFrame):
    def __init__(self, master = None, text = None, bg = cp.smoothblack):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.configure(border=0, borderwidth=0)

        #32, 251, 117
class bot_settings_view_finalize(LabelFrame):
    def __init__(self, master=None,controller=None, text="finalize", bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)


class bot_settings_veiw(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border= 0, borderwidth=0)
        # setup grid 
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=20)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=32)
        self.grid_rowconfigure(1, weight=251)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=117)
        #create class instance 
        self.header = bot_settings_view_header(self, self.controller)
        self.settings_panel = bot_settings_view_settings_panel(self, self.controller)
        self.border = border(self)
        self.finalize = bot_settings_view_finalize(self, self.controller)
        # add to grid
        self.header.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.settings_panel.grid(row=1, column=0, columnspan=3, sticky="nsew")
        self.border.grid(row=2, column=1, sticky="nsew")
        self.finalize.grid(row=3, column=0, columnspan=3, sticky="nsew")
    






    