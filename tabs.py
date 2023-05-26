import tkinter as tk
from tkinter import ttk

window =tk.Tk()
window.title("Tabs")
window.geometry('600x400')

# notebook
notebook = ttk.Notebook(window)

# tab1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text='text 1')
label1.pack()
btn1 = ttk.Button(tab1, text='btn1')
btn1.pack()
# tab2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text='text 2')
label2.pack()
btn2 = ttk.Button(tab2, text='btn2')
btn2.pack()

# tab3
tab3 = ttk.Frame(notebook)
text = tk.Text(tab3, width=20, height=10)
text.pack()
button = ttk.Button(tab3, text='Click')
button.pack()


notebook.add(tab1, text='Tab1')
notebook.add(tab2, text='Tab2')
notebook.add(tab3, text='Menu')
notebook.pack()



window.mainloop()