import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f"x{event.x} y: {event.y}")

window =tk.Tk()
window.title("EVENT Binding")
window.geometry("500x500")

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text='button')
button.pack()

# events
# button.bind('<Alt-KeyPress-a>', lambda event: print(event))
# window.bind('<KeyPress>', lambda event: print(f"a button was ({event.char})"))
# text.bind('<Motion>', get_pos)


entry.bind('<FocusIn>', lambda event: print(('Entry field was selected')))
entry.bind('<FocusOut>', lambda event: print(('Entry field out was selected')))

# Exercise
# text.bind('<Shift-MouseWheel>', lambda event: print("MouseWheel"))

window.mainloop()