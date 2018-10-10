a=['1','2','3','4','5','6','7','8','9']
def printBoard():
	print('\n......')
	print('|'+a[0]+'|'+a[1]+'|'+a[2]+'|')
	print('......')
	print('|'+a[3]+'|'+a[4]+'|'+a[5]+'|')
	print('......')
	print('|'+a[6]+'|'+a[7]+'|'+a[8]+'|')
	print('......\n')
p1=True
while(True):
	printBoard()
	if p1:
		p=input("Player 1,choose your place:")
		if p in a:
			a[int(p)-1]='X'
			p1=not p1
	else:
		p=input("Player 2,choose your place:")
		if p in a:
			a[int(p)-1]='0'
			p1=not p1
#checking for rows
for i in (0,3,6):
	if(a[i]==a[i+1] and a[i]==a[i+2]):
		if(a[i]=='X'):
			print("congrats Player1 won")
		else:
			print("congrats Player2 won")
			print("Game over...")
			printBoard()
			exit()
#checking for columns
for i in range(3):
	if(a[i]==a[i+3] and a[i]==a[i+6]):
		if(a[i]=='X'):
			print("congrats Player1 won")
		else:
			print("congrats Player2 won")
			print("Game over...")
			printBoard()
			exit()
#checking for diagonal 1
if(a[0]==a[4] and a[0]==a[8]):
	if(a[0]=='0'):
		print("congrats Player1 won")
	else:
		print("congrats Player2 won")
		print("game over..")
		printBoard()
		exit()

#checking for diagonal 2
if(a[2]==a[4] and a[2]==a[6]):
	if(a[2]=='0'):
		print("congrats Player1 won")
	else:
		print("congrats Player2 won")
		print("game over..")
		printBoard()
		exit()
else:
	print("u entered invalid position")
	

