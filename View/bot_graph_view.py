from tkinter import LabelFrame
from resources.colorpalete import colorPalette as cp


class bot_graph_view_header(LabelFrame):
    def __init__(self, master=None, controller=None, text=None, bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0,borderwidth=0)
class bot_graph_view_graph(LabelFrame):
    def __init__(self, master=None, controller=None, text="Graph (remove this text later )", bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0,borderwidth=0)
class bot_graph_view_info(LabelFrame):
    def __init__(self, master=None, controller=None, text=None, bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0,borderwidth=0)

class bot_graph_view_container(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg="white"):
            super().__init__(master, text=text, bg=bg)
            self.master = master
            self.controller = controller
            self.configure(border=0, borderwidth=0)
            self.grid_columnconfigure(0, weight=1)
            self.grid_rowconfigure(0, weight=64)
            self.grid_rowconfigure(1, weight=198)
            self.grid_rowconfigure(2, weight=139)
            #create instance of frame 
            self.header = bot_graph_view_header(self, self.controller)
            self.graph = bot_graph_view_graph(self, self.controller)
            self.info = bot_graph_view_info(self, self.controller)
            # pack each frame in the grid
            self.header.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
            self.graph.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
            self.info.grid(row=2, column=0, sticky="nsew", padx=0, pady=0)

class bot_graph_view_border(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=cp.smoothblack):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)

class bot_graph_view_borderContainer(LabelFrame):
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
        self.border = bot_graph_view_border(self, self.controller)
        #add to grid
        self.border.grid(row=2, column=0, sticky="nsew")

class bot_graph_veiw(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        self.grid_columnconfigure(0, weight=220)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        #create instance of frame 
        self.container = bot_graph_view_container(self, self.controller)
        self.border = bot_graph_view_borderContainer(self, self.controller)
        # pack each frame in the grid
        self.container.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=0, pady=0)
        self.border.grid(row=0, column=1, rowspan=3, sticky="nsew", padx=0, pady=0)

     
    
        
