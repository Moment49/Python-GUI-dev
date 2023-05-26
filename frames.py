import tkinter as tk
from tkinter import ttk

window =tk.Tk()
window.title("Frame")
window.geometry('500x500')

# frame
frame = ttk.Frame(window, width=500, height=200, borderwidth=30, relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side='right')

#Parenting setting
label = ttk.Label(frame, text='label in frame')
label.pack()

btn = ttk.Button(frame, text='btn in frame')
btn.pack()

# example
label2 = ttk.Label(window, text='label outside frame')
label2.pack(side='right')





window.mainloop()