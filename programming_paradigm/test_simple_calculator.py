import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for SimpleCalculator class."""

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        result = self.calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtraction(self):
        """Test the subtraction method."""
        result = self.calc.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        """Test the multiply method."""
        result = self.calc.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_divide(self):
        """Test the divide method."""
        result = self.calc.divide(10, 5)
        self.assertEqual(result, 2)

        # Also test division by zero
        result = self.calc.divide(10, 0)
        self.assertEqual(result, "Error: Cannot divide by zero")

if __name__ == "__main__":
    unittest.main()

