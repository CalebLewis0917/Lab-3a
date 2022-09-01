# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Lewis
# Section:      521
# Assignment:   Lab 3b
# Date:         17 09 2021

# kPa Calculation
print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
volume = float(input("Please enter the volume (m^3): "))
temp = float(input("Please enter the temperature (K): "))
gConstant = .008314 # m^3kPa/K*mol
print ("Pressure is {:.0f}".format(moles*gConstant*temp/volume), "kPa")