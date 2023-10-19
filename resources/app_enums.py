from enum import Enum

class ControllerTypes(Enum):
    BOT_DIALOGUE = 1
    BOT_GRAPH = 2
    BOT_SETTINGS = 3
    LIVE_STOCKS = 4

class bot_states_enum(Enum):
    RUNNING = 1
    STOPPED = 2