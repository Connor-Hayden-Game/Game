#
# FOR REFERENCE FOR SOME CANVAS INTERFACE LINES. TO BE DELETED LATER
#

from tkinter import *
from win_settings import *
# import time

# creates canvas
canvas = Canvas(window, width=800, height=600, bg="black")
canvas.pack(fill="both", expand=True)

# displays the main menu
def display_menu():
    window.title("Game Title")

    # sets background of canvas to image given
    background = canvas.create_image(0, 0, image=background_image, anchor="nw")

    # add label to canvas
    canvas.create_text(400, 30, text="WELCOME", font=("Helvetica", 25), fill="#7a2314")

    # add entry box for username
    canvas.create_text(310, 250, text="Username:", font=("Helvetica", 12), fill="#7a2314")
    user_entry = Entry(window)
    canvas.create_window(400, 250, window=user_entry, height=20, width=100)

    # add buttons to canvas
    play_button = Button(window, text="Play Now", command=start_game)
    play_button_win = canvas.create_window(400,275, window=play_button)

    exit_button = Button(window, text="Exit to Desktop", command=close_window)
    exit_button_win = canvas.create_window(400,350, window=exit_button)

# function to close the window
def close_window():
    window.destroy()
    exit()

def start_game():
    # clear canvas
    canvas.delete("all")

    # sets background of canvas to image given
    background = canvas.create_image(0, 0, image=background_image, anchor="nw")

    # text for canvas
    canvas.create_text(400, 250, text="Logging in to", font=("Helvetica", 25), fill="#7a2314")
    canvas.create_text(400, 300, text="*username*...", font=("Helvetica", 25), fill="#7a2314")

    # add timer to make this canvas a temp loading screen, then move on to hero_screen?
    # canvas.after(3000, canvas.delete("all"))
    # hero_screen()

def hero_screen():
    # this will be the heroCreation file code
    pass

def main():
    display_menu()
    window.mainloop()

if __name__ == '__main__':
    main()
