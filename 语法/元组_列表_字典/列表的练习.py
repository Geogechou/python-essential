# 列表的练习、
# 3-5嘉宾名单
people=['Mother','Brother','Sister','grandpa']
print(people)
# 3-5修改嘉宾名单
busy_man='Brother'
people.remove(busy_man)
print(busy_man+" is too busy to come here")
people.append('grandma')
print(people)
# 3-6添加嘉宾
print('I get a bigger table, so we have to invite some others to dinner')
people.insert(0,'Friend1')
people.insert(2,'Friend2')
people.append('Friend3')
print(people)
# 3-7缩减名单
print("Our new table haven't send here, so sorry you guys")
print(people.pop()+" sorry")
print(people.pop()+' sorry')
print(people.pop()+' sorry')
print(people.pop()+' sorry')
print(people.pop()+' sorry')
print('I just invite two man to dinner')
print(people[0]+'   '+people[1])
del people[1]
del people[0]
print(people)

