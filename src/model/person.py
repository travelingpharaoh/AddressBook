class Person(object):
    def __init__ (self, personInformation):
        self.personInformation = personInformation;
        self.addresses = []
        self.emails = []
        self.groups = []
        self.personID=0
        self.phones = []
    
    def addAddress(self, addInfo):
        self.addresses.append(addInfo)
    
    def addEmail(self, email):
        print (email)
        self.emails.append(email)
        print self.emails
        
    def addGroup(self, group):
        self.groups.append(group)
    
    def addPhone (self,phone ):
        self.phones.append(phone)
    
    def getPersonID (self):
        return self.personID
    
    def setPersonID (self, id):
        self.personID = id
        
    def getEmails(self):
        return self.emails
    
    def getAddresses(self):
        return self.addresses
    
    def getGroups(self):
        return self.groups
    
    def getPhones(self):
        return self.phones
    
    def getFirstName(self):
        return self.personInformation.getFirstName()
        
    def getLastName(self):
        return self.personInformation.getLastName()
    
    
        