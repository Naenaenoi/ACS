import sympy as sp
import math
import os
from sympy import *
import sys
x = sp.Symbol('X')
y = sp.Symbol('Y')
os.system('cls')

def percent_error():
    def type_1():
        print("Input dimensions")
        print('')
        dimension1 = float(input("Dimension 1: "))
        dimension2 = float(input("Dimension 2: "))      

        volume = dimension1 * dimension2  

        max_volume = (dimension1 + 0.5) * (dimension2 + 0.5)
        min_volume = (dimension1 - 0.5) * (dimension2 - 0.5)

        difference1 = volume - min_volume
        difference2 = max_volume - volume

        if difference2 > difference1:
            answer = difference2 / volume
        else:
            answer = difference1 / volume

        print(answer * 100)

    def type_2():
        print("Input dimensions")
        print('')
        dimension1 = float(input("Dimension 1: "))
        dimension2 = float(input("Dimension 2: "))
        dimension3 = float(input("Dimension 3: "))
        
        volume = dimension1 * dimension2 * dimension3
        print(volume)

        max_volume = (dimension1 + 0.5) * (dimension2 + 0.5) * (dimension3 + 0.5)
        min_volume = (dimension1 - 0.5) * (dimension2 - 0.5) * (dimension3 - 0.5)
        print(max_volume, min_volume)

        difference1 = volume - min_volume
        difference2 = max_volume - volume
        
        if difference2 > difference1:
            answer = difference2 / volume
        else:
            answer = difference1 / volume

        print(answer * 100)

    print("Number of dimensions")
    print('')
    selector = input()
    if selector == '2':
        type_1()
    elif selector == '3':
        type_2()

        

percent_error()