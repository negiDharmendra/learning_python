import unittest
from basic_learning import *

class numberMathematics(unittest.TestCase):
    def test_getFactorial_of_4(self):
        self.assertEqual(getFactorial(4),24)
    def test_getFactorial_of_6(self):
        self.assertEqual(getFactorial(6),720)
    def test_getFactorial_of_10(self):
        self.assertEqual(getFactorial(10),3628800)
    def test_sumOfFirstNnumber_10(self):
    	self.assertEqual(sumOfFirstNnumber(10),55)


    def test_getFibonacci_of_4(self):
        self.assertEqual(getFibonacci(4),2)
    def test_getFibonacci_of_8(self):
        self.assertEqual(getFibonacci(8),13)
    def test_getFibonacci_of_11(self):
        self.assertEqual(getFibonacci(11),55)


class array(unittest.TestCase):
    def test_getFibonacciSeries_of_8(self):
        self.assertEqual(getFibonacciSeries(8),[0,1,1,2,3,5,8,13])
    def test_getFibonacciSeries_of_13(self):
        self.assertEqual(getFibonacciSeries(13),[0,1,1,2,3,5,8,13,21,34,55,89,144])

class string(unittest.TestCase):
	def test_rot_13_mno(self):
		self.assertEqual(rotN('mno',13),'zab')
	def test_rot_16_mno(self):
		self.assertEqual(rotN('mno',16),'cde')
	def test_rot_25_a(self):
		self.assertEqual(rotN("hellohowaryou",25),"gdkkngnvzqxnt")

if __name__ == '__main__':
    unittest.main()
