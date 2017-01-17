
from model import AddressInformation
from model import PersonInformation
from model import Person
class AddressBook (object):
    def __init__ (self):
        self.People = {}
        self.Addresses = {}
        self.Phones = {}
        self.Emails = {}
        self.Groups ={}
        self.MaxPersonID=0
        
    def createPerson(self, person):
        person.setPersonID(self.MaxPersonID+1)
        self.MaxPersonID=+1
         
    def addPerson(self, p):
        if p not in self.People:
            self.createPerson(p)
            self.registerPerson(p)
            self.registerEmails(p.getEmails(), p.getPersonID())
            self.registerAddresses(p.getAddresses(), p.getPersonID())
            self.registerPhones(p.getPhones(), p.getPersonID())
            self.registerGroups(p.getGroups(), p.getPersonID())
                
    def addPersonToGroup(self, person, groups):
        self.registerGroups(groups, person.getPersonID )
        print("Groups")
        print(person.getGroups())
        
    def registerPerson(self, person):
        key = person.getFirstName()+person.getLastName()
        self.People[key]=person
        print("registerPerson:")
        print(self.People)
        
    def registerEmails(self, emails, personID):
        currentList=list()
        for e in emails:
            print ("e:"+e)
            currentList = self.Emails.setdefault(e, list())
            print currentList
            if e not in currentList:
                currentList.append(personID)
        print self.Emails
    
    def registerAddresses(self, addresses, personID):
        currentList=list()
        for addr in addresses:
            print ("addr:"+addr)
            currentList = self.Addresses.setdefault(addr, list())
            print currentList
            if addr not in currentList:
                currentList.append(personID)
        print self.Addresses
    
    def registerPhones(self, phones, personID):
        currentList=list()
        for phone in phones:
            print ("phone:"+phone)
            currentList = self.Phones.setdefault(phone, list())
            print currentList
            if phone not in currentList:
                currentList.append(personID)
        print self.Phones
        
    def registerGroups(self, groups, personID):
        currentList=list()
        for group in groups:
            print ("group:")
            print(group)
            currentList = self.Groups.setdefault(group, list())
            print currentList
            if group not in currentList:
                currentList.append(personID)
        print self.Phones
        