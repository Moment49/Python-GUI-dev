import tkinter as tk
from tkinter import ttk



window =tk.Tk()
window.title("Canvas")
window.geometry('500x500')

#canvas
canvas = tk.Canvas(window, bg='white')
canvas.pack()

# canvas.create_rectangle((50, 20, 100, 200), fill='red', width=10, outline='green')
# canvas.create_rectangle((50, 20, 100, 200), fill='red', width=10, outline='green')
# canvas.create_line((200, 0, 100, 150), fill='blue')
# canvas.create_oval((400, 0, 100, 100), fill='red')

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x-brus_size/2, y-brus_size/2, x+brus_size/2, y+brus_size/2), fill='black')

def brush_size_adjust(event):
    global brus_size
    if event.delta > 0:
        brus_size += 4
    else:
        brus_size -= 4
    
    brus_size = max(0, min(brus_size, 50))
    print(event)

brus_size = 2
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', brush_size_adjust)


window.mainloop()