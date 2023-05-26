import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def btn_func():
    """Greet user"""
    entry_text = entry_value.get()
    #Update the label
    label.configure(text='Some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'
    # print(label.configure())

def btn_func2():
    """Enable btn"""
    entry_value.get()
    label.configure(text='This is a label')
    entry['state'] = 'enabled'




# Create the window
window = tk.Tk()
window.title("Change widgets with Config")
window.geometry("500x500")


# widgets
label = ttk.Label(master=window, text='This is a label')
label.pack()

# entry
entry_value = tk.StringVar()
entry = ttk.Entry(master=window, textvariable=entry_value)
entry.pack()

# button
btn = ttk.Button(master=window, text='Click me!', command=btn_func)
btn.pack(pady=10)

change_btn = ttk.Button(master=window, text='Click me agein!', command=btn_func2)
change_btn.pack(pady=10)




# run
window.mainloop()