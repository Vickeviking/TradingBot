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
    Astrazeneca = "AZN",
    Investorb = "INVE-B.ST",
    ABB = "ABB.ST",
    AtlasCopco = "ATCO-A.ST"
    def determineTypeFromTicket(ticketString):
        if ticketString == stock_tickets.Tesla.value:
            return stock_types_enum.Tesla
        elif ticketString == stock_tickets.Apple.value:
            return stock_types_enum.Apple
        elif ticketString == stock_tickets.Nvidia.value:
            return stock_types_enum.Nvidia
        elif ticketString == stock_tickets.Amazon.value:
            return stock_types_enum.Amazon
        elif ticketString == stock_tickets.Astrazeneca.value:
            return stock_types_enum.Astrazeneca
        elif ticketString == stock_tickets.Investorb.value:
            return stock_types_enum.Investorb
        elif ticketString == stock_tickets.ABB.value:
            return stock_types_enum.ABB
        elif ticketString == stock_tickets.AtlasCopco.value:
            return stock_types_enum.AtlasCopco
        else:
            return None
    def determineNameFromTicket(ticketString):
        #return string name of stock
        if ticketString == stock_tickets.Tesla.value:
            return "Tesla"
        elif ticketString == stock_tickets.Apple.value:
            return "Apple"
        elif ticketString == stock_tickets.Nvidia.value:
            return "Nvidia"
        elif ticketString == stock_tickets.Amazon.value:
            return "Amazon"
        elif ticketString == stock_tickets.Astrazeneca.value:
            return "Astrazeneca"
        elif ticketString == stock_tickets.Investorb.value:
            return "Investor B"
        elif ticketString == stock_tickets.ABB.value:
            return "ABB"
        elif ticketString == stock_tickets.AtlasCopco.value:
            return "Atlas Copco"
        else:
            return None

class stock_regions(Enum):
    Tesla = "US",
    Apple = "US",
    Nvidia = "US",
    Amazon = "US",
    Astrazeneca = "SE",
    Investorb = "SE",
    ABB = "SE",
    AtlasCopco = "SE"
    def determineRegionFromTicket(ticketString):
        if ticketString == stock_tickets.Tesla.value:
            return stock_regions.Tesla
        elif ticketString == stock_tickets.Apple.value:
            return stock_regions.Apple
        elif ticketString == stock_tickets.Nvidia.value:
            return stock_regions.Nvidia
        elif ticketString == stock_tickets.Amazon.value:
            return stock_regions.Amazon
        elif ticketString == stock_tickets.Astrazeneca.value:
            return stock_regions.Astrazeneca
        elif ticketString == stock_tickets.Investorb.value:
            return stock_regions.Investorb
        elif ticketString == stock_tickets.ABB.value:
            return stock_regions.ABB
        elif ticketString == stock_tickets.AtlasCopco.value:
            return stock_regions.AtlasCopco
        else:
            return None





