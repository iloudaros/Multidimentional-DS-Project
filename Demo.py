import tkinter as tk
import sys
 
sys.path.insert(0, 'Contributions')

from alekarakos import rtreeDemo
from koutou import convex_hull
from iloudaros import lsi_demo



def create_window():
    # Create a new window
    window = tk.Tk()

    BACKGROUND_C = "#342A20"

    BACKGROUND_BT = "#B4894F"
    FOREGROUND__BT = "#000000"
    BUTTON_HOVER_BG_COLOR = "#B4894F"
    BUTTON_HOVER_FG_COLOR = "#C2A47D"

    # Set the title of the window
    window.title("Multidimentional Data Structures Demo")

    # Set the size of the window
    window.geometry("600x350")

    # Set the background color of the window
    window.configure(background=BACKGROUND_C)

    # Create a label widget
    label = tk.Label(window, text="Επιλέξτε το ερώτημα που σας ενδιαφέρει:", font=("Arial", 24), bg=BACKGROUND_C)

    # Pack the label widget to the top of the window
    label.pack(side="top", pady=20)

    # Define button hover effect colors


    # Define button styles
    button_style = {
        "font": ("Arial", 16),
        "bd": 0,
        "padx": 20,
        "pady": 10,
        "bg": BACKGROUND_BT,
        "fg": FOREGROUND__BT,
        "activebackground": BUTTON_HOVER_BG_COLOR,
        "activeforeground": BUTTON_HOVER_FG_COLOR
    }

    # Create 4 button widgets
    button1 = tk.Button(window, text="3D Rtree", **button_style)
    button2 = tk.Button(window, text="Convex Hull", **button_style)
    button3 = tk.Button(window, text="Segment & Interval Trees", **button_style)
    button4 = tk.Button(window, text="Line Segment Intersection", **button_style)

    # Pack the button widgets vertically
    button1.pack(side="top", pady=10)
    button1['command'] = rtreeDemo.Demo
    button2.pack(side="top", pady=10)
    button2['command'] = convex_hull.Demo
    button3.pack(side="top", pady=10)
    button4.pack(side="top", pady=10)
    button4['command'] = lsi_demo.Demo

    # Start the main event loop
    window.mainloop()


if __name__ == '__main__':
    create_window()
