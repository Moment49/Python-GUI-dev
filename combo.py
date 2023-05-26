import tkinter as tk
from tkinter import ttk



window =tk.Tk()
window.title("Combo box")
window.geometry('500x500')

# widget
# items = ['Ice cream', 'Pizza', 'Brocoli']
# food_string = tk.StringVar(value=items[0])
# combo = ttk.Combobox(window, textvariable=food_string)
# combo['values'] = items
# combo.configure(values = items)
# combo.pack()

# # events
# combo.bind('<<ComboboxSelected>>', lambda event: print('test'))


# spin
spin_box = ttk.Spinbox(window, from_=3, to = 20, increment=3, command=lambda: print('a btn pressed'))
# spin_box['value'] = (1, 2, 3, 4, 5)
spin_box.pack()

window.mainloop()