import sympy as sp
import numpy as np
from sympy import *
import os
x = sp.Symbol('X')
y = sp.Symbol('Y')
os.system('cls')

def replacer(entry):
    print("Enter X-value substitution")
    print('')
    number = input()
    lib = {'X':number}
    result = [lib['X'] if element == 'X' else element for element in entry]
    return result

print("Enter equation")
print('')
entry = input()
[*entry]
equation = [element for element in entry if element.strip()]
print('')
print("substitute number for X?")
print('')
answer = input()
if answer =='yes':
    print(replacer(equation))

