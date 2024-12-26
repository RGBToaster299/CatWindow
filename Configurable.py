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
def is_color_in_list(color_name):
    colors = [
        "Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink", "Brown", "Gray", "Black", "White",
        "Aqua", "Azure", "Beige", "Bisque", "BlanchedAlmond", "BlueViolet", "BurlyWood", "CadetBlue",
        "Chartreuse", "Chocolate", "Coral", "CornflowerBlue", "Cornsilk", "Crimson", "Cyan", "DarkBlue",
        "DarkCyan", "DarkGoldenRod", "DarkGray", "DarkGreen", "DarkKhaki", "DarkMagenta", "DarkOliveGreen",
        "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGray",
        "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGray", "DodgerBlue", "FireBrick",
        "FloralWhite", "ForestGreen", "Fuchsia", "Gainsboro", "GhostWhite", "Gold", "GoldenRod", "GreenYellow",
        "HoneyDew", "HotPink", "IndianRed", "Indigo", "Ivory", "Khaki", "Lavender", "LavenderBlush", "LawnGreen",
        "LemonChiffon", "LightBlue", "LightCoral", "LightCyan", "LightGoldenRodYellow", "LightGray", "LightGreen",
        "LightPink", "LightSalmon", "LightSeaGreen", "LightSkyBlue", "LightSlateGray", "LightSteelBlue", "LightYellow",
        "Lime", "LimeGreen", "Linen", "Magenta", "Maroon", "MediumAquaMarine", "MediumBlue", "MediumOrchid",
        "MediumPurple", "MediumSeaGreen", "MediumSlateBlue", "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed",
        "MidnightBlue", "MintCream", "MistyRose", "Moccasin", "NavajoWhite", "Navy", "OldLace", "Olive", "OliveDrab",
        "OrangeRed", "Orchid", "PaleGoldenRod", "PaleGreen", "PaleTurquoise", "PaleVioletRed", "PapayaWhip", "PeachPuff",
        "Peru", "Plum", "PowderBlue", "RebeccaPurple", "RosyBrown", "RoyalBlue", "SaddleBrown", "Salmon", "SandyBrown",
        "SeaGreen", "SeaShell", "Sienna", "Silver", "SkyBlue", "SlateBlue", "SlateGray", "Snow", "SpringGreen",
        "SteelBlue", "Tan", "Teal", "Thistle", "Tomato", "Turquoise", "Violet", "Wheat", "WhiteSmoke", "YellowGreen"
    ]

    return color_name in colors


print("Hi this is where you will configure the Cat Window :3")
def init():
    color = input("Background Color(be careful with grammar):")
    if is_color_in_list(color) != True:
        print("Invalid color please restart the program otherwise everything might break")
    
    facecol = input("Cat Face Color:")
    return color,facecol
BGCol,FaceCol = init()
root = tk.Tk()

root.overrideredirect(False)
root.attributes('-topmost', False)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
initial_x = random.randint(0, screen_width - 200)
initial_y = random.randint(0, screen_height - 100)
root.geometry(f"200x100+{initial_x}+{initial_y}")


label = tk.Label(root, text="=＾●w●＾=", font=("Arial", 24), bg=BGCol, fg=FaceCol)
label.pack(expand=True, fill=tk.BOTH)
root.configure(bg=BGCol)





dx, dy = 3, 3


root.bind("<Escape>", close_app)


ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)


move_window()


root.mainloop()
