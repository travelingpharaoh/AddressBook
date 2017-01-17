#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from model import PersonInformation 
from model import AddressInformation
from addressbook import AddressBook
from model import Person

if __name__ == "__main__":
    ab=AddressBook()
    pi1 = PersonInformation("JOHN","DOE")
    p1 = Person(pi1)
    ab.createPerson(p1)
    print ("Person:"+str(p1.getPersonID()))
    p1.addEmail("test1@gmail.com")
    p1.addEmail("test2@gmail.com")
    ab.registerEmail(p1.getEmails(), p1.getPersonID())
    p1.addAddress("1234 north")
    p1.addAddress("1234 north 2")
    p1.addPhone("455 555 5551")
    p1.addPhone("455 555 5552")
    ab.registerAddress(p1.getAddresses(), p1.getPersonID())
    pi2 = PersonInformation("JANE","TARZAN")
    p2 = Person (pi2)
    p2.addEmail("JANE1@gmail.com")
    p1.addEmail("test2@gmail.com")
    ab.registerEmail(p2.getEmails(), p2.getPersonID())
    p1.addAddress("1234 north 3")
    p1.addAddress("1234 north 2")
    p1.addPhone("455 555 5553")
    p1.addPhone("455 555 5552")
    ab.registerAddress(p2.getAddresses(), p2.getPersonID())