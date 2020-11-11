
import unittest
import arithmetic

class Testarithmetic(unittest.TestCase):

    def test_add(self):
        try:
          self.assertEqual(arithmetic.add(2,3), 5)
          print("Addition pass for positive numbers")
          self.assertEqual(arithmetic.add(-2,-3), -5)
          print("Addition pass for negative numbers")
        except:
          print("Addition Fail")
    
    def test_subtract(self):
       try:
          self.assertEqual(arithmetic.subtract(5,3), 2)
          print("Subtraction pass for positive numbers")
          self.assertEqual(arithmetic.subtract(-2,-3), 1)
          print("Subtraction pass for negative numbers")
       except:
          print("Subtraction Fail")
    
    def test_multiply(self):
       try:
          self.assertEqual(arithmetic.multiply(2,3), 6)
          print("Multiplication pass for positive numbers")
          self.assertEqual(arithmetic.multiply(-2,-3), 6)
          print("Multiplication pass for negative numbers")
       except:
          print("Multiplication Fail")
    
    def test_divide(self):
       try:
          self.assertEqual(arithmetic.divide(6,3), 2)
          print("Division pass for positive numbers")
          self.assertEqual(arithmetic.multiply(-6,-3), 2)
          print("Division pass for negative numbers")
       except:
          print("Division Fail")
       try:
        divide(12,0)
       except:
        print("Error for div by zero")
    
    

if __name__ == '__main__':
    print("\nCases for addition")
    Testarithmetic().test_add()
    print("\nCases for subtraction")
    Testarithmetic().test_subtract()
    print("\nCases for multiplication")
    Testarithmetic().test_multiply()
    print("\nCases for division")
    Testarithmetic().test_divide()
    
