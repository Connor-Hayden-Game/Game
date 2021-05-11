from tkinter import *
from PIL import ImageTk, Image

window = Tk()


# creating an icon for window
window.iconbitmap(r"gui\img\my_icon.ico")

# configs of window
win_width = 800
win_height = 600
window.resizable(width=FALSE, height=FALSE)

# retrieve monitor width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# create center point for window
x = (screen_width / 2) - (win_width / 2)
y = (screen_height / 2) - (win_height / 2)

# set geometry of window
window.geometry(f'{win_width}x{win_height}+{int(x)}+{int(y)}')
