#write a program to print r to roll and q to quit
import random
while True:
	a=input("enter r to roll a dice and q to quit:")
	if(a=='r'):
		print(random.randint(1,6))
	elif(a=='q'):
		print("bye!")
		break
	else:
		print("give either r or q")