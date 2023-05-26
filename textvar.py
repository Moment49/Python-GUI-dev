import tkinter as tk
from tkinter import ttk
# import ttkbootstrap as ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

def btn_func():
    print(str_var.get())
    str_var.set('btn pressed again')

# Create the window
window = tk.Tk()
window.title("Tkinter Variables")
window.geometry("500x200")

# Tkinter Variable
string_var = tk.StringVar(value='Start Value')

label = ttk.Label(master=window, text='label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text='button', command=button_func)
button.pack()

# exercises

str_var = tk.StringVar(value='start value')
entry2 = ttk.Entry(master=window, textvariable=str_var)
entry2.pack()

entry2 = ttk.Entry(master=window, textvariable=str_var)
entry2.pack()

btn = ttk.Button(master=window, text='Button', command=btn_func)
btn.pack(pady=10)



# Run
window.mainloop()