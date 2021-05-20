import mobs
import heroUpdate as hu
import random



def damageDone(hero, monster):
    playerDamageType                    = ''
    playerElementType                   = ''
    mobDamageType                       = monster.mob_class
    mobElementType                      = monster.mob_class
    damage_multiplier                   = 1.0
    dmg                                 = 0.0


    if(hero.weapon.item_element == "eternal"):
        playerElementType = 'eternal'
    elif(hero.weapon.item_element == "fire"):
        playerElementType = 'fire'
    elif(hero.weapon.item_element == "water"):
        playerElementType = 'water'
    elif(hero.weapon.item_element == "earth"):
        playerElementType = 'earth'

    if(hero.player_class == 'Brute'):
        if(mobDamageType == 'Brute'):
            damage_multiplier += 0.0
        if(mobDamageType == 'Archer'):
            damage_multiplier += 0.2
        if(mobDamageType == 'Warlock'):
            damage_multiplier -= 0.2
    elif(hero.player_class == 'Archer'):
        if(mobDamageType == 'Brute'):
            damage_multiplier -= 0.2
        if(mobDamageType == 'Archer'):
            damage_multiplier += 0.0
        if(mobDamageType == 'Warlock'):
            damage_multiplier += 0.2
    elif(hero.player_class == 'Warlock'):
        if(mobDamageType == 'Brute'):
            damage_multiplier += 0.2
        if(mobDamageType == 'Archer'):
            damage_multiplier -= 0.2
        if(mobDamageType == 'Warlock'):
            damage_multiplier += 0.0
    #print(damage_multiplier)
    if(playerElementType == 'eternal'):
        damage_multiplier += 0.5
    elif(playerElementType == 'fire'):
        if(mobElementType == 'fire'):
            damage_multiplier += 0.0
        if(mobElementType == 'water'):
            damage_multiplier -= 0.3
        if(mobElementType == 'earth'):
            damage_multiplier += 0.3
    elif(playerElementType == 'water'):
        if(mobElementType == 'fire'):
            damage_multiplier += 0.3
        if(mobElementType == 'water'):
            damage_multiplier += 0.0
        if(mobElementType == 'earth'):
            damage_multiplier -= 0.3
    elif(playerElementType == 'earth'):
        if(mobElementType == 'fire'):
            damage_multiplier -= 0.3
        if(mobElementType == 'water'):
            damage_multiplier += 0.3
        if(mobElementType == 'earth'):
            damage_multiplier += 0.0
    #print(damage_multiplier)
    if(hero.player_class == 'Brute'):
        dmg = hero.melee  * damage_multiplier
    elif(hero.player_class == 'Archer'):
        dmg = hero.ranged  * damage_multiplier
    elif(hero.player_class == 'Warlock'):
        dmg = hero.magic  * damage_multiplier

    return round(dmg, 2)



def damageReceived(hero, monster):
    playerDamageType                    = ''
    playerElementType                   = ''
    mobDamageType                       = monster.mob_class
    mobElementType                      = monster.mob_class
    damage_multiplier                   = 1.0
    dmg                                 = 0.0


    if(hero.armor.item_element == "eternal"):
        playerElementType = 'eternal'
    elif(hero.armor.item_element == "fire"):
        playerElementType = 'fire'
    elif(hero.armor.item_element == "water"):
        playerElementType = 'water'
    elif(hero.armor.item_element == "earth"):
        playerElementType = 'earth'

    if(hero.player_class == 'Brute'):
        if(mobDamageType == 'Brute'):
            damage_multiplier += 0.0
        if(mobDamageType == 'Archer'):
            damage_multiplier += 0.2
        if(mobDamageType == 'Warlock'):
            damage_multiplier -= 0.2
    elif(hero.player_class == 'Archer'):
        if(mobDamageType == 'Brute'):
            damage_multiplier -= 0.2
        if(mobDamageType == 'Archer'):
            damage_multiplier += 0.0
        if(mobDamageType == 'Warlock'):
            damage_multiplier += 0.2
    elif(hero.player_class == 'Warlock'):
        if(mobDamageType == 'Brute'):
            damage_multiplier += 0.2
        if(mobDamageType == 'Archer'):
            damage_multiplier -= 0.2
        if(mobDamageType == 'Warlock'):
            damage_multiplier += 0.0
    #print(damage_multiplier)
    if(mobElementType == 'eternal'):
        damage_multiplier += 0.5
    elif(mobElementType == 'fire'):
        if(playerElementType == 'fire'):
            damage_multiplier += 0.0
        if(playerElementType == 'water'):
            damage_multiplier -= 0.3
        if(playerElementType == 'earth'):
            damage_multiplier += 0.3
    elif(mobElementType == 'water'):
        if(playerElementType == 'fire'):
            damage_multiplier += 0.3
        if(playerElementType == 'water'):
            damage_multiplier += 0.0
        if(playerElementType == 'earth'):
            damage_multiplier -= 0.3
    elif(mobElementType == 'earth'):
        if(playerElementType == 'fire'):
            damage_multiplier -= 0.3
        if(playerElementType == 'water'):
            damage_multiplier += 0.3
        if(playerElementType == 'earth'):
            damage_multiplier += 0.0
    #print(damage_multiplier)
    dmg = monster.level * damage_multiplier


    return round(dmg, 2)




def combatSequence(hero, monster):
    currHealth = hero.health
    running = True
    print("--------------------------------------------------------")
    print ("You have entered combat against a level " + str(monster.level) + " " + str(monster.mob_class)+ ".")
    OPTIONS_LIST = ["Attack", "Run Away"]
    OPTIONS_DICT = dict(enumerate(OPTIONS_LIST, start=1))
    PROMPT = "\n".join("\t%d. %s"%n for n in OPTIONS_DICT.items())+"\nChoice:"
    while (running):
        if(currHealth <= 0):
            print('You have been badly injured are being rushed to the infirmary. \nYou lost half your gold.')
            hero.bank /= 2
            running = False
        else:
            print('You have '+ str(round(currHealth, 2)) + ' health.')
            print('Enemy has '+ str(round(monster.health, 2)) + ' health.')
            CHOICE = input(PROMPT)
            print("--------------------------------------------------------")
            try:
                CHOICE = int(CHOICE)
            except:
                pass
            if CHOICE in OPTIONS_DICT.keys():
                CHOICE = OPTIONS_DICT[CHOICE]
            if CHOICE == "Attack":
                currAttack = damageDone(hero, monster)
                print('You did '+ str(currAttack) + ' damage.\n')
                monster.health -= float(currAttack)
                if(monster.health > 0):
                    dmgReceived = damageReceived(hero, monster)
                    print('The '+ str(monster.mob_class) + ' did ' + str(dmgReceived) + ' damage.\n')
                    currHealth -= dmgReceived
                elif(monster.health <= 0):
                    hu.increaseXP(monster.level,hero)
                    gold = random.randint(0,monster.level)
                    hu.addGold(gold, hero)
                    print('The monster has died.\n')
                    print('You gained', monster.level, 'experience and', gold, 'gold.\n')
                    running = False

            elif CHOICE == "Run Away":
                print('You fled to safety.')
                running = False
