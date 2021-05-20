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
        points = 10
        if((weaponElementClicked.get() == "Eternal") or (armorClicked.get() == "Eternal") or (amuletClicked.get() == "Eternal")):
            tkinter.messagebox.showinfo("Ah, shucks!", "It looks like you will need to discover the Eternal element before using it to make weapons! Choose a new element.")
        else:
            # gets the user input and then sets it to a temp point to subtract from points var
            healthPoints = int(health.get())
            points -= healthPoints
            meleePoints = int(melee.get())
            points -= meleePoints
            rangedPoints = int(ranged.get())
            points -= rangedPoints
            magicPoints = int(magic.get())
            points -= magicPoints
            
            armorSelected = "level 1 armor of " + armorClicked.get().lower()
            weaponSelected = "level 1 " + weaponClicked.get().lower() + " of " + weaponElementClicked.get().lower()
            amuletSelected = "level 1 amulet of " + amuletClicked.get().lower()

            if(weaponClicked.get() == "Sword"):
                classSelected = "Brute"
            elif(weaponClicked.get() == "Bow"):
                classSelected = "Archer"
            elif(weaponClicked.get() == "Magic Staff"):
                classSelected = "Warlock"

            # input validation
##          should add an elif that says "if they're all left blank do a messagebox saying please enter some stats
            if(points < 0):
                tkinter.messagebox.showinfo("Whoops!",  "You only have 10 points. Please adjust your attributes!")
            elif((healthPoints < 0) or (meleePoints < 0) or (rangedPoints < 0) or (magicPoints < 0)):
                tkinter.messagebox.showinfo("Whoops!", "You cannot have a nageative value!")
            elif(healthPoints == 0):
                tkinter.messagebox.showinfo("Whoops!", "Health cannot be zero!")
            else: # writes to file as long as all inputs are valid
                file = open('interfaceSave.txt', 'w')
                file.write(str(heroName.get()) + '\n' + \
                           str(health.get())   + '\n' + \
                           str(melee.get())    + '\n' + \
                           str(ranged.get())   + '\n' + \
                           str(magic.get())    + '\n' + \
                           str(points)         + '\n' + \
                           str(20)             + '\n' + \
                           str(armorSelected)  + '\n' + \
                           str(weaponSelected) + '\n' + \
                           str(amuletSelected) + '\n' + \
                           str(1)              + '\n' + \
                           str(1)              + '\n' + \
                           str(1)              + '\n' + \
                           str(classSelected))
                file.close()
                go_menu()
                tkinter.messagebox.showinfo("Congrats!", "Hero Created. Click Play Now to start your adventure!")
            
    # take user input for user info
    heroLabel = Label(canvas, text="Hero Name:", fg='#1A5A14', bg='#DDE7EC')
    canvas.create_window(50,95, window=heroLabel, anchor='w')
    # entry box for hero name
    heroName = Entry(canvas)
    canvas.create_window(125,95, window=heroName, anchor='w')

    canvas.create_text(180, 120, text="You have 10 skill points to spend. Choose wisely!", font=('Candara', 10, 'bold'), fill='#1A5A14')

    # creates labels/input boxes for all hero atttributes
    healthLabel = Label(canvas, text="Health:", fg='#1A5A14', bg='#DDE7EC')
    canvas.create_window(50,145, window=healthLabel, anchor='w')
    health = Entry(canvas)
    canvas.create_window(125,145, window=health, anchor='w')
    
    meleeLabel = Label(canvas, text="Melee:", fg='#1A5A14', bg='#DDE7EC')
    canvas.create_window(50,170, window=meleeLabel, anchor='w')
    melee = Entry(canvas)
    canvas.create_window(125,170, window=melee, anchor='w')

    rangedLabel = Label(canvas, text="Ranged:", fg='#1A5A14', bg='#DDE7EC')
    canvas.create_window(50,195, window=rangedLabel, anchor='w')
    ranged = Entry(canvas)
    canvas.create_window(125,195, window=ranged, anchor='w')

    magicLabel = Label(canvas, text="Magic:", fg='#1A5A14', bg='#DDE7EC')
    canvas.create_window(50,220, window=magicLabel, anchor='w')
    magic = Entry(canvas)
    canvas.create_window(125,220, window=magic, anchor='w')

    canvas.create_line(800, 240, 0, 240)

  #########################################################################################
 ######################################              #######################################
######################################   SELECTIONS   #######################################
 ######################################              #######################################
  #########################################################################################

##  ARMOUR SELECTION   
    armorLabel = Label(canvas, text="Select Your Armor Type:", fg='#1A5A14', bg='#DDE7EC')
    canvas.create_window(50, 260, window=armorLabel, anchor='w')
                
    # Armor element dropdown menu options
    armors = [
            "Fire",
            "Water",
            "Earth",
            "Eternal"
            ]

    # Access the menu widget using StringVar function
    armorClicked = StringVar()
                      
    # Create Element dropdown menu
    armorDrop = OptionMenu(canvas, armorClicked, *armors)
    canvas.create_window(250, 260, window=armorDrop)

##  WEAPON SELECTION 
    weaponLabel = Label(canvas, text="Select Your Weapon:", fg='#1A5A14', bg='#DDE7EC')
    canvas.create_window(50,310, window=weaponLabel, anchor='w')

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
    canvas.create_window(250, 310, window=weaponDrop)

##  ELEMENT SELECTION    
    weaponElementLabel = Label(canvas, text="Select Your Weapon Type:", fg='#1A5A14', bg='#DDE7EC')
    canvas.create_window(50, 370, window=weaponElementLabel, anchor='w')
                
    # Element dropdown menu options
    weaponElements = [
            "Fire",
            "Water",
            "Earth",
            "Eternal"
            ]

    # Access the menu widget using StringVar function
    weaponElementClicked = StringVar()
                      
    # Create Element dropdown menu
    weaponElementDrop = OptionMenu(canvas, weaponElementClicked, *weaponElements)
    canvas.create_window(250, 370, window=weaponElementDrop)

##  AMULET SELECTION   
    amuletLabel = Label(canvas, text="Select Your Amulet Type:", fg='#1A5A14', bg='#DDE7EC')
    canvas.create_window(50, 430, window=amuletLabel, anchor='w')
                
    # Armor element dropdown menu options
    amulets = [
            "Fire",
            "Water",
            "Earth",
            "Eternal"
            ]

    # Access the menu widget using StringVar function
    amuletClicked = StringVar()
                      
    # Create Element dropdown menu
    amuletDrop = OptionMenu(canvas, amuletClicked, *amulets)
    canvas.create_window(250, 430, window=amuletDrop)

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
