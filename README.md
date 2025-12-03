# AjayFirst-Demo
This is my first git Repo

import unittest
from testing import adding, divide

class TestAdding(unittest.TestCase):
    
    def test_adding_positive_integers(self):
        """Test adding two positive integers."""
        self.assertEqual(adding(4, 5), 9)
    
    def test_adding_negative_integers(self):
        """Test adding two negative integers."""
        self.assertEqual(adding(-3, -7), -10)
    
    def test_adding_mixed_signs(self):
        """Test adding positive and negative."""
        self.assertEqual(adding(-5, 10), 5)
    
    def test_adding_with_zero(self):
        """Test adding with zero."""
        self.assertEqual(adding(0, 5), 5)
        self.assertEqual(adding(5, 0), 5)
    
    def test_adding_floats(self):
        """Test adding floats."""
        self.assertAlmostEqual(adding(2.5, 3.5), 6.0)
    
    def test_adding_int_and_float(self):
        """Test adding int and float."""
        self.assertAlmostEqual(adding(4, 2.5), 6.5)

class TestDivide(unittest.TestCase):
    
    def test_divide_positive_integers(self):
        """Test dividing two positive integers."""
        self.assertEqual(divide(10, 2), 5.0)
    
    def test_divide_by_zero(self):
        """Test dividing by zero."""
        self.assertEqual(divide(10, 0), "Error: Cannot divide by zero")
    
    def test_divide_floats(self):
        """Test dividing floats."""
        self.assertAlmostEqual(divide(10.0, 2.5), 4.0)
    
    def test_divide_negative(self):
        """Test dividing negative numbers."""
        self.assertEqual(divide(-10, 2), -5.0)

if __name__ == '__main__':
    unittest.main()
