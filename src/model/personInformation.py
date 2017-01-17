

class PersonInformation (object):
    def __init__ (self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def setFirstName(self, first):
        self.firstName = first
    
    def getFirstName (self):
        return self.firstName
    
    def setLastName (self, last):
        self.lastName = last
    
    def getLastName (self):
        return self.lastName
        