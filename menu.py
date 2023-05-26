import tkinter as tk
from tkinter import ttk

window =tk.Tk()
window.title("Menu")
window.geometry('600x400+100+100')
# window.iconbitmap('file path')
window.minsize(200, 100)
window.resizable(False, False)

# screen att
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# window attr
# window.attributes('-alpha', 1)

# security event
window.bind('<Escape>', lambda event: window.quit())
# window.attributes("-disabled", True)
# window.attributes("-fullscreen", True)

# title bar
window.overrideredirect(True)
























# # menu
# menu = tk.Menu(window)
# # submenu
# file_menu = tk.Menu(menu, tearoff=False)
# file_menu.add_command(label='New', command=lambda: print('New file'))
# file_menu.add_command(label='Open', command=lambda: print('Open file'))
# menu.add_cascade(label='File', menu=file_menu)

# # another sub_menu
# help_menu = tk.Menu(menu, tearoff=False)
# menu.add_cascade(label='help', menu=help_menu)

# window.configure(menu = menu)






window.mainloop()