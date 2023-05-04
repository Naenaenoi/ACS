import math
from scipy.stats import binom
import matplotlib.pyplot as plt
from numpy import random
import sympy as sp
import numpy as np
from sympy import *
import os
import sys
x = sp.Symbol('X')
y = sp.Symbol('Y')
os.system('cls')

#Subscript & Superscript libraries
dict1 = {'0':'\u2070',
         '1':'\u00b9',
         '2':'\u00b2',
         '3':'\u00b3',
         '4':'\u2074',
         '5':'\u2075',
         '6':'\u2076',
         '7':'\u2077',
         '8':'\u2078',
         '9':'\u2079',
         '+':'\u207A',
         '-':'\u207B',
         '=':'\u207C',
         '(':'\u207D',
         ')':'\u207E',
         'n':'\u2084',}

dict2 = {'0':'\u2080',
         '1':'\u2081',
         '2':'\u2082',
         '3':'\u2083',
         '4':'\u2084',
         '5':'\u2085',
         '6':'\u2086',
         '7':'\u2087',
         '8':'\u2088',
         '9':'\u2089',
         '+':'\u208A',
         '-':'\u208B',
         '=':'\u208C',
         '(':'\u208D',
         ')':'\u208E',
         'a':'\u2090',
         'e':'\u2091',
         'o':'\u2092',
         'x':'\u2093',
         'h':'\u2095',
         'k':'\u2096',
         'l':'\u2097',
         'm':'\u2098',
         'n':'\u2099',
         'p':'\u209A',
         's':'\u209B',
         't':'\u209C'}

def sups(base,x):
    z = '{}'.format(dict1.get(x))
    return base + z

def subs(base,x):
    z = '{}'.format(dict2.get(x))
    return base + z

def derivative_environment():
    os.system('cls')
    print("Enter equation")
    print("")
    entry = input()
    [*entry]
    Up_equation = [element.upper() for element in entry]
    equation = [element for element in Up_equation if element.strip()]

    def solver(function,var):
        answer = sp.diff(function,)
        return answer

    def variable_finder(entry):
        x_var = ['X','x']
        y_var = ['Y','y']
        for element in entry:
            if element in x_var:
                variable = x
                return variable
            elif element in y_var: 
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
        
    
        
        #result = sups(base,value)
        #return result
        
    def compiler(entry):
        exp = {'^':'**'}
        variables = {'X':'*X'}
        reverse_variables = {'*X':'X'}
        var = variable_finder(entry)
        separated_lists = separator(equation)

        result = []
        for i in separated_lists:
            if i[0] == '+' or i[0] == '-':
                continue
            else:
                list_term_1 = [exp['^'] if element == '^' else element for element in i]
                list_term_2 = [variables['X'] if element == 'X' else element for element in list_term_1]
                term = list_annihilator(list_term_2)
                try:
                    result.append(solver(term, var))
                except :
                    list_term_3 = [reverse_variables['*X'] if element == '*X' else element for element in list_term_2]
                    term = list_annihilator(list_term_3)
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
    

            
    
    print('')
    print(compiler(equation))
    print('')
    print("1: Main Menu")
    print("2: enter another equation")
    print("exit: close ACS")
    print('')
    selector = input()

    if selector == '1':
        mainMenu()
    elif selector == '2':
        derivative_environment()
    elif selector == 'exit':
        sys.exit()
    
def integral_environment():
    os.system('cls')
    print("Enter equation")
    print("")
    entry = input()
    [*entry]
    Up_equation = [element.upper() for element in entry]
    equation = [element for element in Up_equation if element.strip()]

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
    
    def compiler(entry):
        exp = {'^':'**'}
        variables = {'X':'*X'}
        reverse_variables = {'*X':'X'}
        var = variable_finder(entry)
        separated_lists = separator(equation)

        result = []
        for i in separated_lists:
            if i[0] == '+' or i[0] == '-':
                continue
            else:
                list_term_1 = [exp['^'] if element == '^' else element for element in i]
                list_term_2 = [variables['X'] if element == 'X' else element for element in list_term_1]
                term = list_annihilator(list_term_2)
                try:
                    result.append(solver(term, var))
                except ValueError:
                    list_term_3 = [reverse_variables['*X'] if element == '*X' else element for element in list_term_2]
                    term = list_annihilator(list_term_3)
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
        res = final_ret + '+ C'
        return res
    
    
    
    print('')
    print(compiler(equation))
    print('')
    print("1: Main Menu")
    print("2: enter another equation")
    print("exit: close ACS")
    print('')
    selector = input()

    if selector == '1':
        mainMenu()
    elif selector == '2':
        integral_environment()
    elif selector == 'exit':
        sys.exit()

