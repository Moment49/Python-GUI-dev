import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# Create the window
window = tk.Tk()
window.title("Change widgets with Config")
window.geometry("500x500")


# button
def button_func():
    print('a basic btn')

btn_str = tk.StringVar(value='A btn with string var')
btn = ttk.Button(window, text='A simple button',  command=button_func, textvariable=btn_str)
btn.pack(pady=10)

# checkButton
check_var = tk.IntVar(value=10)
check = ttk.Checkbutton(
    window, 
    text='checkbox1', 
    command=lambda:print(check_var.get()),
    variable=check_var,
    onvalue=10,
    offvalue=5
    
    )
check.pack(pady=10)

check2 = ttk.Checkbutton(
    window, 
    text='checkbox2', 
    command=lambda: check_var.get(),    
  )
check2.pack(pady=10)

# radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window, 
                        text='Radiobutton 1' , 
                        value='male', 
                        variable=radio_var,
                        command=lambda:print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(window, 
                        text='Radiobutton 2',
                        command=lambda:print(radio_var.get()),
                        variable=radio_var,
                        value='female')
radio2.pack()

# exercises
def radio_fun():
    print(check_bool.get())
    check_bool.set(False)


# data
radio_str = tk.StringVar()
check_bool = tk.BooleanVar()
# Widgets
radioA  = ttk.Radiobutton(window, 
                        text='Radio A',
                        command=radio_fun,
                        variable=radio_str,
                        value='A')

radioB = ttk.Radiobutton(window, 
                        text='Radio B',
                        command=radio_fun,
                        variable=radio_str,
                        value='B')


exercise_check = ttk.Checkbutton(window, 
                                text='exercise check',
                                variable=check_bool,
                                command=lambda: print(radio_str.get()) )

# Layouts
radioA.pack()
radioB.pack()
exercise_check.pack()
# run
window.mainloop()