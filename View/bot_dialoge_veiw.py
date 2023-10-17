from tkinter import LabelFrame
import tkinter as tk
import tkinter.font as tkFont
from tkinter import Label

from resources.colorpalete import colorPalette


#configure label frames to show within bot_dialoge_veiw
# header 
class bot_dialoge_view_header(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=colorPalette.smoothblack):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.pack_propagate(0)
        self.roboto22 = tkFont.Font(family="Roboto", size=22, weight="normal")
        self.roboto16 = tkFont.Font(family="Roboto", size=16, weight="normal")
        # pack "bot dialoge" label  and "Dialoge settings next to each other"
        self.header1 = Label(self, text="Bot Dialoge", bg=colorPalette.smoothblack, fg="white", font=self.roboto22)
        self.header1.pack(side="left", fill="both", expand=True, padx=70)
        self.header2 = Label(self, text="Dialoge Settings", bg=colorPalette.smoothblack, fg="white", font=self.roboto16)
        self.header2.pack(side="left", fill="both", expand=True)
# dialogesettings
class bot_dialoge_view_dialoge_settings(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=colorPalette.lightbrown):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.pack_propagate(0)
        self.roboto18 = tkFont.Font(family="Roboto", size=18, weight="normal")
        self.Stock_setting = LabelFrame(self, text=None, bg=colorPalette.lightbrown, border=0, borderwidth=0)
        self.Stock_quantity = LabelFrame(self, text=None, bg=colorPalette.lightbrown, border=0, borderwidth=0)
        self.Stock_price = LabelFrame(self, text=None, bg=colorPalette.lightbrown, border=0, borderwidth=0)
        self.Stock_totprice = LabelFrame(self, text=None, bg=colorPalette.lightbrown, border=0, borderwidth=0)
        self.Stock_setting.pack(side="top", fill="both", expand=True, padx=10)
        self.Stock_quantity.pack(side="top", fill="both", expand=True, padx=10 )
        self.Stock_price.pack(side="top", fill="both", expand=True, padx=10)
        self.Stock_totprice.pack(side="top", fill="both", expand=True, padx=10)


        # add radio btn and label to each label frame
        self.Stock_setting_radio = tk.IntVar()
        self.Stock_setting_radio.set(0)
        self.Stock_setting_radio1 = tk.Radiobutton(self.Stock_setting, text=None, variable=self.Stock_setting_radio, value=1, bg=colorPalette.lightbrown, fg="white", border=0)
        self.Stock_setting_radio1.pack(side="left", anchor="e")
        self.Stock_setting_label = Label(self.Stock_setting, text="Stock", bg=colorPalette.lightbrown, fg="white", font=self.roboto18)
        self.Stock_setting_label.pack(side="left", anchor="w")

        self.Stock_quantity_radio = tk.IntVar()
        self.Stock_quantity_radio.set(0)
        self.Stock_quantity_radio1 = tk.Radiobutton(self.Stock_quantity, text=None, variable=self.Stock_quantity_radio, value=1, bg=colorPalette.lightbrown, fg="white")
        self.Stock_quantity_radio1.pack(side="left", anchor="e")
        self.Stock_quantity_label = Label(self.Stock_quantity, text="Quantity", bg=colorPalette.lightbrown, fg="white", font=self.roboto18)
        self.Stock_quantity_label.pack(side="left", anchor="w")

        self.Stock_price_radio = tk.IntVar()
        self.Stock_price_radio.set(0)
        self.Stock_price_radio1 = tk.Radiobutton(self.Stock_price, text=None, variable=self.Stock_price_radio, value=1, bg=colorPalette.lightbrown, fg="white")
        self.Stock_price_radio1.pack(side="left",anchor="e")
        self.Stock_price_label = Label(self.Stock_price, text="Price", bg=colorPalette.lightbrown, fg="white", font=self.roboto18)
        self.Stock_price_label.pack(side="left", anchor="w")

        self.Stock_totprice_radio = tk.IntVar()
        self.Stock_totprice_radio.set(0)
        self.Stock_totprice_radio1 = tk.Radiobutton(self.Stock_totprice, text=None, variable=self.Stock_totprice_radio, value=1, bg=colorPalette.lightbrown, fg="white")
        self.Stock_totprice_radio1.pack(side="left", anchor="e")
        self.Stock_totprice_label = Label(self.Stock_totprice, text="TotPrice", bg=colorPalette.lightbrown, fg="white", font=self.roboto18)
        self.Stock_totprice_label.pack(side="left", anchor="w")






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

