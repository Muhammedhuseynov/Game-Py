# BASIC GAME --> 
                # Angel Kill Monster 
import random
# MAKE WHILE LOOP
game = True

while game == True:
	# for restart
	new_game = True

	# HEROS random attacks
	mons_attack = random.randint(6,14)
	ang_attack = random.randint(5,13)

	# make HEROS :> with dictionary
	monster  = {'health':100,'attack':mons_attack}
	angel  = {'health':100,'attack':ang_attack}
	
	# for user make input
	

	# And here start our game Logic
	while new_game == True:
		print('/ Angel Kill Monster /\nChoose your Hero!\n 1)Monster\n 2)Angel\n > e <) for Exit \n')
		user = input(' />')
		if user == str(1):
		    # MONSTER WILL attacking 
		    angel['health'] = angel['health'] - monster['attack']
		    print(f' ---  Monster Attacked ---->>   -- Angel Health: {angel["health"]}% -- \n')

		    # for: if Dead
		    if angel['health']  <= 0:
		    	print('> Angel Dead < \n Monster won Bro!!! \n > 5 <)For Exit \n For Restart: Any Key ')
		    	# we don't need attacking
		    	new_game = False

		    	# Then ask from user : FOR continuing
		    	user_chance = input('\n/>')
		    	if user_chance == '5':
		    		print(' -- It was Greate Bottle --\n  - See you Later -')
		    		new_game = False
		    		game = False
		    	else:
		    		pass

		# Same logic with Angel   But input > 2 : Angel< 
		elif user == str(2):
		    # ANGEL WILL attacking 
		    monster['health'] = monster['health'] - angel['attack']
		    print(f' ---  Angel Attacked ---->>   -- Monster Health: {monster["health"]}% -- \n')

		    # for: if Dead
		    if monster['health']  <= 0:
		    	print('> Monster Dead < \n Angel won Bro!!! \n > 5 <)For Exit \n For Restart: Any Key ')
		    	# we don't need attacking
		    	new_game = False

		    	# Then ask from user : FOR continuing
		    	user_chance = input('\n/>')
		    	# if user e > Game over
		    	if user_chance == '5':
		    		print(' -- It was Greate Bottle --\n  - See you Later -')
		    		new_game = False
		    		game = False
		    	else:
		    		pass
		# Exit From game    	    	 
		elif user == 'e':
			print(' -- See you Later --')
			new_game = False
			game = False
		else:
			print('\n >> InCorrect Value!!! < \n')        	       