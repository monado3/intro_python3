guess_me=7
start=1
while True:
    if start<guess_me:
        print('too low')
    elif start==guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    start+=1

for num in [3,2,1,0]:
    print(num)

print([num for num in range(10) if num%2==0])

squares={value:value**2 for value in range(10)}
print(squares)

odd={num for num in range(10) if num%2==1}
print(odd)

for num in (number for number in range(10)):
    print('Got ',num)

def good():
    return ['Harry','Ron','Hermione']

def get_odds():
    for num in range(1,10,2):
        yield num
for count,number in enumerate(get_odds(),1):
    if count==3:
        print(number)

def test(func):
    def new_func(*args,**kwargs):
        print('start')
        result=func(*args,**kwargs)
        print('end')
        return result
    return new_func

@test
def greeting():
    print('a','b')

greeting()

titles=['Creature of Habit','Crewel Fate']
plots=['A nun turns into a monster', 'A haunted yarn shop']
movies=dict(zip(titles,plots))
print(movies)
