import sympy as sp
from sympy import *
import tkinter
import customtkinter
import os
import sys
x = sp.Symbol('X')
y = sp.Symbol('Y')

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("300x300")

def button_function():
    print("button pressed")
    
button1 = customtkinter.CTkButton(master=app, text="MAN", command=button_function)
button1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()