from resources.stock_enums import stock_tickets
from resources.stock_enums import stock_regions

#bought stocks are static, ones in live view are dynamic
class stock:
    def __init__(self,staticVersion = False, stockTicket = "", stockValue = 0, stockValueChange = 0, stockValueChangePercentage = 0):
        self.staticVersion = staticVersion
        self.stockTicket = stockTicket
        self.stockType = None
        self.stockValue = stockValue
        self.stockValueChange = stockValueChange
        self.stockValueChangePercentage = stockValueChangePercentage
        self.region = None
        #set stock type and region
        self.stockType = stock_tickets.determineTypeFromTicket(stockTicket)
        self.region = stock_regions.determineRegionFromTicket(stockTicket)
        self.stockName = stock_tickets.determineNameFromTicket(stockTicket)



    def setStockTicket(self, stockTicketString):
        self.stockType = stock_tickets.determineTypeFromTicket(stockTicketString)
        self.region = stock_regions.determineRegionFromTicket(stockTicketString)

    def setDynamic(self, isDynamic):
        self.staticVersion = not isDynamic

    def update(self, newValue):
        if self.staticVersion:
            return
        oldStockValue = self.stockValue
        self.stockValue = newValue
        self.stockValueChange = self.stockValue - oldStockValue
        self.stockValueChangePercentage = (self.stockValueChange / oldStockValue) #TODO check if this is correct

            
    
    
