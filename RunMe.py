import tkinter as tk
import random
import ctypes
import time

def move_window():
    global dx, dy


    x, y = root.winfo_x(), root.winfo_y()


    mouse_x, mouse_y = root.winfo_pointerx(), root.winfo_pointery()


    x_new, y_new = x + dx, y + dy


    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()


    window_width, window_height = 200, 100

    if x_new <= 0 or x_new + window_width >= screen_width:
        dx = -dx
    if y_new <= 0 or y_new + window_height >= screen_height:
        dy = -dy


    if x_new <= mouse_x <= x_new + window_width and y_new <= mouse_y <= y_new + window_height:
        dx = -dx
        dy = -dy


    root.geometry(f"{window_width}x{window_height}+{x_new}+{y_new}")


    root.after(10, move_window)

def close_app(event=None):
    root.destroy()


root = tk.Tk()

root.overrideredirect(False)
root.attributes('-topmost', False)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
initial_x = random.randint(0, screen_width - 200)
initial_y = random.randint(0, screen_height - 100)
root.geometry(f"200x100+{initial_x}+{initial_y}")


root.configure(bg="blue")


label = tk.Label(root, text="=＾●w●＾=", font=("Arial", 24), bg="blue", fg="white")
label.pack(expand=True, fill=tk.BOTH)

dx, dy = 3, 3


root.bind("<Escape>", close_app)


ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)


move_window()


root.mainloop()
