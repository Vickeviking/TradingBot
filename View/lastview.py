
class bot_settings_view_header(LabelFrame):
    def __init__(self, master=None,controller=None, text=None, bg=cp.clayred):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        self.labelfont = tkFont.Font(family="Roboto", size=20, weight="normal")
        self.label = Label(self, text="Setup Tradebot", bg=cp.clayred, fg="white", font=self.labelfont)
        #place a bit to the left
        self.label.pack(side="left")


class bot_settings_view_settings_panel_left(LabelFrame):
    def __init__(self, master=None, controller=None, text=None, bg=cp.clayred, fg="white"):
        super().__init__(master, text=text, bg=bg)
        self.master = master
        self.controller = controller
        self.configure(border=0, borderwidth=0)
        self.roboto20 = tkFont.Font(family="Roboto", size=24, weight="normal")
        self.roboto16 = tkFont.Font(family="Roboto", size=20, weight="normal")
        self.roboto14 = tkFont.Font(family="Roboto", size=18, weight="normal")

        #setup grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)

       
        #Nasdaq stock pile, radio button & label 
         #tesla
        self.nasdaq_tesla = Label(self, text="tesla", bg=cp.clayred, fg="white", font=self.roboto14)
        self.nasdaq_tesla_radio = Radiobutton(self, bg=cp.clayred, fg="white", font=self.roboto14)
         #apple
        self.nasdaq_apple = Label(self, text="apple", bg=cp.clayred, fg="white", font=self.roboto14)
        self.nasdaq_apple_radio = Radiobutton(self, bg=cp.clayred, fg="white", font=self.roboto14)
         #Nvidia
        self.nasdaq_nvidia = Label(self, text="nvidia", bg=cp.clayred, fg="white", font=self.roboto14)
        self.nasdaq_nvidia_radio = Radiobutton(self, bg=cp.clayred, fg="white", font=self.roboto14)
         #Amazon
        self.nasdaq_amazon = Label(self, text="amazon", bg=cp.clayred, fg="white", font=self.roboto14)
        self.nasdaq_amazon_radio = Radiobutton(self, bg=cp.clayred, fg="white", font=self.roboto14)
        #sthlm stock pile, radio button & label
         #AstraZeneca
        self.sthlm_astrazeneca = Label(self, text="AstraZeneca", bg=cp.clayred, fg="white", font=self.roboto14)
        self.sthlm_astrazeneca_radio = Radiobutton(self, bg=cp.clayred, fg="white", font=self.roboto14)
         #InvestorAB
        self.sthlm_investorab = Label(self, text="InvestorAB", bg=cp.clayred, fg="white", font=self.roboto14)
        self.sthlm_investorab_radio = Radiobutton(self, bg=cp.clayred, fg="white", font=self.roboto14)
          #abb
        self.sthlm_abb = Label(self, text="abb", bg=cp.clayred, fg="white", font=self.roboto14)
        self.sthlm_abb_radio = Radiobutton(self, bg=cp.clayred, fg="white", font=self.roboto14)
            #AtlasCopco
        self.sthlm_atlascopco = Label(self, text="AtlasCopco", bg=cp.clayred, fg="white", font=self.roboto14)
        self.sthlm_atlascopco_radio = Radiobutton(self, bg=cp.clayred, fg="white", font=self.roboto14)

  
        self.nasdaq_tesla_radio.grid(row=3, column=0, sticky="nse")
        self.nasdaq_tesla.grid(row=3, column=1, sticky="nsw")
        self.nasdaq_apple_radio.grid(row=4, column=0, sticky="nse")
        self.nasdaq_apple.grid(row=4, column=1, sticky="nsw")
        self.nasdaq_nvidia_radio.grid(row=5, column=0, sticky="nse")
        self.nasdaq_nvidia.grid(row=5, column=1, sticky="nsw")
        self.nasdaq_amazon_radio.grid(row=6, column=0, sticky="nse")
        self.nasdaq_amazon.grid(row=6, column=1, sticky="nsw")













    