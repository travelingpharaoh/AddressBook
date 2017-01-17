
class AddressInformation(object):
    def __init__ (self, street):
        self.streetAddress=street
        
    def setStreetAddress(self, street):
        self.streetAddress = street;
    
    def getStreetAddress(self):
        return self.streetAddress
        