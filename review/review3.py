years_list=[x for x in range(1997,1997+6)]
print(years_list)

print(years_list[3])

print(years_list[-1])

things=['mozzarella','cinderella','salmonella']

things[1].capitalize()
print(things)

things[1]=things[1].capitalize()
print(things)

things[0]=things[0].upper()
print(things)

del things[-1]
print(things)

surprise=['Groucho','Chico','Harpo']
print(surprise)

surprise[-1]=surprise[-1].lower()[::-1].capitalize()
print(surprise)

e2f={'dog':'chein','cat':'chat','walrus':'morse'}
print(e2f)

print(e2f['walrus'])

f2e={}
for english,french in e2f.items():
    f2e[french]=english
print(f2e)

print(f2e['chein'])

print(set(e2f.keys()))

life={'animals':{'cats':['Henri','Grumpy','Lucy'],'octopi':{},'emus':{}},'plants':{},'other':{}}
print(life)

print(life.keys())

print(life['animals'].keys())

print(life['animals']['cats'])
