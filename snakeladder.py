#write a program to play snake and ladder
import random
c=0
while True:
	r=random.randint(1,6)
	c=c+r
	if(c==8):
		c=37
		print("climb the ladder")
	elif(c==11):
		c=2
		print("snake has bitten u")	
	elif(c==13):
		c=34
		print("climb the ladder")
	

