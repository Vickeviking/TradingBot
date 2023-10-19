# Import the library tkinter
from tkinter import *
from Controller.bot_dialoge_controller import bot_dialoge_controller
from Controller.bot_graph_controller import bot_graph_controller
from Controller.bot_settings_controller import bot_settings_controller
from Controller.live_stocks_controller import live_stocks_controller
from resources.app_enums import ControllerTypes
from Model.market import market as marketClass
from Model.trade_bot import tradeBot as tradeBotClass

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

        #globals 
        self.botStatus = 2 # 1 = running, 2 = stopped

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


        # last touches (direct inits in creation canceled, because of circular dependencies?, bad error msg so hard to tell, but this way works)
        # give controllers acces to dialoge controller, to display msg
        self.trade_bot.settings = self.controllers[ControllerTypes.BOT_SETTINGS].model
        self.trade_bot.market = self.market
        self.controllers[ControllerTypes.BOT_SETTINGS].dialoge_controller = self.controllers[ControllerTypes.BOT_DIALOGUE]
        self.trade_bot.wallet.start_value = self.controllers[ControllerTypes.BOT_SETTINGS].model.start_balance
       
        


        # Start the update clock
        self.update_clock()

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
    
    def checkBotChange(self):
        bot_state = self.controllers[ControllerTypes.BOT_SETTINGS].model.bot_state.value
        if bot_state != self.botStatus: # bot state changed
            self.botStatus = bot_state
            #TODO act upon bot state change, view already implememnted but do these: 
                #TODO if started 
                    #TODO tradebot reset -> add settings to tradebot
                    #TODO market signal logic reset
                    #TODO wallet reset
                    #TODO market reset -> should now show the picked stocks 
                #TODO if stopped
                    #TODO tradebot reset
                    #TODO market signal logic reset
                    #TODO wallet reset
                    #TODO market reset -> should now show nothing ? 
                    #TODO show off values , turn off models ? each model having off/on state 

    
    
        

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
