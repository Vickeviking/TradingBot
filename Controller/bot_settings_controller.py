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
        self.trade_bot = None # the tradebot model


    def get_label_frame(self):
        return self.view
    
    # setters
    def set_new_stock(self, stock):
        if len(self.model.stocks) < 4:
            self.model.stocks.append(stock)
    def remove_stock(self, stock):
        self.model.stocks.remove(stock)

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
        #stocks = [], buy_rsi_range = [0,100], buy_percentage_dip = 0, buy_derivative_on_switch = False, buy_derivative_steps = 0, buy_quantity_at_atime = 0, sell_profit_exit = 0, sell_loss_exit = 0, sell_derivative_on_switch = False, sell_derivative_steps = 0, start_balance = 100
        self.updatedSettings = ts(self.model.stocks, self.model.buy_rsi_range, self.model.buy_percentage_dip, self.model.buy_derivative_on_switch, self.model.buy_derivative_steps, self.model.buy_quantity_at_atime, self.model.sell_profit_exit, self.model.sell_loss_exit, self.model.sell_derivative_on_switch, self.model.sell_derivative_steps, self.model.start_balance)
        self.trade_bot.implementedSettings = self.updatedSettings
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




