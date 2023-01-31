import sympy as sp
import numpy as np
from sympy import *
import os
x = sp.Symbol('X')
y = sp.Symbol('Y')
os.system('cls')

def integral_environment():
    os.system('cls')
    print("Enter equation")
    print("")
    entry = input()
    [*entry]
    equation = [element for element in entry if element.strip()]

    def solver(function,var):
            answer = sp.integrate(function,var)
            return answer
    
    def variable_finder(entry):
            for element in entry:
                if element == 'X':
                    variable = x
                    return variable
                elif element == 'Y':
                    variable = y
                    return variable
    
    def separator(entry):
        operators = ['+','-','*','/']
        sublists = []
        current_sublist = []
        for element in entry:
            if element in operators:
                sublists.append(current_sublist)
                current_sublist = []
                sublists.append([element])
            else:
                current_sublist.append(element)
        sublists.append(current_sublist)
        return sublists
    
    def list_annihilator(entry):
        stringy = ""
        for element in entry:
            stringy += element
        return stringy
    
    def compiler(entry):
        exp = {'^':'**'}
        variables = {'X':'*X'}
        var = variable_finder(entry)
        separated_lists = separator(equation)

        result = []
        for i in separated_lists:
            if i[0] == '+' or i[0] == '-':
                continue
            else:
                list_term_1 = [exp['^'] if element == '^' else element for element in i]
                term = list_annihilator(list_term_1)
                result.append(solver(term, var))
        
        final_ret = ""
        for i in result:
            final_ret = final_ret + str(i)
            for z in separated_lists:
                if z[0] == '+' or z[0] == '-':
                    final_ret = final_ret + z[0]
                    separated_lists.remove(z)
                    break
                else:
                    continue
        return final_ret
    init_printing(use_unicode=False, wrap_line=False)
    print('')
    print(compiler(equation))
    print('')
    
integral_environment()