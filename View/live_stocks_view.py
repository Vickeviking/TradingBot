from tkinter import LabelFrame
import tkinter as tk
import tkinter.font as tkFont
import matplotlib.pyplot as plt
import matplotlib as mp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from resources.colorpalete import colorPalette as cp
from resources.app_enums import bot_states_enum as bot_states
class live_stock_view_header(LabelFrame):
    def __init__(self, master=None, controller=None, text=None, bg=cp.smoothblack):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        self.roboto22 = tkFont.Font(family="Roboto", size=22, weight="normal")
        
        # Create a Frame to center the labels
        self.center_frame = tk.Frame(self, bg=cp.smoothblack, height=4)
        self.center_frame.pack(expand=True, fill=tk.BOTH)
        #create padding for the frame
        self.center_frame.grid_rowconfigure(0, weight=1)
        self.center_frame.grid_columnconfigure(0, weight=1)
        self.center_frame.grid_columnconfigure(1, weight=6)
        self.center_frame.grid_columnconfigure(2, weight=2)
        self.center_frame.grid_columnconfigure(3, weight=1)
        # Create a label for the stock name (Ticket)
        self.stock_name_label = tk.Label(self.center_frame, text="Apple(AAPL) ", font=self.roboto22, fg="white", bg=cp.smoothblack, height=3)
        self.stock_name_label.grid(row=0, column=1, sticky="e")
        # Create a label for the value
        self.value_label = tk.Label(self.center_frame, text="$204.00", font=self.roboto22, fg="white", bg=cp.smoothblack, height=3)
        self.value_label.grid(row=0, column=3, sticky="w")
        # Create a label for the percentage
        self.percentage_label = tk.Label(self.center_frame, text="+0.2%", font=self.roboto22, fg="green", bg=cp.smoothblack, height=3)
        self.percentage_label.grid(row=0, column=2, sticky="w")

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
    def updateLive(self, dataArray, stockName, stockPercentage, stockPrice):
        self.ax_graph.clear()
        xPlots = []
        for i in range(len(dataArray)):
            xPlots.append(i)
        self.header.stock_name_label.configure(text=stockName)
        self.header.percentage_label.configure(text=stockPercentage)
        self.header.value_label.configure(text=str(round(stockPrice,2)))
        self.ax_graph.clear()
        self.ax_graph.plot(xPlots, dataArray)
        self.canvas_graph.draw()
    def clearPlot(self):
        self.ax_graph.clear()
        self.header.stock_name_label.configure(text="Choose a Stock")
        self.header.percentage_label.configure(text="")
        self.header.value_label.configure(text="")
        self.canvas_graph.draw()

class live_stocks_veiw(LabelFrame):
    def __init__(self, master=None, controller=None, text=None, bg="green"):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.bot_state = None
        self.configure(border=0, borderwidth=0)
        self.pack_propagate(0)
        
        self.live_stocks = []

        for _ in range(4):
            live_stock = LiveStockView(self, self.controller)
            live_stock.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            self.live_stocks.append(live_stock)

    def update(self):
        # If not showing stocks, clear the plot for all LiveStockView instances
            if self.bot_state == bot_states.STOPPED or not self.controller.model.showStocks:
                for live_stock in self.live_stocks:
                    live_stock.clearPlot()
                return
            elif self.controller.model.showStocks:
                itteratorStock = 0
                for live_stock in self.live_stocks:
                    if itteratorStock < len(self.controller.model.stocks):
                        if self.controller.model.showStocks:
                            live_stock.updateLive(self.controller.model.stocks[itteratorStock].last10StockValues,self.controller.model.stocks[itteratorStock].stockName ,self.controller.model.stocks[itteratorStock].stockValueChangePercentage, self.controller.model.stocks[itteratorStock].stockValue)
                    itteratorStock += 1

        
    def switchState(self, botStateParam):
        if botStateParam == bot_states.STOPPED:
            self.bot_state = bot_states.STOPPED
            self.showStocks = False
        else:
            self.bot_state = bot_states.RUNNING
            self.showStocks = True