import math
import os
import sys
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

def dSolver():
    ans = False
    while ans == False:
        print("Select input mode")
        print('')
        selector = input()
        
        if selector == '1':
            a = int(input("A = "))
            n = int(input("Exponent = "))
            answer = a * n
            exp = n - 1
            print(answer,sups("X",str(exp)))
            
        elif selector == '2':
            a1 = int(input("A1 = "))
            n1 = int(input("Exponent1 = "))
            op = str(input("operator = "))
            a2 = int(input("A2 = "))
            n2 = int(input("Exponent2 = "))
            answer1 = a1 * n1
            exp1 = n1 - 1
            answer2 = a2 * n2
            exp2 = n2 - 1
            print(answer1,sups("X",str(exp1)), op, answer2, sups("X",str(exp2)))

        elif selector == 'main menu':
            ans = True
            mainMenu()
            
        elif selector == 'exit':
            sys.exit()

        else: 
            print("Invalid selection")

def mainMenu():
    os.system('cls')
    print("Automatic Calculus Solver main menu")
    print('')
    print('')
    print("1: Derivative solver")
    print("2: Limits solver (non-functional)")
    print("3: Optimization solver (non-functional)")
    print("4: Integral solver (non-functional)")
    print('')
    print("type info for a little blurb about the program, and exit to close the program")
    print('')
    selector = input()
            
    if selector == '1':
        dSolver()
        
    elif selector == 'info':
        infoPage()

    elif selector == 'exit':
        sys.exit()
        
mainMenu()




def infoPage():
    os.system('cls')

    print("ACS version 1.1.0            Last updated: 1/4/2023")
    print('')
    print("ACS or Automatic Calculus Solver is a program intended to solve different types of formulas/equations in calculus. ")
    print('')
    print("The aim is to be user-friendly where user input does not need to be exact, and multiple input methods will be allowed.")
    print('')
    print("At the moment however, this program is a work in progress and many features of it are not active.")
    selector = input()
        
    if selector == 'main menu':
        mainMenu()
    elif selector == 'exit':
        sys.exit()