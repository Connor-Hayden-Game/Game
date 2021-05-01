import mobs
import heroUpdate as hu




def damageDone(hero, monster):
	playerDamageType 					= ''
	playerElementType 					= ''
	mobDamageType 						= monster.mob_class
	mobElementType 						= monster.mob_class
	damage_multiplier 					= 1.0
	dmg 								= 0.0


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
	print(damage_multiplier)
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
	print(damage_multiplier)
	if(hero.player_class == 'Brute'):
		dmg = hero.melee  * damage_multiplier 
	elif(hero.player_class == 'Archer'):
		dmg = hero.ranged  * damage_multiplier	
	elif(hero.player_class == 'Warlock'):
		dmg = hero.magic  * damage_multiplier

	return dmg



# def damageRecieved(hero, mob):
	
