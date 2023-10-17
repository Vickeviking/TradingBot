from enum import Enum

class stock_types_enum(Enum):
    #nasdaq stocks
    Tesla = 1,
    Apple = 2,
    Nvidia = 3,
    Amazon = 4,
    #sthlm stocks
    Astrazeneca = 5,
    Investorb = 6,
    ABB = 7,
    AtlasCopco = 8

class stock_tickets(Enum):
    Tesla = "TSLA",
    Apple = "AAPL",
    Nvidia = "NVDA",
    Amazon = "AMZN",
    Astrazeneca = "AZN.ST",
    Investorb = "INVE-B.ST",
    ABB = "ABB.ST",
    AtlasCopco = "ATCO-A.ST"

class stock_regions(Enum):
    Tesla = "US",
    Apple = "US",
    Nvidia = "US",
    Amazon = "US",
    Astrazeneca = "SE",
    Investorb = "SE",
    ABB = "SE",
    AtlasCopco = "SE"





