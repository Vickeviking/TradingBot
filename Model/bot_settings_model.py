# bot_settings_model.py
from resources.stock_enums import *
from resources.app_enums import *


class bot_settings_model:
    def __init__(self, controller=None):
        self.controller = controller
        self.stocks = [] #max 4 stocks
        #buysignals
        self.buy_rsi_range = [0,100] # 0-100, 2 values, first is lower 
        self.buy_percentage_dip = 0
        self.buy_derivative_on_switch = False
        self.buy_derivative_steps = 0 # intervall
        self.buy_quantity_at_atime = 0 # 0-100%
        #sellsignals
        self.sell_profit_exit = 0 # 0-100%
        self.sell_loss_exit = 0
        self.sell_derivative_on_switch = False
        self.sell_derivative_steps = 0
        # start balance
        self.start_balance = 100
        # bot state
        self.bot_state = bot_states_enum.STOPPED.value








