import unittest
from triangle_classifier import classify_triangle
import math


class TestTriangleClassification(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(6, 6, 6), "Equilateral triangle")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(7, 7, 10), "Isosceles triangle")

    def test_scalene(self):
        self.assertEqual(classify_triangle(9, 12, 15), "Scalene triangle and Right triangle")  # Updated

    def test_right_scalene(self):
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene triangle and Right triangle")

    def test_right_isosceles(self):
        self.assertEqual(classify_triangle(2, 2, math.sqrt(8)), "Isosceles triangle and Right triangle")

    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(2, 2, 5), "Not a triangle")
        self.assertEqual(classify_triangle(3, 4, 8), "Not a triangle")

    def test_zero_length(self):
        self.assertEqual(classify_triangle(0, 4, 5), "Not a triangle")
        self.assertEqual(classify_triangle(1, 0, 3), "Not a triangle")

    def test_negative_length(self):
        self.assertEqual(classify_triangle(-3, 4, 5), "Not a triangle")


if __name__ == "__main__":
    unittest.main()
