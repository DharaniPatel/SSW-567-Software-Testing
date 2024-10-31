"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(side_a,side_b,side_c):
    """
        Classifies a triangle based on the lengths of its sides.
        
        Parameters:
        a (int): Length of the first side.
        b (int): Length of the second side.
        c (int): Length of the third side.

        Returns:
        str: Type of the triangle ('Equilateral', 'Isoceles', 'Scalene', 'Right', 'NotATriangle', 
        or 'InvalidInput').
        """
        # pylint: disable=too-many-return-statements

    # require that the input values be >= 0 and <= 200
    if side_a > 200 or side_b > 200 or side_c > 200:
        return 'InvalidInput'
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return 'InvalidInput'
    if not(isinstance(side_a,int) and isinstance(side_b,int) and isinstance(side_c,int)):
        return 'InvalidInput'

    if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
        return 'NotATriangle'

    if side_a == side_b and side_b == side_c:
        return 'Equilateral'
    if (side_a**2 + side_b**2 == side_c**2) or \
        (side_a**2 + side_c**2 == side_b**2) or \
        (side_b**2 + side_c**2 == side_a**2):
        return 'Right'
    if (side_a == side_b) or (side_a == side_c) or (side_b == side_c):
        return 'Isoceles'
    return 'Scalene'
