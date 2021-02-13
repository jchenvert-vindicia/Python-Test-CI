from basic_math import base_math

import unittest


class TestBaseMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(base_math.add(2,5), 7, "Should be 7")


    def test_subtract(self):
        self.assertEqual(base_math.subtract(5, 2), 3, "Should be 3")
    
    
    def test_multiply(self):
        self.assertEqual(base_math.multiply(5, 2), 10, "Should be 10")
    
    
    def test_divide(self):
        self.assertEqual(base_math.divide(10, 5), 2, "Should be 2")
    
    
    def test_failing_add(self):
        self.assertEqual(base_math.add(4, 4), 8, "Should be 8")


def main():
    unittest.main()


if __name__ == "__main__":
    main()

