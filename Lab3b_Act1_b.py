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

# Wavelength Calculation
print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm): "))
angle = float(input("Please enter the angle (degrees): "))
print ("Wavelength is {:.4f}".format((2*distance)*sin(angle*(pi/180))), "nm")
