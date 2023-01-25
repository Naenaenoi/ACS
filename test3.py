import sympy as sp
from sympy import *
import os
x = sp.Symbol('X')
y = sp.Symbol('Y')
os.system('cls')

# Intended flow: Equation is entered, equation is iterated through until the program encounters
# a number, the number in front of the variable is considered an element and passed to the element
# variable, the program continues until it encounters a carrot symbol, the area after 
# the carrot symbol and before the next + or - sign is then considered an exponent, the area
# between the beginning of the equation and the exponent is considered a term and is passed to the 
# term variable. All of this is done while the elements in the equation list are removed from the
# list in order to work with the sp.diff() function.

exponent = {'^':'**'}

print("Enter equation")
print("")
equation = input()
[*equation]

def intmaker(entry):
    for element in entry:
        intlist = [int(element)]
        return intlist

def intterpreter(entry):
    try:
        for element in entry:
            intlist = [int(element)]
    except:
        error = True
        skip = False
        for element in entry:
            if error == True:
                skip = True
                continue
            if skip:
                skip = False
                intmaker(entry)
        return intlist
            

print(intterpreter(equation))
"""
def dSolver(function,variable):
    answer = sp.diff(function,variable)
    return answer

element1 = 6
exponent = 3

term = element1*x**exponent

print(dSolver(term,x))



print("Enter equation")
print("")
equation = input()
[*equation]

stripped_equation = [ele for ele in equation if ele.strip()]
"""