# 6-4,6-5,6-6练习
rivers={
	'nile':'egypt',
	'long river':'china',
	'mississippi':'USA'
}
for river,country in rivers.items():
	print("The "+str(river).title()+" runs through "+str(country))
print('\n')	
for river in rivers.keys():
	print(str(river).title())
print('\n')

for country in rivers.values():
	if str(country).lower()=='usa':
		print(str(country).upper())
	else:
		print(str(country).title())	

# ------------
favorite_languages={
	'Lee':'php',
	'Geoge':'python',
	'Hobby':'C',
	'Pluss':'C++'
}

persons=['lee','geoge','hobby']	
# 拷贝一份全部小写的副本，进行比较
persons_lower=[]
for person in persons:
	persons_lower.append(str(person).lower())
	
for user in favorite_languages.keys():
	if str(user).lower() in persons_lower:
		print('Thank you '+user)
	else:
		print('Come on '+user)	

