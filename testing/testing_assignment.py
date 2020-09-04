
'''Algorithm
1. importing unittest
2. making class Test_learners with variable unittest.TestCase
3. unittesting of the code is done to find whether it is right or it needs any changes
'''
import unittest
from back_end.connection import *
import front_end.image
from model.model_class import *

class Test_computer(unittest.TestCase):
    def setUp(self):
        self.s=Student(1000,"Saumya Lohani","Dillibazaar","2001-04-06","Female","9876543210","saumya@gmail.com")
        self.con=DbConnection()
        pass
    def test_get_ID(self):
        self.assertEqual(1000,self.s.get_ID())
    def test_get_Name(self):
        self.assertEqual("Saumya Lohani",self.s.get_Name())
    def test_set_ID(self):
        self.s.set_ID(1001)
        self.assertEqual(1001,self.s.get_ID())
    def test_set_Name(self):
        self.s.set_Name("Manisha Thapa")
        self.assertEqual("Manisha Thapa",self.s.get_Name())
    def test_get_Residence(self):
        self.assertEqual("Dillibazaar", self.s.get_Residence())
    def test_get_DOB(self):
        self.assertEqual("2001-04-06", self.s.get_DOB())
    def test_set_Residence(self):
        self.s.set_Residence("Banepa")
        self.assertEqual("Banepa", self.s.get_Residence())
    def test_set_DOB(self):
        self.s.set_DOB("1999-11-08")
        self.assertEqual("1999-11-08", self.s.get_DOB())
    def test_insert(self):
        query='insert into computer values(%s,%s,%s,%s,%s,%s,%s);'
        values=(1003,"Horizon Thapa","Shankhu","2002-02-14","Male","9808438657","horizon@gmail.com")
        self.con.insert(query,values)
        query='select * from computer where ID=%s;'
        values=(1003,)
        actual=self.con.search(query,values)
        expect=[(1003,"Horizon Thapa","Shankhu","2002-02-14","Male","9808438657","horizon@gmail.com"),]
        self.assertEqual(actual,expect)
    def test_delete(self):
        query='delete from computer where ID=%s;'
        values=(1002,)
        self.con.insert(query,values)
        query='select * from computer where ID=%s;'
        values=(1002,)
        actual=self.con.search(query,values)
        expect=[]
        self.assertEqual(actual,expect)
    def test_update(self):
        query = 'update computer set Name=%s,Residence=%s,DOB=%s,Gender=%s,Contact=%s,Email=%s where ID=%s;'
        values = ("Yangchen Lama","Bouddha","21-11-1999","Female","9856347823","yamgchen@hotmail.com",1000)
        self.con.insert(query, values)
        query = 'select * from computer where ID=%s;'
        values = (1000,)
        actual = self.con.search(query, values)
        expect = [(1000,"Yangchen Lama","Bouddha","21-11-1999","Female","9856347823","yamgchen@hotmail.com")]
        self.assertEqual(actual, expect)
    def test_linear_search(self):
        records=["Saumya Lohani","Shiksha Kandel"]
        Name="Saumya Lohani"
        self.assertTrue(front_end.image.linear_search(records,Name))

    def tearDown(self):
        self.s = None
        self.con = None
if __name__ == "__main__":
    unittest.main()