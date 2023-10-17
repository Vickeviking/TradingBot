from tkinter import LabelFrame
from tkinter import Label
from tkinter import Radiobutton
from tkinter import font as tkFont
from tkinter import * 
from tkmacosx import Button as macButton
from resources.colorpalete import colorPalette as cp

class bot_settings_view_header(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        self.labelfont = tkFont.Font(family="Roboto", size=20, weight="normal")
        self.label = Label(self, text="Setup Tradebot", bg=cp.clayred, fg="white", font=self.labelfont)
        self.label.pack(pady=4, anchor="center")



class bot_settings_view_settings_panel_left(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0, height=4)
        self.pack_propagate(0)
        self.roboto22 = tkFont.Font(family="Roboto", size=22, weight="normal")
        self.roboto20 = tkFont.Font(family="Roboto", size=20, weight="normal")
        self.roboto18 = tkFont.Font(family="Roboto", size=18, weight="normal")
        self.roboto16 = tkFont.Font(family="Roboto", size=16, weight="normal")
        self.roboto14 = tkFont.Font(family="Roboto", size=14, weight="normal")

        self.topHeaderFrame = LabelFrame(self, bg=cp.clayred, border=0, borderwidth=0)
        self.headerFrame = LabelFrame(self.topHeaderFrame, bg=cp.clayred, border=0, borderwidth=0, pady=0)
        self.bottomHeaderFrame = LabelFrame(self.topHeaderFrame, bg=cp.clayred, border=0, borderwidth=0, pady=2)
        self.bottomHeaderFrameNasdaq = LabelFrame(self.bottomHeaderFrame, bg=cp.clayred, border=0, borderwidth=0, padx=1, pady=4)
        self.bottomHeaderFrameSthlm = LabelFrame(self.bottomHeaderFrame, bg=cp.clayred, border=0, borderwidth=0, padx=1, pady=4)

        self.nasdaqsthlmFrame = LabelFrame(self, bg=cp.clayred, border=0, borderwidth=0, padx=3, pady=10)

        self.nasdaqFrame = LabelFrame(self.nasdaqsthlmFrame, bg=cp.clayred, border=0, borderwidth=0, padx=5, pady=2)
        self.nasdaqstockFrame1 = LabelFrame(self.nasdaqFrame, bg=cp.clayred, border=0, borderwidth=0, padx = 0, pady=2)
        self.nasdaqstockFrame2 = LabelFrame(self.nasdaqFrame, bg=cp.clayred, border=0, borderwidth=0, padx = 0, pady=2)
        self.nasdaqstockFrame3 = LabelFrame(self.nasdaqFrame, bg=cp.clayred, border=0, borderwidth=0, padx = 0, pady=2)
        self.nasdaqstockFrame4 = LabelFrame(self.nasdaqFrame, bg=cp.clayred, border=0, borderwidth=0, padx = 0, pady=2)

        self.sthlmFrame = LabelFrame(self.nasdaqsthlmFrame, bg=cp.clayred, border=0, borderwidth=0, padx=5, pady=2)
        self.sthlmstockFrame1 = LabelFrame(self.sthlmFrame, bg=cp.clayred, border=0, borderwidth=0, padx = 0, pady=2)
        self.sthlmstockFrame2 = LabelFrame(self.sthlmFrame, bg=cp.clayred, border=0, borderwidth=0, padx = 0, pady=2)
        self.sthlmstockFrame3 = LabelFrame(self.sthlmFrame, bg=cp.clayred, border=0, borderwidth=0, padx = 0, pady=2)
        self.sthlmstockFrame4 = LabelFrame(self.sthlmFrame, bg=cp.clayred, border=0, borderwidth=0, padx = 0, pady=2)


        self.topHeaderFrame.pack()
        self.headerFrame.pack(side="top")
        self.bottomHeaderFrameNasdaq.pack(side="left")
        self.bottomHeaderFrameSthlm.pack(side="right")
        self.bottomHeaderFrame.pack(side="bottom")

        #header
        self.header = Label(self.headerFrame, text="Choose 4 stocks", bg=cp.clayred, fg="white", font=self.roboto20, height=1, padx=0, pady=0)
        self.header.pack()

        #Nasdaq stock pile, radio button & label 
        self.nasdaq_header = Label(self.bottomHeaderFrameNasdaq, text="Nasdaq", bg=cp.clayred, fg="white", font=self.roboto16)
        self.nasdaq_opening_hours = Label(self.bottomHeaderFrameNasdaq, text="15:30-22:00", bg=cp.clayred, fg="white", font=self.roboto14)
        self.nasdaq_tesla = Label(self.nasdaqstockFrame1, text="tesla", bg=cp.clayred, fg="white", font=self.roboto14)
        self.nasdaq_tesla_radio = Radiobutton(self.nasdaqstockFrame1, bg=cp.clayred, fg="white", font=self.roboto14)
        self.nasdaq_apple = Label(self.nasdaqstockFrame2, text="apple", bg=cp.clayred, fg="white", font=self.roboto14)
        self.nasdaq_apple_radio = Radiobutton(self.nasdaqstockFrame2, bg=cp.clayred, fg="white", font=self.roboto14)
        self.nasdaq_nvidia = Label(self.nasdaqstockFrame3, text="nvidia", bg=cp.clayred, fg="white", font=self.roboto14)
        self.nasdaq_nvidia_radio = Radiobutton(self.nasdaqstockFrame3, bg=cp.clayred, fg="white", font=self.roboto14)
        self.nasdaq_amazon = Label(self.nasdaqstockFrame4, text="amazon", bg=cp.clayred, fg="white", font=self.roboto14)
        self.nasdaq_amazon_radio = Radiobutton(self.nasdaqstockFrame4, bg=cp.clayred, fg="white", font=self.roboto14)
        #pack nasdaq stock pile
        self.nasdaqstockFrame1.pack()
        self.nasdaqstockFrame2.pack()
        self.nasdaqstockFrame3.pack()
        self.nasdaqstockFrame4.pack()
        # pack
        self.nasdaq_header.pack()
        self.nasdaq_opening_hours.pack()
        self.nasdaq_tesla.pack(side="left")
        self.nasdaq_tesla_radio.pack(side="right")
        self.nasdaq_apple.pack(side="left")
        self.nasdaq_apple_radio.pack(side="right")
        self.nasdaq_nvidia.pack(side="left")
        self.nasdaq_nvidia_radio.pack(side="right")
        self.nasdaq_amazon.pack(side="left")
        self.nasdaq_amazon_radio.pack(side="right")
        # paclk nasdaq frame
        self.nasdaqFrame.pack(side="left")


        #sthlm stock pile, radio button & label
        self.sthlm_header = Label(self.bottomHeaderFrameSthlm, text="Stockholm", bg=cp.clayred, fg="white", font=self.roboto16)
        self.sthlm_opening_hours = Label(self.bottomHeaderFrameSthlm, text="09:00-17:30", bg=cp.clayred, fg="white", font=self.roboto14)
        self.sthlm_astrazeneca = Label(self.sthlmstockFrame1, text="AstraZeneca", bg=cp.clayred, fg="white", font=self.roboto14)
        self.sthlm_astrazeneca_radio = Radiobutton(self.sthlmstockFrame1, bg=cp.clayred, fg="white", font=self.roboto14)
        self.sthlm_investorab = Label(self.sthlmstockFrame2, text="InvestorAB", bg=cp.clayred, fg="white", font=self.roboto14)
        self.sthlm_investorab_radio = Radiobutton(self.sthlmstockFrame2, bg=cp.clayred, fg="white", font=self.roboto14)
        self.sthlm_abb = Label(self.sthlmstockFrame3, text="abb", bg=cp.clayred, fg="white", font=self.roboto14)
        self.sthlm_abb_radio = Radiobutton(self.sthlmstockFrame3, bg=cp.clayred, fg="white", font=self.roboto14)
        self.sthlm_atlascopco = Label(self.sthlmstockFrame4, text="atlas copco", bg=cp.clayred, fg="white", font=self.roboto14)
        self.sthlm_atlascopco_radio = Radiobutton(self.sthlmstockFrame4, bg=cp.clayred, fg="white", font=self.roboto14)
        #pack sthlm stock pile
        self.sthlmstockFrame1.pack()
        self.sthlmstockFrame2.pack()
        self.sthlmstockFrame3.pack()
        self.sthlmstockFrame4.pack()
        # pack
        self.sthlm_header.pack()
        self.sthlm_opening_hours.pack()
        self.sthlm_astrazeneca.pack(side="left")
        self.sthlm_astrazeneca_radio.pack(side="right")
        self.sthlm_investorab.pack(side="left")
        self.sthlm_investorab_radio.pack(side="right")
        self.sthlm_abb.pack(side="left")
        self.sthlm_abb_radio.pack(side="right")
        self.sthlm_atlascopco.pack(side="left")
        self.sthlm_atlascopco_radio.pack(side="right")
        # pack sthlm frame
        self.sthlmFrame.pack(side="right")

        #pack sthlm and nasdaq frame
        self.nasdaqsthlmFrame.pack()

        #pack header & times
        self.nasdaq_header.pack()
        self.nasdaq_opening_hours.pack()
        self.sthlm_header.pack()
        self.sthlm_opening_hours.pack()


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
    def __init__(self, master=None,controller=None, text=None, bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        self.pack_propagate(0)
        self.roboto22 = tkFont.Font(family="Roboto", size=22, weight="normal")
        self.roboto20 = tkFont.Font(family="Roboto", size=20, weight="normal")
        self.roboto18 = tkFont.Font(family="Roboto", size=18, weight="normal")
        self.roboto16 = tkFont.Font(family="Roboto", size=16, weight="normal")
        self.roboto14 = tkFont.Font(family="Roboto", size=14, weight="normal")

        self.headerFrame = LabelFrame(self, bg=cp.clayred, border=0, borderwidth=0, pady=0)
        self.headerFrame.pack(side="top", anchor="n")

        self.leftrightCpntr = LabelFrame(self.headerFrame, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0)
        self.leftrightCpntr.pack(side="bottom")

        self.leftlayerContainer = LabelFrame(self.leftrightCpntr, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=5)
        self.leftlayerContainer.pack(side="left", anchor="n")

        self.layerl1 = LabelFrame( self.leftlayerContainer, bg=cp.clayred, border=0, borderwidth=0, padx=5, pady=1)
        self.layerl1.pack()

        self.layerl2 = LabelFrame( self.leftlayerContainer, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=6)
        self.layerl2.pack()
        self.layerl2_1 = LabelFrame( self.layerl2, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0)
        self.layerl2_1.pack(side="top")
        self.layerl2_2 = LabelFrame( self.layerl2, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0)
        self.layerl2_2.pack(side="bottom")

        self.layerl3 = LabelFrame( self.leftlayerContainer, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=6)
        self.layerl3.pack()
        self.layerl3_1 = LabelFrame( self.layerl3, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0)
        self.layerl3_1.pack(side="top")
        self.layerl3_2 = LabelFrame( self.layerl3, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0)
        self.layerl3_2.pack(side="bottom")

        self.layerl4 = LabelFrame( self.leftlayerContainer, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=6)
        self.layerl4.pack()
        self.layerl4_1 = LabelFrame( self.layerl4, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0)
        self.layerl4_1.pack(side="top")
        self.layerl4_2 = LabelFrame( self.layerl4, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0)
        self.layerl4_2.pack(side="bottom")

        self.layerl5 = LabelFrame( self.leftlayerContainer, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=6)
        self.layerl5.pack()
        self.layerl5_1 = LabelFrame( self.layerl5, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0)
        self.layerl5_1.pack(side="top")
        self.layerl5_2 = LabelFrame( self.layerl5, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0)
        self.layerl5_2.pack(side="bottom")


        self.paddingFrame = LabelFrame(self.leftrightCpntr, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0, width=50)
        self.paddingFrame.pack(side="left")


        self.rightlayerContainer = LabelFrame(self.leftrightCpntr, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=5)
        self.rightlayerContainer.pack(side="left", anchor="n")
        self.layerr1 = LabelFrame( self.rightlayerContainer, bg=cp.clayred, border=0, borderwidth=0, padx=5, pady=1)
        self.layerr1.pack()

        self.layerr2 = LabelFrame( self.rightlayerContainer, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=6)
        self.layerr2.pack()
        self.layerr2_1 = LabelFrame( self.layerr2, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0)
        self.layerr2_1.pack(side="top")
        self.layerr2_2 = LabelFrame( self.layerr2, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0)
        self.layerr2_2.pack(side="bottom")

        self.layerr3 = LabelFrame( self.rightlayerContainer, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=6)
        self.layerr3.pack()
        self.layerr3_1 = LabelFrame( self.layerr3, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0)
        self.layerr3_1.pack(side="top")
        self.layerr3_2 = LabelFrame( self.layerr3, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0)
        self.layerr3_2.pack(side="bottom")

        self.layerr4 = LabelFrame( self.rightlayerContainer, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=6)
        self.layerr4.pack()
        self.layerr4_1 = LabelFrame( self.layerr4, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0)
        self.layerr4_1.pack(side="top")
        self.layerr4_2 = LabelFrame( self.layerr4, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=0)
        self.layerr4_2.pack(side="bottom")

        self.layerr5 = LabelFrame( self.rightlayerContainer, bg=cp.clayred, border=0, borderwidth=0, padx=0, pady=6)
        self.layerr5.pack()

        #left layer 1
        self.layerl1_label = Label(self.layerl1, text="Buy-signals", bg=cp.clayred, fg="white", font=self.roboto18)
        self.layerl1_label.pack()
        #left layer 2
        self.layerl2_1_label = Label(self.layerl2_1, text="RSI range", bg=cp.clayred, fg="white", font=self.roboto14)
        self.layerl2_1_label.pack()
        self.layerl2_2_numberinput1 = Entry(self.layerl2_2, bg="white", fg="black", font=self.roboto14, width=2)
        self.layerl2_2_numberinput1.pack(side="left")
        self.layerl2_2_label = Label(self.layerl2_2, text="-", bg=cp.clayred, fg="white", font=self.roboto14)
        self.layerl2_2_label.pack( side="left")
        self.layerl2_2_numberinput2 = Entry(self.layerl2_2, bg="white", fg="black", font=self.roboto14, width=2)
        self.layerl2_2_numberinput2.pack(side="left")
        #left layer 3
        self.layerl3_1_label = Label(self.layerl3_1, text="Procentage dip", bg=cp.clayred, fg="white", font=self.roboto14)
        self.layerl3_1_label.pack()
        self.layerl3_2_slider = Scale(self.layerl3_2, from_=0, to=100, bg=cp.smoothblack, fg="white", font=self.roboto14, orient=HORIZONTAL, length=70, showvalue=False)
        self.layerl3_2_slider.pack(side="left")
        self.layerl3_2_label = Label(self.layerl3_2, text="0%", bg=cp.clayred, fg="white", font=self.roboto20)
        self.layerl3_2_label.pack(side="left")
        #left layer 4
        self.layerl4_1_label = Label(self.layerl4_1, text="Derivative Switch", bg=cp.clayred, fg="white", font=self.roboto14)
        self.layerl4_1_label.pack()
        self.layerl4_2_button = macButton(self.layerl4_2, text="OFF", bg=cp.smoothblack, fg="white", font=self.roboto14, width=40)
        self.layerl4_2_button.pack(side="left")
        self.layerl4_2_label2 = Label(self.layerl4_2, text="steps", bg=cp.clayred, fg="white", font=self.roboto20, padx=5)
        self.layerl4_2_label2.pack(side="left")
        self.layerl4_2_numberinput = Entry(self.layerl4_2, bg="white", fg="black", font=self.roboto14, width=1)
        self.layerl4_2_numberinput.pack(side="left")
        #left layer 5
        self.layerl5_1_label = Label(self.layerl5_1, text="Quantity at a time", bg=cp.clayred, fg="white", font=self.roboto14)
        self.layerl5_1_label.pack()
        self.layerl5_2_slider = Scale(self.layerl5_2, from_=0, to=100, bg=cp.smoothblack, fg="white", font=self.roboto14, orient=HORIZONTAL, length=70, showvalue=False)
        self.layerl5_2_slider.pack(side="left")
        self.layerl5_2_label = Label(self.layerl5_2, text="0%", bg=cp.clayred, fg="white", font=self.roboto20)
        self.layerl5_2_label.pack(side="left")

        #right layer 1
        self.layerr1_label = Label(self.layerr1, text="Sell-signals", bg=cp.clayred, fg="white", font=self.roboto18)
        self.layerr1_label.pack(side="top", anchor="n")
        #right layer 2
        self.layerr2_1_label = Label(self.layerr2_1, text="Profit exit", bg=cp.clayred, fg="white", font=self.roboto14)
        self.layerr2_1_label.pack()
        self.layerr2_2_slider = Scale(self.layerr2_2, from_=0, to=100, bg=cp.smoothblack, fg="white", font=self.roboto14, orient=HORIZONTAL, length=70, showvalue=False)
        self.layerr2_2_slider.pack(side="left")
        self.layerr2_2_label = Label(self.layerr2_2, text="0%", bg=cp.clayred, fg="white", font=self.roboto20)
        self.layerr2_2_label.pack(side="left")
        #right layer 3
        self.layerr3_1_label = Label(self.layerr3_1, text="Loss exit", bg=cp.clayred, fg="white", font=self.roboto14)
        self.layerr3_1_label.pack()
        self.layerr3_2_slider = Scale(self.layerr3_2, from_=0, to=100, bg=cp.smoothblack, fg="white", font=self.roboto14, orient=HORIZONTAL, length=70, showvalue=False)
        self.layerr3_2_slider.pack(side="left")
        self.layerr3_2_label = Label(self.layerr3_2, text="0%", bg=cp.clayred, fg="white", font=self.roboto20)
        self.layerr3_2_label.pack(side="left")
        #right layer 4
        self.layerr4_1_label = Label(self.layerr4_1, text="Derivative Switch", bg=cp.clayred, fg="white", font=self.roboto14)
        self.layerr4_1_label.pack()
        self.layerr4_2_button = macButton(self.layerr4_2, text="OFF", bg=cp.smoothblack, fg="white", font=self.roboto14, width=40)
        self.layerr4_2_button.pack(side="left")
        self.layerr4_2_label2 = Label(self.layerr4_2, text="steps", bg=cp.clayred, fg="white", font=self.roboto20, padx=5)
        self.layerr4_2_label2.pack(side="left")
        self.layerr4_2_numberinput = Entry(self.layerr4_2, bg="white", fg="black", font=self.roboto14, width=1)
        self.layerr4_2_numberinput.pack(side="left")








class bot_settings_view_settings_panel(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=cp.clayred):
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
    def __init__(self, master=None,controller=None, text=None, bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        self.pack_propagate(0)
        self.roboto18 = tkFont.Font(family="Roboto", size=18, weight="normal")
        # create class instance
        self.padding = Label(self, bg=cp.clayred, width=4)
        self.start_balance = Label(self, text="Start balance: ", bg=cp.clayred, fg="white", font=self.roboto18)
        self.start_balance_entry = Entry(self, bg="white", fg="black", font=self.roboto18, width=6)
        self.padding2 = Label(self, bg=cp.clayred, width=4)
        self.save_settings_button = macButton(self, text="Save settings", bg=cp.smoothblack, fg="white", font=self.roboto18, width=140)
        self.padding3 = Label(self, bg=cp.clayred, width=2)
        self.start_bot_button = macButton(self, text="Start bot", bg=cp.smoothblack, fg="white", font=self.roboto18, width=90)

        # add to grid
        self.padding.pack(side="left")
        self.start_balance.pack(side="left", padx=4)
        self.start_balance_entry.pack(side="left")
        self.padding2.pack(side="left")
        self.save_settings_button.pack(side="left")
        self.padding3.pack(side="left")
        self.start_bot_button.pack(side="left")


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
        self.grid_rowconfigure(3, weight=60)
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
    

