import unittest
from Calculator import Calculator

class Tests(unittest.TestCase):

    def test_calculator(self):

        self.assertEqual(Calculator.add(1,0),0)
        self.assertEqual(Calculator.add(1,1),2)
        self.assertEqual(Calculator.add(1.5,1.5),3)

if __name__=='__main__':
    unittest.main()
