import sympy as sp
import os
x = sp.Symbol('X')
os.system('cls')
list1 = ['5','12','6']

def listmaker(list1):
    modifiedlist = [int(ele) for ele in list1]
    output = [sp.diff(x**ele) for ele in modifiedlist]
    return output
print(listmaker(list1))