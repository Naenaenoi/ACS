import sympy as sp
import os
x = sp.Symbol('X')
y = sp.Symbol('Y')
os.system('cls')

special_Characters = ['+','-','*','/','^','X','Y']

print("Enter equation")
print("")
inp1 = input()
[*inp1]

def interpreter(entry):
    counter = 0
    for element in entry:
        if element in special_Characters:
            index1 = entry.index(element)
            counter += 1
            
            
            

"""
def dSolver(entry):
    counter = 0
    for element in entry:
        counter += 1
        if element in special_Characters:
            result = element.pop(counter)
        else:
            result = entry

    modifiedlist = [int(element) for element in result]
    output = [sp.diff(element*x**element) for element in modifiedlist]
    return output

print(dSolver(inp1))
"""