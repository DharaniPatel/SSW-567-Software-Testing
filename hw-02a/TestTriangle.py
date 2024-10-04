import unittest

from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsocelesTriangles(self): 
        self.assertEqual(classifyTriangle(4,4,5),'Isoceles','4,4,5 is an Isoceles triangle')

    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(3,4,6),'Scalene','3,4,6 is a Scalene triangle')

    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(1,2,4),'NotATriangle','1,2,4 is not a triangle')

    def testInvalidInput(self): 
        self.assertEqual(classifyTriangle(-1,2,3),'InvalidInput','-1 is invalid')

    def testNonIntegerInput(self): 
        self.assertEqual(classifyTriangle(1.5,2,3),'InvalidInput','1.5 is invalid')

    def testLargeInput(self): 
        self.assertEqual(classifyTriangle(201,2,3),'InvalidInput','201 is invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()