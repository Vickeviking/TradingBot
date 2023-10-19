
from Model.fetch_data import fetchData
from Model.stock import stock
from resources.app_enums import bot_states_enum as bot_states

class market:
    def __init__(self):
        self.bot_state = bot_states.STOPPED
        self.showStocks = False
    def update(self):
        if self.bot_state == bot_states.STOPPED.value: #TODO could cause error, double check compatinbility
            return
    def switchState(self, botStateParam):
        if botStateParam == bot_states.STOPPED.value: # switched off
            self.bot_state = bot_states.STOPPED
            self.showStocks = False
        else: # switched on
            self.bot_state = bot_states.RUNNING
            self.showStocks = True
            pass