import sympy as sp
import numpy as np
from sympy import *
import os
x = sp.Symbol('X')
y = sp.Symbol('Y')
os.system('cls')

print("Enter equation")
print("")
entry = str(input())

print(sp.diff(entry))