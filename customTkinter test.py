import customtkinter as ctk
import tkinter
import os
import sympy as sp
x = sp.Symbol('X')
y = sp.Symbol('Y')

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("700x400")



dict1 = {'**0':'\u2070',
         '**1':'\u00b9',
         '**2':'\u00b2',
         '**3':'\u00b3',
         '**4':'\u2074',
         '**5':'\u2075',
         '**6':'\u2076',
         '**7':'\u2077',
         '**8':'\u2078',
         '**9':'\u2079'}

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
    entry = entry_box.get()
    [*entry]
    Up_equation = [element.upper() for element in entry]
    equation = [element for element in Up_equation if element.strip()]

    def solver(function, var):
        answer = sp.diff(function, var)
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
    answer_label.configure(text= compiler(equation))
    answer_label.update()

    
def integral_environment():
        entry = entry_box.get()
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
        answer_label.configure(text= int_compiler(equation))
        answer_label.update()
        
    
def Selector():
    answer_label.configure(text = "Select solver mode first")
    answer_label.update()

def Derivative():
    integral_checkbox.deselect()
    integral_checkbox.update()
    solve.configure(command=derivative_environment)
    solve.update()
    entry_box.configure(placeholder_text="Input derivative")
    entry_box.update()

def Integral():
    derivative_checkbox.deselect()
    derivative_checkbox.update()
    solve.configure(command=integral_environment)
    solve.update()
    entry_box.configure(placeholder_text="Input integeral")
    entry_box.update()
    
app.title("ACS")
    
option_frame = ctk.CTkFrame(app)
option_frame.place(relx=0.5, rely=0.4, anchor = tkinter.CENTER)

derivative_checkbox = ctk.CTkCheckBox(option_frame, text="Derive", command=Derivative)
derivative_checkbox.grid(row=0, column=0, padx=10, pady=10)

integral_checkbox = ctk.CTkCheckBox(option_frame, text="Integrate", command=Integral)
integral_checkbox.grid(row=0, column=1, padx=10, pady=10)

equation = tkinter.StringVar()
entry_box = ctk.CTkEntry(app, width=350, height=40, placeholder_text="Select Entrty Mode", textvariable = equation)
entry_box.place(relx=0.4, rely=0.9, anchor = tkinter.S)
    
solve = ctk.CTkButton(app, text="Solve", command = Selector)
solve.place(relx=0.8, rely=0.89, anchor = tkinter.S)

answer_label = ctk.CTkLabel(app, text="", font=("TkDefaultFont",20))
answer_label.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

app.mainloop()