#File for testing new things before bringing to the ACS file


#Tester for entire equation input instead of individual characters
import os
import sympy as sp

os.system('cls')
print("Enter equation")
print("")
inp1 = int(input())
"""
[*inp1]
#Sample equation: 5X^2 + 13X + 2
res = [ele for ele in inp1 if ele.strip()]

print(res)
"""

x = sp.Symbol('X')

print(sp.diff(x**inp1))