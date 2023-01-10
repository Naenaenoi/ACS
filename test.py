#File for testing new things before bringing to the ACS file


#Tester for entire equation input instead of individual characters
#import latex
import os
from sympy.interactive import printing 
printing.init_printing(use_latex = True)
import sympy as sp
import numpy as np

dict3 = {'X': '1',
         '^': '0.001',
         '+': '0.002',
         '-': '0.003',
         '=': '0.004',
}

def specialCharacters(x):
    z = '{}'.format(dict3.get(x))
    return x

os.system('cls')
print("Enter equation")
print("")
inp1 = input()

[*inp1]
#Sample equation: 5X^2 + 13X + 2
res = [ele for ele in inp1 if ele.strip()]


try:
    res = [float(i) for i in res]
except ValueError:
    specialCharacters(ValueError)
    
print(res, ValueError)



nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ops = [ '+','-','=']
var = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


error = False

#try:

#except:
    #error = True
   # if error == True:
        



"""
x = sp.Symbol('X')

print(sp.diff(x**inp1))


 
x = sp.symbols('x') 
I = sp.Integral(x**2,(x,0,1)) 
v = I.doit() 
print(latex(I),=,latex(v)) 
"""