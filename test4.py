import sympy as sp
import math
import os
from sympy import *
import sys
x = sp.Symbol('X')
y = sp.Symbol('Y')
os.system('cls')

def percent_error():
    print("Input dimensions")
    print('')
    dimension1 = input("Dimension 1")
    dimension2 = input("Dimension 2")
    dimension3 = input("Dimension 3")
    
    volume = dimension1 * dimension2 * dimension3
    
    max_volume = (dimension1 + 0.5) * (dimension2 + 0.5) * (dimension3 + 0.5)
    min_volume = (dimension1 - 0.5) * (dimension2 - 0.5) * (dimension3 - 0.5)
    
    difference1 = volume - min_volume
    difference2 = max_volume - volume
    
    if difference2 > difference1:
        difference2 / volume
    else:
        