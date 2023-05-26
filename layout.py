import tkinter as tk
from tkinter import ttk

window =tk.Tk()
window.title("Layout")
window.geometry('600x400+100+100')


# widget
label_1 = ttk.Label(window, text='text1', background='red')
label_2 = ttk.Label(window, text='text2', background='blue')

# pack
# label_1.pack(side='left', expand=True, fill='y')
# label_2.pack(side='left', expand=True, fill='both')

# Grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=2)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

label_1.grid(row=0, column=1, sticky='n')
# label_2.grid(row=0, column=0, sticky='nsew')
label_2.grid(row=1, column=1, columnspan=1, sticky='nsew')

# place
# label_1.place(x=100, y=200, width=200, height=100)
# label_2.place(relx=0.5, rely=0.5, relwidth=1, anchor='center')

window.mainloop()