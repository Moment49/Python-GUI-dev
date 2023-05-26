import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# Function
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_str.set(km_output)


# Window
window = ttk.Window(themename='darkly')
window.title('Demo')
window.geometry('300x200')

#TITLE
title_label = ttk.Label(window, text='Miles to Kilometeres', font='Calibri 20 bold')
title_label.pack()

# Input Field
input_frame = ttk.Frame(window)
entry_int = tk.IntVar()
entry = ttk.Entry(input_frame, width=30, textvariable=entry_int)
button = ttk.Button(input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=20)

# OutPut Label
output_str = tk.StringVar()
output_label = ttk.Label(
    window, 
    text='Output',
    font='Calibri 24', 
    textvariable=output_str)
output_label.pack(pady=5)

# Run
window.mainloop()