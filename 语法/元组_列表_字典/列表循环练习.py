# 4-3数到20
for value in range(1,21):
	print(value)
numbers=[]	
#for value in range(1,1000000):
#	numbers.append(value)
#print(numbers)
#print(sum(numbers))
odd_number=[]
for value in range(1,20,2):
	odd_number.append(value)
print(odd_number)	
multi_three=[]
for value in range(3,30,3):
	multi_three.append(value)
print(multi_three)	
power_three=[]
for value in range(1,10):
	power_three.append(value**3)
print(power_three)	
power_three_analysis=[value**3 for value in range(1,10)]
print(power_three_analysis)
