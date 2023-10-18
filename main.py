# Import the library tkinter
from tkinter import *
from Controller.bot_dialoge_controller import bot_dialoge_controller
from Controller.bot_graph_controller import bot_graph_controller
from Controller.bot_settings_controller import bot_settings_controller
from Controller.live_stocks_controller import live_stocks_controller
from resources.app_enums import ControllerTypes

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

        # Initializing controllers
        self.controllers = {
            ControllerTypes.BOT_DIALOGUE: bot_dialoge_controller(self.app),
            ControllerTypes.BOT_GRAPH: bot_graph_controller(self.app),
            ControllerTypes.BOT_SETTINGS: bot_settings_controller(self.app),
            ControllerTypes.LIVE_STOCKS: live_stocks_controller(self.app)
        }
        # give controllers acces to dialoge controller, to display msg
        self.controllers[ControllerTypes.BOT_SETTINGS].dialoge_controller = self.controllers[ControllerTypes.BOT_DIALOGUE]


        bot_dialoge_frame = self.controllers[ControllerTypes.BOT_DIALOGUE].get_label_frame()
        bot_dialoge_frame.pack_propagate(0)
        bot_graph_frame = self.controllers[ControllerTypes.BOT_GRAPH].get_label_frame()
        bot_graph_frame.pack_propagate(0)
        bot_settings_frame = self.controllers[ControllerTypes.BOT_SETTINGS].get_label_frame()
        
        live_stocks_frame = self.controllers[ControllerTypes.LIVE_STOCKS].get_label_frame()
        
        # Displaying in frame
        bot_dialoge_frame.grid(row=0, column=0, sticky="nsew")
        bot_graph_frame.grid(row=0, column=1, sticky="nsew")
        bot_settings_frame.grid(row=0, column=2, sticky="nsew")
        live_stocks_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")

        # Start the update clock
        self.update_clock()

    def update_clock(self):
        # implement updates here
        self.controllers[ControllerTypes.BOT_DIALOGUE].update()
        self.controllers[ControllerTypes.BOT_GRAPH].update()
        self.controllers[ControllerTypes.BOT_SETTINGS].update()
        self.controllers[ControllerTypes.LIVE_STOCKS].update()
        self.app.after(300, self.update_clock)
        
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
