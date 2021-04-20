#testing function implementation
import heroCreation as hc
import heroUpdate as hu
import itemCreation as ic



class Hero(object):
    f = open('save.txt','r').read().splitlines()
    name                = f[0]
    health              = int(f[1])
    melee               = int(f[2])
    ranged              = int(f[3])
    magic               = int(f[4])
    points              = int(f[5])
    bank                = int(f[6])
    armor               = ic.Item(f[7], f[8], f[9], f[10])
    weapon              = ic.Item(f[11], f[12], f[13], f[14])
    amulet              = ic.Item(f[15], f[16], f[17], f[18])
    experience          = int(f[19])
    player_level        = int(f[20])
    floor_level         = int(f[21])
    #inventory           = list(f[22])


hero_obj = Hero()

#hu.addToInv(ic.random_item(hero_obj), hero_obj)
hu.equipToSlot(ic.random_item(hero_obj), hero_obj)






