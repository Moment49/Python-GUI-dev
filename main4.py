import tkinter as tk
from tkinter import ttk

def btn_func():
    """Greet user"""
    print("Hello")
    print(entry_value.get())


# Create a window
# window = tk.Tk()
# window.title("Getting and Setting widgets")
# # window.title("Window and widgets")
# window.geometry('800x500')

# # ttk Widgets
# label = ttk.Label(master=window, text='This is a text')
# label.pack()

# # tk- Text Create widgets
# text = tk.Text(master=window)
# text.pack()

# # ttk entry
# entry = ttk.Entry(master=window)
# entry.pack()
# # ttk label
# mylabel = ttk.Label(master=window, text="my label", font="Calibri 18")
# mylabel.pack()

# # ttk button
# button = ttk.Button(master=window, text="A button", command=btn_func)
# button.pack()



window = tk.Tk()
window.title("Getting and Setting widgets")
window.geometry('800x500')

# widgets
label = ttk.Label(master=window, text='This is a label')
label.pack()

# entry
entry_value = tk.StringVar()
entry = ttk.Entry(master=window, textvariable=entry_value)
entry.pack()

# button
btn = ttk.Button(master=window, text='Click me!', command=btn_func)
btn.pack()



#run
window.mainloop()