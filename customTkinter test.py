import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    print("button pressed")
    
def integral_window():
    wewe = int

# Use CTkButton instead of tkinter Button
button1 = customtkinter.CTkButton(master=app, text="Derivative Environment", command=button_function)
button1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

button2 = customtkinter.CTkButton(master=app, text="Integral Environment", command=integral_window)
button2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)



app.mainloop()