#File for testing new things before bringing to the ACS file


#Tester for entire equation input instead of individual characters
import math
import os
from sympy import Symbol, symbols
from sympy.interactive import printing 
printing.init_printing(use_latex = True)
import sympy as sp
import numpy as np



os.system('cls')
x = sp.Symbol('X')

special_Characters = ['+','-','*','/','^','X','Y']

def dSolver(entrylist):
    for ele in entrylist:
        if ele not in special_Characters:
            modifiedlist = [int(ele) for ele in entrylist]
            output = [sp.diff(x**ele) for ele in modifiedlist]
            return output
        else:
            continue

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
"""
separated_list = sep_list_ops(res)
organized_list = sep_list_vars(separated_list)
answer = dSolver(organized_list)
"""
print(dSolver(res))