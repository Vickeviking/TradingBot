# Import the library tkinter
from tkinter import *
from Controller.bot_dialoge_controller import bot_dialoge_controller
from Controller.bot_graph_controller import bot_graph_controller
from Controller.bot_settings_controller import bot_settings_controller
from Controller.live_stocks_controller import live_stocks_controller
from resources.app_enums import ControllerTypes
from Model.market import market as marketClass
from Model.trade_bot import tradeBot as tradeBotClass
from resources.app_enums import bot_states_enum as bot_states

class MyApp:
    def __init__(self):
        self.app = Tk()
        self.app.title("Minute Trade Bot")
        self.app.geometry("2560x1600+0+0")
        self.app.grid_columnconfigure(0, weight=355000)
        self.app.grid_columnconfigure(1, weight=234375)
        self.app.grid_columnconfigure(2, weight=441100)
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_rowconfigure(1, weight=1)
        self.timeDelay = 3000 #ms

        #globals 
        self.botStatus = bot_states.STOPPED # 1 = running, 2 = stopped

        # Initializing controllers
        self.controllers = {
            ControllerTypes.BOT_DIALOGUE: bot_dialoge_controller(self.app),
            ControllerTypes.BOT_GRAPH: bot_graph_controller(self.app),
            ControllerTypes.BOT_SETTINGS: bot_settings_controller(self.app),
            ControllerTypes.LIVE_STOCKS: live_stocks_controller(self.app)
        }
        # Initializing frames
        bot_dialoge_frame = self.controllers[ControllerTypes.BOT_DIALOGUE].get_label_frame()
        bot_dialoge_frame.pack_propagate(0)
        bot_graph_frame = self.controllers[ControllerTypes.BOT_GRAPH].get_label_frame()
        bot_graph_frame.pack_propagate(0)
        bot_settings_frame = self.controllers[ControllerTypes.BOT_SETTINGS].get_label_frame()
        bot_settings_frame.pack_propagate(0)
        live_stocks_frame = self.controllers[ControllerTypes.LIVE_STOCKS].get_label_frame()
        live_stocks_frame.pack_propagate(0)

        # Displaying frames
        bot_dialoge_frame.grid(row=0, column=0, sticky="nsew")
        bot_graph_frame.grid(row=0, column=1, sticky="nsew")
        bot_settings_frame.grid(row=0, column=2, sticky="nsew")
        live_stocks_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")

        #init system models 
        self.market = marketClass()  
        self.trade_bot = tradeBotClass()
       
        # give settingControll needs to update alot, needs ptr
        self.trade_bot.setMarket(self.market)
        self.market.stockViewModel = self.controllers[ControllerTypes.LIVE_STOCKS].model
        self.controllers[ControllerTypes.BOT_SETTINGS].set_dialoge_controller(self.controllers[ControllerTypes.BOT_DIALOGUE])
        self.controllers[ControllerTypes.BOT_SETTINGS].set_market_model(self.market)
        self.controllers[ControllerTypes.BOT_SETTINGS].set_live_stocks_model(self.controllers[ControllerTypes.LIVE_STOCKS].model)
        self.controllers[ControllerTypes.BOT_SETTINGS].set_trade_bot(self.trade_bot)
       
        # Start the update clock
        self.update_clock()
        self.updateStockViewModel()

    def update_clock(self):
        # update controllers, frames are updated by controllers
        self.controllers[ControllerTypes.BOT_DIALOGUE].update()
        self.controllers[ControllerTypes.BOT_GRAPH].update()
        self.controllers[ControllerTypes.BOT_SETTINGS].update()
        self.controllers[ControllerTypes.LIVE_STOCKS].update()
        # update system models (are "floating around and used by controllers, so stored in top layer")
        self.market.update()
        self.trade_bot.update()
        self.checkBotChange()

        self.app.after(300, self.update_clock)

    def updateStockViewModel(self):
        if len(self.controllers[ControllerTypes.LIVE_STOCKS].model.stocks) != 0:
            for i in range(4):
                self.controllers[ControllerTypes.LIVE_STOCKS].model.stocks[i].update10StockValues()
        self.app.after(self.timeDelay, self.updateStockViewModel)
    
    def checkBotChange(self):
        bot_state = self.controllers[ControllerTypes.BOT_SETTINGS].model.bot_state
        if bot_state != self.botStatus.value: # bot state changed
            if bot_state == bot_states.RUNNING.value: #only checking if changed 
                    self.botStatus = bot_states.RUNNING
                    self.trade_bot.switchState(bot_states.RUNNING) #make neceseary "resets"
                    self.market.switchState(bot_states.RUNNING) # -- || –- 
                    self.controllers[ControllerTypes.LIVE_STOCKS].view.switchState(bot_states.RUNNING)
            else:
                    self.botStatus = bot_states.STOPPED
                    self.trade_bot.switchState(bot_states.STOPPED)
                    self.market.switchState(bot_states.STOPPED)
                    self.controllers[ControllerTypes.LIVE_STOCKS].view.switchState(bot_states.STOPPED)

    
    
        

    def run(self):
        # Start the main loop
        self.app.mainloop()

    def get_controller(self, controller_type):
        return self.controllers[controller_type]




def main():
    my_app = MyApp()
    my_app.run()

if __name__ == "__main__":
    main()
