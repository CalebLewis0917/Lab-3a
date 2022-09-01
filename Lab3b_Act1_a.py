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

# Force Calculation
print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg): "))
accel = float(input("Please enter the acceleration (m/s^2): "))
force = float(mass*accel)
print ("Force is {:.1f}".format(force), "N")
