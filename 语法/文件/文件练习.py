filename='guest_book.txt'
"""

with open(filename,'w') as file_object:
	name=input("enter your name: ")
	file_object.write(name)

"""
i=0
while i in range(3):
	with open(filename,'a') as file_object:
		reason=input("Why you like program?")
		reason+='\n'
		file_object.write(reason)
		i+=1
