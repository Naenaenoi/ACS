import sympy as sp
from sympy import *
import os
x = sp.Symbol('X')
y = sp.Symbol('Y')
os.system('cls')

variables = ['^']

def group(entry):
    sublist = []
    counter = 0
    for element in entry:
        counter += 1
        for element in variables:
            counter -= 1
            
            
            
        

dict1 = {
    '^':'**'
}

print("Enter equation")
print("")
equation = input()
[*equation]

stripped_equation = [ele for ele in equation if ele.strip()]

print(stripped_equation)