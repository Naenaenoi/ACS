import tkinter
import customtkinter as ctk
import os
import sympy as sp
x = sp.Symbol('X')
y = sp.Symbol('Y')

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    print("button pressed")
    
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
    
    print(compiler(equation))
    
        

root = ctk.app()
def integral_button():
    root.clear_Widgets()

    output_label = ctk.Label(root, text=integral_environment())
    output_label.pack()

    root.run()
    

# Use CTkButton instead of tkinter Button
button1 = ctk.CTkButton(master=app, text="Derivative Environment", command=button_function)
button1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

button2 = ctk.CTkButton(master=app, text="Integral Environment", command=integral_button)
button2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

app.mainloop()