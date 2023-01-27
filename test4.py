import sympy as sp
import numpy as np
from sympy import *
import os
x = sp.Symbol('X')
y = sp.Symbol('Y')
os.system('cls')

print("Enter equation")
print("")
equation = input()

def solver(function,variable):
    answer = sp.diff(function,variable)
    return answer

def variable_finder(entry):
    for element in entry:
        if element == 'X':
            variable = x
            return variable
        elif element == 'Y':
            variable = y
            return variable



def address_maker(entry):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    variables = ['X','Y']
    operators = ['+','-','/','*','%']
    symbol_list = ['^']
    
    everything_counter = 0
    number_counter = 0
    operator_counter = 0
    variable_counter = 0
    symbol_counter = 0
    for element in entry:
        everything_counter += 1
        if element in numbers:
            number_counter += 1
        if element in symbol_list:
            symbol_counter += 1
        if element in variables:
            variable_counter += 1
        if element in operators:
            operator_counter += 1
    return everything_counter, number_counter, variable_counter, symbol_counter, operator_counter

def indexer(entry):
    addresses = address_maker(entry)
    for element in entry:
        wawa

def compiler(entry):
    addresses = address_maker(entry)
    variable = variable_finder(entry)
    
    return addresses, variable
    

print(compiler(equation))