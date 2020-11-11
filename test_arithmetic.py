#Siddhika Bejekar
#MIS : 111803136

import unittest
import arithmetic

class Testarithmetic(unittest.TestCase):
    #addition
    def test_add(self): 
        self.assertEqual(arithmetic.add(2,3), 5)
        print("Addition pass for both positive integers")
        
        self.assertEqual(arithmetic.add(-9,-7), -16)
        print("Addition pass for both negative integers")
        
        self.assertEqual(arithmetic.add(4.25, 2.25), 6.50)
        print("Addition pass for float numbers")
        
        self.assertEqual(arithmetic.add(9, -12), -3)
        print("Addition pass for one positive one negative integer")
        
        self.assertEqual(arithmetic.add(9,0), 9)
        print("Addition of any number with 0 is the number itself")
   
   
    #subtraction    
    def test_subtract(self):
       self.assertEqual(arithmetic.subtract(5,3), 2)
       print("Subtraction pass for both positive integers")
       
       self.assertEqual(arithmetic.subtract(-5,-3), -2)
       print("Subtraction pass for both negative integers")
       
       self.assertEqual(arithmetic.subtract(-5, 3), -8)
       print("Subtraction pass for one positive one negative integer")
       
       self.assertEqual(arithmetic.subtract(4.25, 2.25), 2)
       print("Subtraction pass for float numbers")
       
       self.assertEqual(arithmetic.subtract(5,0), 5)
       print("Subtraction for any number-0 = number ")
   
   
    #multiplication 
    def test_multiply(self):
       self.assertEqual(arithmetic.multiply(2,3), 6)
       print("Multiplication pass for both positive integers")
     
       self.assertEqual(arithmetic.multiply(-2,-3), 6)
       print("Multiplication pass for both negative integers")
       
       self.assertEqual(arithmetic.multiply(2,-3), -6)
       print("Multiplication pass one positive and one negative integer")
       
       self.assertEqual(arithmetic.multiply(2.5,3.5), 8.75)
       print("Multiplication pass for float numbers")
       
       self.assertEqual(arithmetic.multiply(7, 1), 7)
       print("Multiplication of a number with 1 is the number itself")
       
       self.assertEqual(arithmetic.multiply(8,0), 0)
       print("Multiplication of any number with 0 is 0")
  
  
    #division
    def test_divide(self):
       self.assertEqual(arithmetic.divide(12,3), 4)
       print("Division pass for both positive numbers")
       
       self.assertEqual(arithmetic.divide(-12,-3), 4)
       print("Division pass for both negative integers")
       
       self.assertEqual(arithmetic.divide(-12,3), -4)
       print("Division pass for one positive one negative integers ")
    
       self.assertEqual(arithmetic.divide(0,9), 0)
       print("0 divided by any number outputs 0") 
       
       self.assertEqual(arithmetic.divide(8, 1), 8)
       print("Any number divided by '1' is the number itself")
       
       
       #division by 0
       try:
       	self.assertEqual(arithmetic.divide(45,0), 0)
       	print("0 divided by any number outputs 0")   
       except:
       	print("Error: Division by 0 is undefined")

if __name__ == '__main__':
	print("\nAddition operations:")
	Testarithmetic().test_add()
	print("\nSubtraction operations:")
	Testarithmetic().test_subtract()
	print("\nMultiplication operations:")
	Testarithmetic().test_multiply()
	print("\nDivision operations:")
	Testarithmetic().test_divide()
    
