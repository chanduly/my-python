#write a program for snake and ladder
import random
c=0
while True:
	a=input("enter r to roll a dice and q to quit:")
	r=(random.randint(1,6))
	c=c+r
	c=11
	c=8
	if(c==11):
		   c=2
		   print("come down")
	elif(c==8):
			c=37
			print("climb")
	if(a=='r'):
		print(random.randint(1,6))
	elif(a=='q'):
		print("bye!")
		break
	else:
		print("give either r or q")