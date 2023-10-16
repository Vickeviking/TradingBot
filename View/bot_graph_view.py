from tkinter import LabelFrame
import tkinter as tk
import tkinter.font as tkFont
from resources.colorpalete import colorPalette as cp
import matplotlib.pyplot as plt
import matplotlib as mp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class bot_graph_view_header(LabelFrame):
    def __init__(self, master=None, controller=None, text=None, bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0,borderwidth=0)
        self.roboto22 = tkFont.Font(family="Roboto", size=22, weight="normal")
        # Create a label 
        self.stock_name_label = tk.Label(self, text="Bot Liquidation Graph ", font=self.roboto22, fg="white", bg=cp.clayred, height=3)
        self.stock_name_label.pack(anchor="center", fill="both", expand=True)

class bot_graph_view_graph(LabelFrame):
    def __init__(self, master=None, controller=None, text=None, bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0,borderwidth=0)
        #create stock graph
        self.graph_width = 2
        self.graph_height = 2
        
        self.fig_graph, self.ax_graph = plt.subplots(figsize=(self.graph_width, self.graph_height))
        self.ax_graph.set_facecolor("white")
        self.ax_graph.set_title("")
        self.ax_graph.set_xlabel("")
        self.ax_graph.set_ylabel("")
        self.fig_graph.subplots_adjust(left=0.27, right=0.98, bottom=0.12, top=0.95)
        self.fig_graph.patch.set_facecolor(cp.clayred)
        self.ax_graph.tick_params(axis="x", colors="white")
        self.ax_graph.tick_params(axis="y", colors="white")

        #plot 5 numbers 
        self.ax_graph.plot([1,2,3,4,5], [0.1,0.12,0.13,0.11,0.14])
        self.ax_graph.xaxis.set_major_formatter(mp.ticker.NullFormatter())
        self.canvas_graph = FigureCanvasTkAgg(self.fig_graph, master=self)
        self.canvas_graph.get_tk_widget().pack()
class bot_graph_view_info(LabelFrame):
    def __init__(self, master=None, controller=None, text=None, bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0,borderwidth=0)

class bot_graph_view_container(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=cp.smoothblack):
            super().__init__(master, text=text, bg=bg)
            self.master = master
            self.controller = controller
            self.configure(border=0, borderwidth=0)
            self.grid_columnconfigure(0, weight=1)
            self.grid_rowconfigure(0, weight=64)
            self.grid_rowconfigure(1, weight=198)
            self.grid_rowconfigure(2, weight=139)
            self.pack_propagate(0)
            #create instance of frame 
            self.header = bot_graph_view_header(self, self.controller)
            self.graph = bot_graph_view_graph(self, self.controller)
            self.graph.pack_propagate(0)
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
        self.pack_propagate(0)
        #create instance of frame 
        self.container = bot_graph_view_container(self, self.controller)
        self.border = bot_graph_view_borderContainer(self, self.controller)
        # pack each frame in the grid
        self.container.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=0, pady=0)
        self.border.grid(row=0, column=1, rowspan=3, sticky="nsew", padx=0, pady=0)

     
    
        
