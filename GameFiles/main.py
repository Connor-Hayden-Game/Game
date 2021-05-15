# Fonts we like: Matura MT Script Capitals

from tkinter import *
import tkinter.messagebox
from win_settings import *
import heroCreation as hc
import heroUpdate as hu

# creates canvas
canvas = Canvas(window, width=800, height=600)
canvas.pack(fill='both', expand=True)

# global window title
window.title('CR')

# displays the main menu
def display_menu():
    # set main menu bg to black for now
    canvas.configure(bg='black')

    # add label to canvas
    canvas.create_text(400, 200, text="Castle Reign", font=('Matura MT Script Capitals', 75), fill='#1A5A14')

    # add buttons to canvas (named per function)
    play_button = Button(window, text="Create Hero", bg='#1A5A14', font=('Matura MT Script Capitals', 15), padx=2, pady=2, command=play_now)
    canvas.create_window(400,280, window=play_button)

    exit_button = Button(window, text="Exit to Desktop", command=close_window)
    canvas.create_window(400,325, window=exit_button)

# clear canvas for the game interface
def play_now():
    # clear canvas in order to start fresh
    canvas.delete('all')

    # set game interface canvas configs
    canvas.configure(bg='#DDE7EC')

    # add buttons to game interface
    main_menu_button = Button(window, text="Main Menu", command=go_menu)
    canvas.create_window(760,20, window=main_menu_button)

    canvas.create_text(400, 20, text="Hero Creation", font=('Candara', 25), fill='#1A5A14')

    def createHero():
        points = 30
        # bank = hu.bank

        # gets the user input and then sets it to a temp point to subtract from points var
        healthPoints = int(health.get())
        points -= healthPoints
        meleePoints = int(melee.get())
        points -= meleePoints
        rangedPoints = int(ranged.get())
        points -= rangedPoints
        magicPoints = int(magic.get())
        points -= magicPoints

        # input validation
##      should add an elif that says "if they're all left blank do a messagebox saying please enter some stats
        if(points < 0):
            tkinter.messagebox.showinfo("Whoops!",  "You only have 30 points. Please adjust your attributes!")
        elif((healthPoints<0) or (meleePoints<0) or (rangedPoints<0) or (magicPoints<0)):
            tkinter.messagebox.showinfo("Whoops!", "You cannot have a nageative value!")
        elif(healthPoints==0):
            tkinter.messagebox.showinfo("Whoops!", "Health cannot be zero!")
        else: # writes to file as long as all inputs are valid
            file = open('interfaceSave.txt', 'w')
            file.write(str(heroName.get()) + '\n'   + \
                       str(health.get()) + '\n'+ \
                       str(melee.get()) + '\n' + \
                       str(ranged.get()) + '\n'+ \
                       str(magic.get()) + '\n' + \
                       str(points) + '\n' + \
                       str(20))
            file.close()
            go_menu()
            tkinter.messagebox.showinfo("Congrats!", "Hero Created. Click Play Now to start your adventure!")

##  info icons on right side of screen
    # coinImage = Image.open(r'img/coinPouch.png')
    # canvas.image = ImageTk.PhotoImage(coinImage)
    # canvas.create_image(680,60, image=canvas.image, anchor='nw')

    # coinLabel = Label(canvas, text="Coins:", fg='#1A5A14')
    # canvas.create_window(700,95, window=coinLabel)

    # coinAmount = Label(canvas, text=hu.bank, fg='#1A5A14')
    # canvas.create_window(700,95, window=coinAmount)
    
    # take user input for user info
    heroLabel = Label(canvas, text="Hero Name:", fg='#1A5A14')
    canvas.create_window(100,95, window=heroLabel)
    # entry box for hero name
    heroName = Entry(canvas)
    canvas.create_window(200,95, window=heroName)

    canvas.create_text(180, 120, text="You have 30 skill points to spend. Choose wisely!", font=('Candara', 10), fill='#1A5A14')

    # creates labels/input boxes for all hero atttributes
    healthLabel = Label(canvas, text="Health:", fg='#1A5A14')
    canvas.create_window(100,145, window=healthLabel)
    health = Entry(canvas)
    canvas.create_window(200,145, window=health)
    
    meleeLabel = Label(canvas, text="Melee:", fg='#1A5A14')
    canvas.create_window(100,170, window=meleeLabel)
    melee = Entry(canvas)
    canvas.create_window(200,170, window=melee)

    rangedLabel = Label(canvas, text="Ranged:", fg='#1A5A14')
    canvas.create_window(100,195, window=rangedLabel)
    ranged = Entry(canvas)
    canvas.create_window(200,195, window=ranged)

    magicLabel = Label(canvas, text="Magic:", fg='#1A5A14')
    canvas.create_window(100,220, window=magicLabel)
    magic = Entry(canvas)
    canvas.create_window(200,220, window=magic)
    
    # submit button to write all attributes to text file
    submit_button = Button(window, text="Submit", command=createHero)
    canvas.create_window(400,530, window=submit_button)
    
# return to main menu
def go_menu():
    canvas.delete('all')
    display_menu()

# function to close the window
def close_window():
    window.destroy()
    exit()

def main():
    display_menu()
    window.mainloop()

if __name__ == '__main__':
    main()
