import tkinter
import customtkinter as ctk
import os
import sympy as sp
x = sp.Symbol('X')
y = sp.Symbol('Y')

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("700x400")

def default():
    print("Nothing lol")
    
def updater():
    print("notig")
    

    

    
def integral_environment(entry):
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
        
        def int_compiler(entry):
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
    
option_frame = ctk.CTkFrame(app)
option_frame.place(relx=0.5, rely=0.4, anchor = tkinter.CENTER)

derivative_button = ctk.CTkButton(option_frame, text="Derivative", command=updater)
derivative_button.grid(row=0, column=0, padx=10, pady=10)

integral_button = ctk.CTkButton(option_frame, text="Integral")
integral_button.grid(row=0, column=1, padx=10, pady=10)
    
equation = tkinter.StringVar()
entry_box = ctk.CTkEntry(app, width=350, height=40, textvariable = equation)
entry_box.place(relx=0.5, rely=0.8, anchor = tkinter.S)
    
solve = ctk.CTkButton(app, text="Solve", command = default)
solve.place(relx=0.5, rely=0.9, anchor = tkinter.S)

answer_label = ctk.CTkLabel(app, text="")
answer_label.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

app.mainloop()