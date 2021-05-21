# Fonts we like: Matura MT Script Capitals

from tkinter import *
import tkinter.messagebox
import tkinter.scrolledtext
from win_settings import *
import heroCreation as hc
import heroUpdate as hu
import os

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
    play_button = Button(window, text="Play now", bg='#1A5A14', activebackground='#0D2B0A', font=('Matura MT Script Capitals', 15), padx=2, pady=2, command=play_now)
    canvas.create_window(400,280, window=play_button)
    
    create_button = Button(window, text="Create hero", bg='#1A5A14', activebackground='#0D2B0A', font=('Matura MT Script Capitals', 13), padx=2, pady=2, command=create_now)
    canvas.create_window(400,335, window=create_button)

    exit_button = Button(window, text="Exit to desktop", bg='#69181F', activebackground='#4F1318', highlightcolor='green', font=('Matura MT Script Capitals', 10), padx=0, pady=0, command=close_window)
    canvas.create_window(400,380, window=exit_button)

# clear canvas for the game interface
def create_now():
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


    # ARMOUR SELECTION   
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

    # WEAPON SELECTION 
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

    # ELEMENT SELECTION    
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

    # AMULET SELECTION   
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

# PLAY NOW SCREEN
def play_now():
    chkFile = "interfaceSave.txt"
    if os.path.isfile(chkFile):
        # clear canvas in order to start fresh
        canvas.delete('all')
        canvas.configure(bg='#DDE7EC')

        # creates canvas
        rightFrame = Frame(bg='grey')
        canvas.create_window(430,5, window=rightFrame, height=590, width=368, anchor='nw')

        statsFrame = Frame(bd=2, bg='grey', relief=RAISED)
        canvas.create_window(435, 40, window=statsFrame, height=105, width=360, anchor='nw')

        # main menu button
        main_menu_button = Button(window, text="Main Menu", command=go_menu)
        canvas.create_window(760,20, window=main_menu_button)

        # create scrolling console box
        text2Print = tkinter.scrolledtext.ScrolledText(window, height=23, width=40, fg='#1A5A14', bg='#9BB0C4', font=('Calibri', 15))
        canvas.create_window(5, 5, window=text2Print, anchor='nw')

    else:
        tkinter.messagebox.showinfo("Whoops!", "It looks like you have not created a hero yet! Click \"Create Hero\" first.")

    userEntry = StringVar()
    userTextBar = Entry(canvas, justify=LEFT, textvariable=userEntry, width=50, bg='#9BB0C4')
    canvas.create_window(5, 580, window=userTextBar, anchor='w')
    userTextBar.focus_set()
    
    OPTIONS_LIST = ["Fight Mobs", "Add Points", "Visit Merchant", "Coin Flip", "Change floor level",  "Exit"]
    OPTIONS_DICT = dict(enumerate(OPTIONS_LIST, start=1))
    PROMPT = "\n".join("\t%d. %s"%n for n in OPTIONS_DICT.items())
    
    text2Print.insert(INSERT, "What would you like to do?\n\n")
    text2Print.insert(INSERT, PROMPT + "\n")
    text2Print.insert(INSERT, "------------------------------------------------------------------\n")
    
    # LIVE STATS
    file = open('interfaceSave.txt','r+')
    lines = file.readlines()

    displayName = Label(rightFrame, text=lines[0].rstrip('\n') + "'s Stats", borderwidth=8, fg='#1A5A14', bg='grey', font=('Matura MT Script Capitals', 12))
    displayName.grid(row=0, padx=125)

    displayHealth = Label(statsFrame, text="Health: ", borderwidth=1, fg='#1A5A14', bg='#808080')
    displayHealth.grid(row=1, column=0, ipadx=3, ipady=3, sticky=E)
    healthStat = Label(statsFrame, text=lines[1].rstrip('\n'), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
    healthStat.grid(row=1, column=1, ipadx=3, ipady=3, sticky=W)

    displayMelee = Label(statsFrame, text="Melee: ", borderwidth=1, fg='#1A5A14', bg='#808080')
    displayMelee.grid(row=1, column=3, ipadx=3, ipady=3, sticky=E)
    meleeStat = Label(statsFrame, text=lines[2].rstrip('\n'), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
    meleeStat.grid(row=1, column=4, ipadx=3, ipady=3, sticky=W)

    displayRanged = Label(statsFrame, text="Ranged: ", borderwidth=1, fg='#1A5A14', bg='#808080')
    displayRanged.grid(row=2, column=0, ipadx=3, ipady=3, sticky=E)
    rangedStat = Label(statsFrame, text=lines[3].rstrip('\n'), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
    rangedStat.grid(row=2, column=1, ipadx=3, ipady=3, sticky=W)

    displayMagic = Label(statsFrame, text="Magic: ", borderwidth=1, fg='#1A5A14', bg='#808080')
    displayMagic.grid(row=2, column=3, ipadx=3, ipady=3, sticky=E)
    magicStat = Label(statsFrame, text=lines[4].rstrip('\n'), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
    magicStat.grid(row=2, column=4, ipadx=3, ipady=3, sticky=W)

    displayPoints = Label(statsFrame, text="Points: ", borderwidth=1, fg='#1A5A14', bg='#808080')
    displayPoints.grid(row=3, column=0, ipadx=3, ipady=3, sticky=E)
    pointsStat = Label(statsFrame, text=lines[5].rstrip('\n'), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
    pointsStat.grid(row=3, column=1, ipadx=3, ipady=3, sticky=W)

    displayExp = Label(statsFrame, text="EXP: ", borderwidth=1, fg='#1A5A14', bg='#808080')
    displayExp.grid(row=3, column=3, ipadx=3, ipady=3, sticky=E)
    expStat = Label(statsFrame, text=lines[10].rstrip('\n') + "/" + str(float(10+(float(lines[11].rstrip('\n')) ** 2))), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
    expStat.grid(row=3, column=4, ipadx=3, ipady=3, sticky=W)

    displayLvl = Label(statsFrame, text="Player Level: ", borderwidth=1, fg='#1A5A14', bg='#808080')
    displayLvl.grid(row=4, column=0, ipadx=3, ipady=3, sticky=E)
    lvlStat = Label(statsFrame, text=lines[11].rstrip('\n'), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
    lvlStat.grid(row=4, column=1, ipadx=3, ipady=3, sticky=W)

    displayFloor = Label(statsFrame, text="Floor Level: ", borderwidth=1, fg='#1A5A14', bg='#808080')
    displayFloor.grid(row=4, column=3, ipadx=3, ipady=3, sticky=E)
    floorStat = Label(statsFrame, text=lines[12].rstrip('\n'), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
    floorStat.grid(row=4, column=4, ipadx=3, ipady=3, sticky=W)

    # LIVE UPDATE THE PLAYERS STATS
    def updateStats(statsFrame):
        file = open('interfaceSave.txt','r+')
        lines = file.readlines()

        tempFrame = statsFrame
        tempFrame.destroy()
        statsFrame = Frame(bd=2, bg='grey', relief=RAISED)
        canvas.create_window(435, 40, window=statsFrame, height=105, width=360, anchor='nw')

        displayName = Label(rightFrame, text=lines[0].rstrip('\n') + "'s Stats", borderwidth=8, fg='#1A5A14', bg='grey', font=('Matura MT Script Capitals', 12))
        displayName.grid(row=0, padx=125)

        displayHealth = Label(statsFrame, text="Health: ", borderwidth=1, fg='#1A5A14', bg='#808080')
        displayHealth.grid(row=1, column=0, ipadx=3, ipady=3, sticky=E)
        healthStat = Label(statsFrame, text=lines[1].rstrip('\n'), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
        healthStat.grid(row=1, column=1, ipadx=3, ipady=3, sticky=W)

        displayMelee = Label(statsFrame, text="Melee: ", borderwidth=1, fg='#1A5A14', bg='#808080')
        displayMelee.grid(row=1, column=3, ipadx=3, ipady=3, sticky=E)
        meleeStat = Label(statsFrame, text=lines[2].rstrip('\n'), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
        meleeStat.grid(row=1, column=4, ipadx=3, ipady=3, sticky=W)

        displayRanged = Label(statsFrame, text="Ranged: ", borderwidth=1, fg='#1A5A14', bg='#808080')
        displayRanged.grid(row=2, column=0, ipadx=3, ipady=3, sticky=E)
        rangedStat = Label(statsFrame, text=lines[3].rstrip('\n'), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
        rangedStat.grid(row=2, column=1, ipadx=3, ipady=3, sticky=W)

        displayMagic = Label(statsFrame, text="Magic: ", borderwidth=1, fg='#1A5A14', bg='#808080')
        displayMagic.grid(row=2, column=3, ipadx=3, ipady=3, sticky=E)
        magicStat = Label(statsFrame, text=lines[4].rstrip('\n'), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
        magicStat.grid(row=2, column=4, ipadx=3, ipady=3, sticky=W)

        displayPoints = Label(statsFrame, text="Points: ", borderwidth=1, fg='#1A5A14', bg='#808080')
        displayPoints.grid(row=3, column=0, ipadx=3, ipady=3, sticky=E)
        pointsStat = Label(statsFrame, text=lines[5].rstrip('\n'), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
        pointsStat.grid(row=3, column=1, ipadx=3, ipady=3, sticky=W)

        displayExp = Label(statsFrame, text="EXP: ", borderwidth=1, fg='#1A5A14', bg='#808080')
        displayExp.grid(row=3, column=3, ipadx=3, ipady=3, sticky=E)
        expStat = Label(statsFrame, text=lines[10].rstrip('\n') + "/" + str(float(10+(float(lines[11].rstrip('\n')) ** 2))), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
        expStat.grid(row=3, column=4, ipadx=3, ipady=3, sticky=W)

        displayLvl = Label(statsFrame, text="Player Level: ", borderwidth=1, fg='#1A5A14', bg='#808080')
        displayLvl.grid(row=4, column=0, ipadx=3, ipady=3, sticky=E)
        lvlStat = Label(statsFrame, text=lines[11].rstrip('\n'), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
        lvlStat.grid(row=4, column=1, ipadx=3, ipady=3, sticky=W)

        displayFloor = Label(statsFrame, text="Floor Level: ", borderwidth=1, fg='#1A5A14', bg='#808080')
        displayFloor.grid(row=4, column=3, ipadx=3, ipady=3, sticky=E)
        floorStat = Label(statsFrame, text=lines[12].rstrip('\n'), borderwidth=1, fg='#1A5A14', bg='#808080', relief=SUNKEN)
        floorStat.grid(row=4, column=4, ipadx=3, ipady=3, sticky=W)

    # IF ENTER BUTTON IS CLICKED
    def enterTextClick(event=None):
        # retrieve what the user typed
        CHOICE = userEntry.get()

        # insert user's entry into the console
        text2Print.insert(INSERT, CHOICE + '\n')
        text2Print.insert(INSERT, "------------------------------------------------------------------\n")
        userTextBar.delete(0, 'end')

        # scroll the bar with the text entrys
        text2Print.yview('end')

        # update stats
        updateStats(statsFrame)

        # if CHOICE in OPTIONS_DICT.keys():
        #    CHOICE = OPTIONS_DICT[CHOICE]
        if CHOICE == "1":
            # mob = Monster(int(hero_obj.floor_level), random.choice(mob_list), random.choice(elements_list))
            # combat.combatSequence(hero_obj, mob)
            # mob2 = Monster(int(hero_obj.floor_level), random.choice(mob_list), random.choice(elements_list))
            # combat.combatSequence(hero_obj, mob2)
            # mob3 = Monster(int(hero_obj.floor_level), random.choice(mob_list), random.choice(elements_list))
            # combat.combatSequence(hero_obj, mob3)
            # print("Get ready for the Boss!")
            # mob4= Boss((int(hero_obj.floor_level) +1), random.choice(mob_list), random.choice(elements_list))
            # combat.combatSequence(hero_obj, mob4)
            text2Print.insert(INSERT, "fighting mobs \n")
        elif CHOICE == "2":
            # hu.add_points(hero_obj)
            text2Print.insert(INSERT, "adding points \n")
        elif CHOICE == "3":
            # me.merchant(hero_obj)
            text2Print.insert(INSERT, "visiting merchant \n")
        elif CHOICE == "4":
            # me.coinFlip(hero_obj)
            text2Print.insert(INSERT, "flipping coin \n")
        elif CHOICE == "5":
            text2Print.insert(INSERT, "What floor level would you like? \n")
            # floorChoice = the next input
            # if floorChoice is not valid:
                # text2Print.insert(INSERT, "please enter a valid floor number \n")
            # else:
                # write to file to update floor
                # text2Print.insert(INSERT, "floor updated! \n")
                
            # hero_obj.floor_level = int(tmp_level)
        elif CHOICE == "6":
            # running = False
            text2Print.insert(INSERT, "Exiting \n")
            close_window()
            
        text2Print.insert(INSERT, "------------------------------------------------------------------\n")

    # IF RETURN BUTTON IS PUSHED
    def enterTextReturn(event):
        pass

    # enter button for console text
    userEnterText = Button(window, text="Enter", command=enterTextClick, bg='#1A5A14', font=('Matura MT Script Capitals', 10), width=10)
    canvas.create_window(315, 580, window=userEnterText, anchor='w')

    # bind return key
    window.bind('<Return>', enterTextClick)
    
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
