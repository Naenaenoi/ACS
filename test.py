#File for testing new things before bringing to the ACS file


#Tester for entire equation input instead of individual characters
import os

os.system('cls')
print("Enter equation")
print("")
inp1 = input()
[*inp1]

res = [ele for ele in inp1 if ele.strip()]

print(res)    