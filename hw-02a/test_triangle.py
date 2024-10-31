"""
Unit tests for the classify_triangle function.
"""

import unittest

from triangle import classify_triangle

class TestTriangle(unittest.TestCase):
    """Test cases for triangle classification."""

    def test_right_triangle_a(self):
        """Test case for a right triangle with sides 3, 4, 5."""
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        """Test case for a right triangle with sides 5, 3, 4."""
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def test_equilateral_triangles(self):
        """Test case for an equilateral triangle with sides 1, 1, 1."""
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def test_isoceles_triangles(self):
        """Test case for an isoceles triangle with sides 4, 4, 5."""
        self.assertEqual(classify_triangle(4,4,5),'Isoceles','4,4,5 is an Isoceles triangle')

    def test_scalene_triangles(self):
        """Test case for a scalene triangle with sides 3, 4, 6."""
        self.assertEqual(classify_triangle(3,4,6),'Scalene','3,4,6 is a Scalene triangle')

    def test_not_a_triangle(self):
        """Test case for values that do not form a triangle, like sides 1, 2, 4."""
        self.assertEqual(classify_triangle(1,2,4),'NotATriangle','1,2,4 is not a triangle')

    def test_invalid_input(self):
        """Test case for invalid input with a negative side."""
        self.assertEqual(classify_triangle(-1,2,3),'InvalidInput','-1 is invalid')

    def test_non_integer_input(self):
        """Test case for non-integer input, such as a float."""
        self.assertEqual(classify_triangle(1.5,2,3),'InvalidInput','1.5 is invalid')

    def test_large_input(self):
        """Test case for input that exceeds the valid range."""
        self.assertEqual(classify_triangle(201,2,3),'InvalidInput','201 is invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
