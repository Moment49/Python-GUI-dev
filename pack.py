import tkinter as tk
from tkinter import ttk

window =tk.Tk()
window.title("Layout")
window.geometry('600x400+100+100')


# widget
label_1 = ttk.Label(window, text='text1', background='red')
label_2 = ttk.Label(window, text='text2', background='blue')
label_3 = ttk.Label(window, text='text3', background='green')
button = ttk.Button(window, text='Button')

# Layout
label_1.pack(side='left')
label_2.pack(side='left')
label_3.pack(side='left')
button.pack(side='left')


window.mainloop()