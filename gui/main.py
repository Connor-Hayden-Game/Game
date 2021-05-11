from tkinter import *
from win_settings import *

# creates canvas
canvas = Canvas(window, width=800, height=600, bg="black")
canvas.pack(fill="both", expand=True)

# displays the main menu
def display_menu():
    window.title("Game Title")

    # add label to canvas
    canvas.create_text(400, 30, text="WELCOME", font=("Helvetica", 25), fill="blue")

    # add buttons to canvas
    play_button = Button(window, text="Play Now", command=play_now)
    play_button_win = canvas.create_window(400,280, window=play_button)

    exit_button = Button(window, text="Exit to Desktop", command=close_window)
    exit_button_win = canvas.create_window(400,325, window=exit_button)

# clear canvas for the game interface
def play_now():
    canvas.delete('all')

    canvas.configure(bg='white')

    canvas.create_text(400, 30, text="TIME TO PLAY", font=("Helvetica", 25), fill="blue")

# function to close the window
def close_window():
    window.destroy()
    exit()

def main():
    display_menu()
    window.mainloop()

if __name__ == '__main__':
    main()
