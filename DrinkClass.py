class drink:
    def __init__(self, drinkID, name, price):
        self.id = drinkID
        self.name = name
        self.price = price
    
    def getID(self):
        return self.drinkID

    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
    
