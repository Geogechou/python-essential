sandwich_orders=['A','b','pastrami','pastrami','C','pastrami','D']
finished_sandwiched=[]
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
	print('pastrami'+"has been deleted!")
while sandwich_orders:	
	temp=sandwich_orders.pop()
	print("I made you "+temp+" sandwich")
	finished_sandwiched.append(temp)
print("---------------------------------------------")	
for value in finished_sandwiched:
	print("I hava finished "+value)	
print('---------------------------------------------')
active_flag=True
dreamPlace={}
while active_flag:
	user=input("enter your name")
	place=input("If you could visit one place in"+
	 "the world,where would you go?")
	dreamPlace[user]=place;
	succeed=input("Do you wannna succeed?Y/N")
	if succeed.lower()=='n':
		active_flag=False
		
print("----------------------------------------------")
for key,value in dreamPlace.items():
	print(key+"------------"+value)	 
