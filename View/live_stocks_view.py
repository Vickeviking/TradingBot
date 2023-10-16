from tkinter import LabelFrame
import tkinter as tk
import tkinter.font as tkFont
import matplotlib.pyplot as plt
import matplotlib as mp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from resources.colorpalete import colorPalette as cp
class live_stock_view_header(LabelFrame):
    def __init__(self, master=None, controller=None, text=None, bg=cp.smoothblack):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        self.roboto22 = tkFont.Font(family="Roboto", size=22, weight="normal")
        
        # Create a Frame to center the labels
        center_frame = tk.Frame(self, bg=cp.smoothblack, height=4)
        center_frame.pack(expand=True, fill=tk.BOTH)
        #create padding for the frame
        center_frame.grid_rowconfigure(0, weight=1)
        center_frame.grid_columnconfigure(0, weight=1)
        center_frame.grid_columnconfigure(1, weight=6)
        center_frame.grid_columnconfigure(2, weight=2)
        center_frame.grid_columnconfigure(3, weight=1)
        # Create a label for the stock name (Ticket)
        stock_name_label = tk.Label(center_frame, text="Apple(AAPL) ", font=self.roboto22, fg="white", bg=cp.smoothblack, height=3)
        stock_name_label.grid(row=0, column=1, sticky="e")
        # Create a label for the percentage
        percentage_label = tk.Label(center_frame, text="+0.2%", font=self.roboto22, fg="green", bg=cp.smoothblack, height=3)
        percentage_label.grid(row=0, column=2, sticky="w")

class LiveStockView(LabelFrame):
    def __init__(self, master=None, controller=None, text=None, bg="blue"):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        # create stock graph
        self.graph_width = 0.8
        self.graph_height = 1.8
        
        self.fig_graph, self.ax_graph = plt.subplots(figsize=(self.graph_width, self.graph_height))
        self.ax_graph.set_facecolor("white")
        self.ax_graph.set_title("")
        self.ax_graph.set_xlabel("")
        self.ax_graph.set_ylabel("")
        self.fig_graph.subplots_adjust(left=0.26, right=0.98, bottom=0.12, top=0.95)
        self.fig_graph.patch.set_facecolor(cp.smoothblack)
        self.ax_graph.tick_params(axis="x", colors="white")
        self.ax_graph.tick_params(axis="y", colors="white")

        #plot 5 numbers 
        self.ax_graph.plot([1,2,3,4,5], [204,205,206,204,205])
        self.ax_graph.xaxis.set_major_formatter(mp.ticker.NullFormatter())
        self.canvas_graph = FigureCanvasTkAgg(self.fig_graph, master=self)
    

        # Configure pack
        self.header = live_stock_view_header(self, self.controller)
        self.graph = self.canvas_graph.get_tk_widget()
        
        # Place the frame to control its maximum height
        self.header.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
        self.graph.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
        

class live_stocks_veiw(LabelFrame):
    def __init__(self, master=None, controller=None, text=None, bg="green"):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        self.pack_propagate(0)
        
        self.live_stocks = []

        for _ in range(4):
            live_stock = LiveStockView(self, self.controller)
            live_stock.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            self.live_stocks.append(live_stock)
