import sympy as sp
import numpy as np
from sympy import *
import os
x = sp.Symbol('X')
y = sp.Symbol('Y')
os.system('cls')

def derivative_environment():
    print("Enter equation")
    print("")
    entry = input()
    [*entry]
    equation = [element for element in entry if element.strip()]

    def solver(function,var):
        answer = sp.diff(function,var)
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

    #separator created by Deacon Tait, I modified it. This program would not work without it.
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


    def intmaker(entry):
        ints = ""
        chars = ['*','X','**']
        for element in entry:
            if element in chars:
                continue
            else:
                ints = int(element)
        return ints

        
    def compiler(entry):
        iterations = 0
        exp = {'^':'**'}
        variables = {'X':'*X'}
        var = variable_finder(entry)
        separated_lists = separator(equation)
        addresses = address_maker(separated_lists[0])
        exponent = addresses[0] - addresses[3] -1

        result = []
        for i in separated_lists:
            if i[0] == '+' or i[0] == '-':
                continue
            else:
                list_term_1 = [exp['^'] if element == '^' else element for element in i]
                list_term_2 = [variables['X'] if element == 'X' else element for element in list_term_1]
                term = list_annihilator(list_term_2)
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
    print(compiler(equation))