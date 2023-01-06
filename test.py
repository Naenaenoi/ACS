#File for testing new things before bringing to the ACS file


#Tester for entire equation input instead of individual characters
import os
def remover(List, item):
 
    # remove the item for all its occurrences
    c = List.count(item)
    for i in range(c):
        List.remove(item)
 
    return List


os.system('cls')
print("Enter equation")
print("")
inp1 = input()
[*inp1]

res = [ele for ele in inp1 if ele.strip()]

print(res)