from tkinter import *
from win_settings import *
import tkinter.messagebox

# global window title
window.title('TEST ENVIRONMENT')

# creates canvas
canvas = Canvas(window, width=800, height=600)
canvas.pack(fill='both', expand=True)

canvas.configure(bg='#DDE7EC')

canvas.create_line(335, 800, 335, 0)
# canvas.create_line(500, 800, 500, 0)
        
def createDrops():
##  WEAPON SELECTION 
    weaponLabel = Label(canvas, text="Select Your Weapon!")
    canvas.create_window(20,20, window=weaponLabel, anchor='w')

    # Weapon dropdown menu options
    weapons = [
            "Sword",
            "Bow",
            "Magic Staff"
            ]

    # Access the menu widget using StringVar function
    weaponClicked = StringVar()
              
    # Create weapon dropdown menu
    weaponDrop = OptionMenu(canvas, weaponClicked, *weapons)
    canvas.create_window(150, 20, window=weaponDrop, anchor='w')

##  ELEMENT SELECTION    
    elementLabel = Label(canvas, text="Select Your Element!")
    canvas.create_window(20, 70, window=elementLabel, anchor='w')
            
    # Element dropdown menu options
    elements = [
            "Fire",
            "Water",
            "Earth",
            "Eternal"
            ]

    # Access the menu widget using StringVar function
    elementClicked = StringVar()
                  
    # Create element dropdown menu
    elementDrop = OptionMenu(canvas, elementClicked, *elements)
    canvas.create_window(150, 70, window=elementDrop, anchor='w')

    def showWeapon():
        if(elementClicked.get() == "Eternal"):
            tkinter.messagebox.showinfo("Ah, shucks!", "It looks like you will need to discover the Eternal element before using it to make weapons! Choose a new element.")
        else:
            submitLabel = Label(canvas, text="level 1 " + weaponClicked.get().lower() + " of " + elementClicked.get().lower())
            submitLabel.lower()
            canvas.create_window(150, 150, window=submitLabel, anchor='w')

    submitWeapon = Button(window, text="Submit", command=showWeapon)
    canvas.create_window(150, 110, window=submitWeapon, anchor='w')

def createRads():
    weaponLabel = Label(canvas, text="Select Your Weapon!")
    canvas.create_window(375,20, window=weaponLabel, anchor='w')

    clicked = StringVar()

    swordRadio = Radiobutton(text="Sword", variable=clicked)
    canvas.create_window(500, 20, window=swordRadio, anchor='w')

    bowRadio = Radiobutton(text="Bow", variable=clicked)
    canvas.create_window(500, 50, window=bowRadio, anchor='w')

    staffRadio = Radiobutton(text="Magic Staff", variable=clicked)
    canvas.create_window(500, 80, window=staffRadio, anchor='w')

            
    selected = clicked.get() # doesn't work yet. Selects all when hovered over

def main():
    createDrops()
    # createRads()

if __name__ == '__main__':
    main()
