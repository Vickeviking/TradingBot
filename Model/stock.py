from resources.stock_enums import stock_tickets
from resources.stock_enums import stock_regions

#bought stocks are static, ones in live view are dynamic
class stock:
    def __init__(self,staticVersion = False, stockTicket = "", stockValue = 0, stockValueChange = 0, stockValueChangePercentage = 0, region = None):
        self.staticVersion = staticVersion
        self.stockTicket = stockTicket
        self.stockType = None
        self.stockValueChange = stockValueChange
        self.stockValueChangePercentage = stockValueChangePercentage
        self.region = region
        #set stock type and region
        self.stockType = stock_tickets.determineTypeFromTicket(stockTicket)
        self.region = stock_regions.determineRegionFromTicket(stockTicket)
        self.stockName = stock_tickets.determineNameFromTicket(stockTicket)
        self.last10StockValues = []
        self.stockValue = stockValue




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

    def update10StockValues(self): # updates once per second
        if self.stockValue == 0:
            return
        # check if array full
        if len(self.last10StockValues) >= 10:
            self.last10StockValues.pop(0)
        # add new value
        self.last10StockValues.append(self.stockValue)
        

            
    
    
