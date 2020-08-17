import unittest

def get_max(a,b):
    return a

class TestCase1(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_max(2,3),2) #Sử dụng assert để ktra

    def test2(self):
        self.assertEqual(get_max(3,2),3)

unittest.main()