import sympy as sp
import os
x = sp.Symbol('X')
os.system('cls')

special_Characters = ['+','-','*','/','^','X','Y']

print("Enter equation")
print("")
inp1 = input()
[*inp1]

def dSolver(entry):
    counter = 0
    for element in entry:
        counter += 1
        if element in special_Characters:
            result = element.pop(counter)

    modifiedlist = [int(element) for element in result]
    output = [sp.diff(x**element) for element in modifiedlist]
    return output

print(dSolver(inp1))