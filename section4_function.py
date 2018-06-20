def do_nothing():
    pass

do_nothing

def make_a_sound():
    print('quack')

make_a_sound()

def agree():
    return True

if agree():
    print('Splendid!')

def echo(anything):
    return anything+' '+anything

print(echo('abc'))

#Noneは役に立つ
thing=None
if thing:
    print("It's some thing")
else:
    print("It's no thing")

def menu(wine,entree,dessert):
    return {'wine':wine,'entree':entree,'dessert':dessert}

print(menu('chardonnay','chiken','cake'))

print(menu(entree='beef',wine='bordeaux',dessert='bagel'))
