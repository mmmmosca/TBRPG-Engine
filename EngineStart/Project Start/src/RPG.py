import subprocess
def fight(player_name,enemy_name,playerh,enemyh,playerd,enemyd,rheal,nheal):
	heals=nheal
	player = playerh
	enemy = enemyh
	while True:
		print("remaining heals: "+str(heals))
		print(f'{player_name}:	'+str(player))
		print(f'{enemy_name}:	'+str(enemy))
		turn=input('#: ')
		subprocess.call('clear')
		if(turn == 'att'):
			attack=playerd
			enemy=enemy-attack
			attack_enemy=enemyd
			player=player-attack_enemy
		elif(turn=='hel'):
			if(heals <= 0):
				player=player+0
				heals=heals-0
			elif(player >= playerh):
				player=player+0
				heals=heals-0
			else:
				player=player+rheal
				heals=heals-1
		if(player <= 0):
			print(f"{enemy_name} wins!")
			break
		elif(enemy <= 0):
			print(f'{player_name} wins')
			break
def story(storyfile):
	file=open(storyfile+'.sf','r')
	for line in file:
		print(line, end='')
def choice(choice1,choice2,anchoice1,anchoice2):
	print('1.'+choice1)
	print('2.'+choice2)
	choice=input('choice:')
	if(choice == choice1):
		print(anchoice1)
	elif(choice == choice2):
		print(anchoice2)