# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Lewis
# Section:      521
# Assignment:   Lab 3b
# Date:         17 09 2021

from math import *

area = float(input("Please enter the area: "))

# Calculates the radius of a circle given area
def circle(A):
    print("A circle with area {:.2f} has a radius {:.3f}".format(area, sqrt(A/pi)))

# Calculates the side length of an equilateral triangle given area
def triangle(A):
    print("An equilateral triangle with area {:.2f} has a side {:.3f}".format(area, sqrt(4*A/sqrt(3))))

# Calculates the side length of a square given area
def square(A):
    print("A square with area {:.2f} has a side {:.3f}".format(area, sqrt(A)))

# Calculates the side length of a pentagon given area
def pentagon(A):
    print("A pentagon with area {:.2f} has a side {:.3f}".format(area, sqrt(4*A/(sqrt(25+10*sqrt(5))))))

# Calculates the side length of a dodecagon given area
def dodecagon(A):
    print("A dodecagon with area {:.2f} has a side {:.3f}".format(area, sqrt(A/(6+3*sqrt(3)))))    
    
circle(area)
triangle(area)
square(area)
pentagon(area)
dodecagon(area)
    