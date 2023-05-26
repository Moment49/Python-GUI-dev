import tkinter as tk
from tkinter import ttk

def button_func(entry_str):
    print("a button was pressed")
    print(entry_str.get())

def outer_func(param):
    def inner():
        print("a button was pressed!!!")
        print(param.get())
    return inner

window =tk.Tk()
window.title("buttons, Function and arguments")

# widgets
entry_str = tk.StringVar(value='test')
entry = ttk.Entry(window, textvariable=entry_str)
entry.pack()


# button = ttk.Button(window, text='button', command=lambda: button_func(entry_str))
button = ttk.Button(window, text='button', command=outer_func(entry_str))
button.pack()



window.mainloop()