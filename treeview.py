import tkinter as tk
from ttkbootstrap import ttk
from random import choice

# window
window =tk.Tk()
window.title('TreeView')
window.geometry("600x400")

# data
first_names =['James', 'John', 'Leonard', 'Kelly']
last_names =['Gabriel', 'Anderson', 'Martins', 'Micheal']

# treeview
table = ttk.Treeview(window, columns=('First', 'Last', 'Email'), show='headings')
table.heading('First', text='First name')
table.heading('Last', text='Last name')
table.heading('Email', text='Email')
table.pack(fill='both', expand=True)

# Insert values to a table
# table.insert(parent='', index=0, values=('John', 'Doe', 'Johndow@gmail.com'))

for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f"{first[0]}{last}@gmail.com"
    data = (first, last, email)
    table.insert(parent='', index=0, values=data)

table.insert(parent='', index=tk.END, values=('XXX', 'YYY', 'ZZZZZ'))

# events
def items_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])
def delete_items(_):
    for i in table.selection():
        print(i)
        print(table.delete(i))

table.bind('<<TreeviewSelect>>', items_select)
table.bind('<Delete>', delete_items)

# run
window.mainloop()