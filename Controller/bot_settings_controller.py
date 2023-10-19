# bot_dialogue_controller.py
from View.bot_settings_view import bot_settings_veiw
from Model.bot_settings_model import *
from resources.stock_enums import *
from resources.app_enums import ControllerTypes
from resources.colorpalete import colorPalette
from Model.trade_bot import mySettings as ts #tradebot settings

class bot_settings_controller:
    def __init__(self, master=None, ):
        self.master = master
        # Create a frame for the label frame
        self.view = bot_settings_veiw(master=self.master, controller=self) 
        self.view.grid(row=0, column=0, sticky="nsew")  
        #create model
        self.model = bot_settings_model(self)
        self.dialoge_controller = None
        # needs market model , aswell as live_stocks_model
        self.market_model = None
        self.live_stocks_model = None
        self.trade_bot = None # the tradebot model


    def get_label_frame(self):
        return self.view
    
    # setters
    def set_new_stock(self, stock):
        if len(self.model.stocks) < 4:
            self.model.stocks.append(stock)
    def remove_stock(self, stock):
        self.model.stocks.remove(stock)
    
    def set_dialoge_controller(self, dialoge_controller):
        self.dialoge_controller = dialoge_controller
    def set_market_model(self, market_model):
        self.market_model = market_model
    def set_live_stocks_model(self, live_stocks_model):
        self.live_stocks_model = live_stocks_model
    def set_trade_bot(self, trade_bot):
        self.trade_bot = trade_bot
        if self.trade_bot.market != None:
            self.market_model = self.trade_bot.market

    # setttings

    # buy signals
    def set_buy_lower_rsi(self, rsi_lower):
        if rsi_lower != "" and int(rsi_lower) < int(self.model.buy_rsi_range[1]):
            self.model.buy_rsi_range[0] = rsi_lower
    def set_buy_upper_rsi(self, rsi_upper):
        if rsi_upper != "" and int(rsi_upper) > int(self.model.buy_rsi_range[0]):
            self.model.buy_rsi_range[1] = rsi_upper
    def set_buy_percentage_dip(self, percentage_dip):
        self.model.buy_percentage_dip = percentage_dip
    def set_buy_derivative_on_switch(self, derivative_on_switch):
        self.model.buy_derivative_on_switch = derivative_on_switch
    def set_buy_derivative_steps(self, derivative_steps):
        self.model.buy_derivative_steps = derivative_steps
    def set_buy_quantity_at_atime(self, quantity_at_atime):
        self.model.buy_quantity_at_atime = quantity_at_atime
    # sell signals
    def set_sell_profit_exit(self, profit_exit):
        self.model.sell_profit_exit = profit_exit
    def set_sell_loss_exit(self, loss_exit):
        self.model.sell_loss_exit = loss_exit
    def set_sell_derivative_on_switch(self, derivative_on_switch):
        self.model.sell_derivative_on_switch = derivative_on_switch
    def set_sell_derivative_steps(self, derivative_steps):
        self.model.sell_derivative_steps = derivative_steps
    # start balance
    def set_start_balance(self, start_balance):
        self.model.start_balance = start_balance
    # bot state
    def set_bot_state(self, bot_state):
        self.model.bot_state = bot_state

    def stockbtn_clicked(self, stock):
        if stock in self.model.stocks:
            self.remove_stock(stock)
            self.update()
        else:
            self.set_new_stock(stock)
            self.update()

    def startBtnClicked(self):
        if len(self.model.stocks) < 4:
            self.message = "Please select 4 stocks first"
            self.dialoge_controller.addMessage(customMessage=self.message)
            return
        msgColor = None
        if self.model.bot_state == bot_states_enum.STOPPED.value:
            self.set_bot_state(bot_states_enum.RUNNING)
            msgColor = colorPalette.neongreen
        else:
            self.set_bot_state(bot_states_enum.STOPPED)
            msgColor = colorPalette.neonred
        # dialoge message 
        self.message = "Bot state changed to: " + self.model.bot_state.name
        self.dialoge_controller.addMessage(customMessage=self.message, customMessage_color=msgColor)
        # set new settings to bot 
        self.updatedSettings = ts(self.model.stocks, self.model.buy_rsi_range, self.model.buy_percentage_dip, self.model.buy_derivative_on_switch, self.model.buy_derivative_steps, self.model.buy_quantity_at_atime, self.model.sell_profit_exit, self.model.sell_loss_exit, self.model.sell_derivative_on_switch, self.model.sell_derivative_steps, self.model.start_balance)
        self.trade_bot.implementedSettings = self.updatedSettings
        # update stocks in live_stock_model, dynamic stocks
        self.live_stocks_model.setStocks(self.model.stocks) #should contain tickets ?
        # update stocks in market 
        self.market_model.updateStocktypes(self.model.stocks) #should contain tickets ? 

        self.update()

    def save_settings_clicked(self):
        # dialoge message 
        if self.model.bot_state == bot_states_enum.RUNNING.value:
            self.message = "Stop bot to apply settings"
            self.dialoge_controller.addMessage(customMessage=self.message)
            self.update()
        else:
            self.message = "Settings saved"
            self.dialoge_controller.addMessage(customMessage=self.message)
            self.update()

    


    def update(self):
        # update radio btn for stocks
        self.view.updateRadioBtn(self.model.stocks)
        self.view.updateBuySignals(self.model.buy_percentage_dip, self.model.buy_quantity_at_atime)
        self.view.updateSellSignals(self.model.sell_profit_exit, self.model.sell_loss_exit)
        self.view.update()




