from tkinter import LabelFrame

from resources.colorpalete import colorPalette as pc


class live_stock_view_header(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=pc.smoothblack):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        # Add any additional methods or configurations as needed
class live_stock_view_graph(LabelFrame):
    def __init__(self, master=None,controller=None, text="graph delete later", bg=pc.smoothblack):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        # Add any additional methods or configurations as needed
class live_stock_view_info(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=pc.smoothblack):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        # Add any additional methods or configurations as needed

class live_stock_veiw(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg="green"):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border= 0, borderwidth=0)
        #create grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=102)
        self.grid_rowconfigure(1, weight=238)
        self.grid_rowconfigure(2, weight=60)
        #create instances of each view
        self.header = live_stock_view_header(self, self.controller)
        self.graph = live_stock_view_graph(self, self.controller)
        self.info = live_stock_view_info(self, self.controller)
        #pack each view in the grid
        self.header.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.graph.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        self.info.grid(row=2, column=0, sticky="nsew", padx=0, pady=0)

class live_stocks_veiw(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg="green"):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        # configure grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        # create instances of each view
        self.live_stock1 = live_stock_veiw(self, self.controller)
        self.live_stock2 = live_stock_veiw(self, self.controller)
        self.live_stock3 = live_stock_veiw(self, self.controller)
        self.live_stock4 = live_stock_veiw(self, self.controller)
        # pack each view in the grid
        self.live_stock1.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.live_stock2.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.live_stock3.grid(row=0, column=2, sticky="nsew", padx=0, pady=0)
        self.live_stock4.grid(row=0, column=3, sticky="nsew", padx=0, pady=0)

    