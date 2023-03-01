import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("400x300")
app.title = "ACS"


entry = customtkinter.CTkEntry(master=app,
                               width=220,
                               height=25,
                               border_width=2,
                               corner_radius=10)
entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def Derivative_button():
    print(entry.get)

button = customtkinter.CTkButton(master = app, text="Enter", command = Derivative_button)
button.pack(padx=20, pady=10)




app.mainloop()