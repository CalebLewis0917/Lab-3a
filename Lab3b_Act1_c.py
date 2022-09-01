# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Lewis
# Section:      521
# Assignment:   Lab 3b
# Date:         17 09 2021

# Mass Calculation
print("This program calculates how much Radon-222 is left given time and initial amount")
time = float(input("Please enter the time (days): "))
initialM = float(input("Please enter the initial amount (g): "))
#half_life = float(input("Please enter the half-life (days): "))
print ("Radon-222 left is {:.2f}".format(initialM*(2**(-time/3.8))), "g")