# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
from model import PersonInformation 
from model import AddressInformation
from addressbook import AddressBook
from model import Person

class  Test(unittest.TestCase):
    #def setUp(self):
    #    self.foo = PersonInformation()
    #

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def test_PersonInformation(self):
        #assert x != y;
        #self.assertEqual(x, y, "Msg");
        pi1 = PersonInformation("JOHN","DOE")
        assert pi1.getFirstName()=="JOHN"
        assert pi1.getLastName() =="DOE"
        pi1.setFirstName("Jane")
        pi1.setLastName("Fonda")
        assert pi1.getFirstName()=="Jane"
        assert pi1.getLastName() =="Fonda"
        
        # self.fail("TODO: Write test")
    
    def test_AddressInformation(self):
        ai1 = AddressInformation ("last street")
        assert ai1.getStreetAddress()=="last street"
        ai1.setStreetAddress("first street")
        assert ai1.getStreetAddress() == "first street"
    
    def test_AddressBook(self):
        ab=AddressBook()
        pi1 = PersonInformation("JOHN","DOE")
        p1 = Person(pi1)
        print ("Person:"+str(p1.getPersonID()))
        p1.addEmail("test1@gmail.com")
        p1.addEmail("test2@gmail.com")
        p1.addAddress("1234 north")
        p1.addAddress("1234 north 2")
        p1.addPhone("455 555 5551")
        p1.addPhone("455 555 5552")
        p1.addGroup(1)
        p1.addGroup(2)
        ab.addPerson(p1)
        pi2 = PersonInformation("JANE","TARZAN")
        p2 = Person (pi2)
        p2.addEmail("JANE1@gmail.com")
        p2.addEmail("test2@gmail.com")
        p2.addAddress("1234 north 3")
        p2.addAddress("1234 north 2")
        p2.addPhone("455 555 5553")
        p2.addPhone("455 555 5552")
        p2.addGroup(1)
        p2.addGroup(3)
        ab.addPerson(p2)
        ab.addPersonToGroup(p2,[2])
        print("result:")
        
        members = ab.getGroupMembers(2)
        print("members:")
        print(len(members))
        #print(members)
        print(members[0].getFirstName())
        print(members[0].getLastName())
        assert len(members)==1
        members = ab.getGroupMembers(1)
        print("members group1 :")
        print(len(members))
        assert len(members)==2
        print(members[1].getFirstName())
        print(members[1].getLastName())
        
if __name__ == '__main__':
    unittest.main()

