#File for testing new things before bringing to the ACS file


#Tester for entire equation input instead of individual characters
import math
import os
from sympy.interactive import printing 
printing.init_printing(use_latex = True)
import sympy as sp
import numpy as np



os.system('cls')

def dSolver(inputList):
    for element in inputList:
        output = sp.diff(inputList)
        return output

operators = ['+','-','*','/','^']

def sep_list_ops(expression):
    sublists = []
    current_sublist = []
    for element in expression:
        if element in operators:
            sublists.append(current_sublist)
            current_sublist = []
            sublists.append([element])
        else:
            current_sublist.append(element)
    sublists.append(current_sublist)
    return sublists

variables = ['X','Y']

def sep_list_vars(expression):
    sublists = []
    current_sublist = []
    for element in expression:
        if element in variables:
            sublists.append(current_sublist)
            current_sublist = []
            sublists.append([element])
        else:
            current_sublist.append(element)
    sublists.append(current_sublist)
    return sublists

#Sample equation: 5X^2 + 13X + 2
print("Enter equation")
print("")
inp1 = input()
[*inp1]

res = [ele for ele in inp1 if ele.strip()]

separated_list = sep_list_ops(res)
organized_list = sep_list_vars(separated_list)
answer = dSolver(organized_list)

print(answer)


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ops = [ '+','-','=','/','*']
var = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        


"""

x = sp.Symbol('X')

print(sp.diff(x**inp1))


 
x = sp.symbols('x') 
I = sp.Integral(x**2,(x,0,1)) 
v = I.doit() 
print(latex(I),=,latex(v)) 
"""