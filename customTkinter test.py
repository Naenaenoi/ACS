import customtkinter as ctk
import tkinter
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

button = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="log",
                                 command=button_function)
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)


    

app.mainloop()