def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        try:
            num, denom = frac_str.split('/')
        except ValueError:
            return None
        try:
            leading, num = num.split(' ')
        except ValueError:
            return float(num) / float(denom)        
        if float(leading) < 0:
            sign_mult = -1
        else:
            sign_mult = 1
        return float(leading) + sign_mult * (float(num) / float(denom))



        
def sequence_environment():
    def arithmetic():
        sequence = []
        print("Input target term")
        print('')
        target_term = int(input())
        
        for ele in range(2):
            ele = str(input("Enter term " + str(ele+1) + " in the sequence."))
            sequence.append(int(ele))
        
        d = sequence[1] - sequence[0]
        first_term = sequence[0] 
        
        def calculate(n,a1,d):
            answer = a1 + (n-1) * d
        
            print("Term " + str(n) + " of your sequence is " + str(answer) + ".")
            print("")
            print("")
            print("")
            
        calculate(target_term,first_term,d)
        
    def geometric():
        def Equation_finder():
            sequence = []
            print("Input target term")
            target_term = float(input())
            for ele in range(2):
                ele = str(input("Enter term " + str(ele+1) + " in the sequence."))
                sequence.append(convert_to_float(ele))
                    
            r = sequence[1] / sequence [0]
            first_term = sequence[0]
                    
            def calculate(n,a1,r):
                answer = a1 * r ** (n-1)
                
                print("r = " + str(r))
                print("a1 = " + str(a1))
                print("Target term value = " + str(answer))
                
            calculate(target_term, first_term, r)
                
        def Sequence_finder():
            sequence = []
            print("Input target term")
            target_term = float(input())
            for ele in range(2):
                ele = str(input("Enter term " + str(ele+1) + " in the sequence."))
                sequence.append(float(ele))
                    
            r = sequence[1] / sequence [0]
            first_term = sequence[0]
                    
            def calculate(n,a1,r):
                answer = a1 * r ** (n-1)
                
                print("r = " + str(r))
                print("a1 = " + str(a1))
                print("Target term value = " + str(answer))

            calculate(target_term, first_term, r) 
            
                
        print("1: Sequence -> equation")
        print("2: Equation -> sequence")
        print('')
        selector = input()
        if selector == '1':
            Equation_finder()
        elif selector == '2':
            Sequence_finder()
                
        
    
    print("1: Arithmetic")
    print("2: Geometric")
    print('')
    selector = input()
    if selector == '1':
        arithmetic()
    elif selector == '2':
        geometric()
        
def binomial_dist_solver():
    print("Trials")
    print("")
    trials = int(input())
    print("")
    print("Successes")
    print("")
    successes = int(input())
    print("")
    print("probability")
    print("")
    probability  = float(input())

    round_result = round(binom.pmf(successes, trials, probability), 3)
    print(round_result)

def binom_dist_generator():
    print("Trials")
    print("")
    trials = int(input())
    print("")
    print("size")
    print("")
    size = int(input())
    print("")
    print("probability")
    print("")
    probability  = float(input())
    
    result = random.binomial(trials, probability, size)

    print(result)

def normal_dist():
    

    

def infoPage():
    os.system('cls')

    print("ACS version 1.2.0, Last updated: 1/29/2023")
    print('')
    print("ACS (pronounced ""Axe"") or Automatic Calculus Solver is a program intended to solve different types of formulas/equations in calculus. ")
    print('')
    print("The aim is to be user-friendly where user input does not need to be exact, and multiple input methods will be allowed.")
    print('')
    print("At the moment however, this program is a work in progress and many features of it are not active.")
    selector = input()
        
    if selector == 'main menu':
        mainMenu()
    elif selector == 'exit':
        sys.exit()

def mainMenu():
    os.system('cls')
    print("Automatic Calculus Solver main menu")
    print('')
    print('')
    print("1: Derivative solver")
    print("2: Integral solver")
    print("3: Sequences solver")
    print("4: binomial distribution solver")
    print("5: binomial distribution generator")
    print("6: Normal distribution solver")
    print("info: information about ACS")
    print("exit: close ACS")
    print('')
    selector = input()
            
    if selector == '1':
        derivative_environment()
    elif selector == '2':
        integral_environment()
    elif selector == '3':
        sequence_environment()
    elif selector == '4':
        binomial_dist_solver()
    elif selector == '5':
        binom_dist_generator()
    elif selector == '6':
        normal_dist()
    elif selector == 'info':
        infoPage()
    elif selector == 'exit':
        sys.exit()
    else: 
        print("Invalid selection")

mainMenu()