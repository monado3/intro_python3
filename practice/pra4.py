print([number for number in range(5)])

rows = range(1, 4)
cols = range(1, 3)

for row in rows:
    for col in cols:
        print(row, col)

cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

for row, col in cells:
    print(row, col)

word = 'letters'
letter_count = {letter: word.count(letter) for letter in set(word)}

a_set = {number for number in range(5)}
print(a_set)

number_thing = (number for number in range(1, 5))
print(number_thing)
for number in number_thing:
    print(number)

number_list = list(number_thing)
print(number_list)


def do_nothing():
    pass


do_nothing()


def echo(anything):
    return anything + ' ' + anything


print(echo('abc'))


def menu(wine, entree, dessert):
    print({'wine': wine, 'entree': entree, 'dessert': dessert})


menu('chardonnay', 'chiken', 'cake')
menu(entree='beef', dessert='bagel', wine='bordeaux')


def menu1(wine, entree, dessert='pudding'):
    print({'wine': wine, 'entree': entree, 'dessert': dessert})


menu1('chardonnay', 'chicken')


def print_args(*args):
    print('Positional argument tuple', args)


print_args()
print_args(3, 2, 1, 'wait!', 'uh...')


def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too', required2)
    print('All the rest:', args)


print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')


def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)


print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')


def echo1(anything):
    'echoは、与えられた入力引数を返す'
    return anything


help(echo1)

print(echo1.__doc__)


def answer():
    print(42)


answer()


def run_something(func):
    func()


run_something(answer)

print(type(run_something))


def add_args(arg1, arg2):
    print(arg1 + arg2)


def sum_args(*args):
    print(sum(args))


sum_args(1, 2, 3, 3, 4, 5)


def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)


print(outer(4, 7))


def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    print(inner(saying))


knights('Ni!')


def knights2(saying):
    def inner2():
        return "We are the kights who say: '%s'" % saying
    return inner2


a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(type(a))
print(type(b))

print(a, b)

print(a(), b())


def edit_story(words, func):
    for word in words:
        print(func(word))


stairs = ['thud', 'meow', 'thud', 'hiss']


def enliven(word):
    return word.capitalize() + '!'


edit_story(stairs, enliven)

edit_story(stairs, lambda word: word.capitalize() + '!')

print(sum(range(1, 101)))


def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


ranger = my_range(1, 5)
print(ranger)

for x in ranger:
    print(x)


def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional aruguments:', args)
        print('Keyword arguments', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function


def add_ints(a, b):
    return(a + b)


add_ints(3, 5)

cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)


@document_it
def multi_int(a, b):
    return(a * b)


multi_int(3, 5)


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function


@document_it
@square_it
def add_ints1(a, b):
    return a + b


add_ints1(3, 5)

animal = 'fruitbat'


def print_global():
    print('inside print_global:', animal)


print('at the top level:', animal)
print_global()


def change_and_print_global():
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)
# change_and_print_global()


animal = 'fruitbat'


def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))


change_local()
print(id(animal))

animal = 'fruitbat'


def change_and_print_global1():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global1:', animal)


print(animal)
change_and_print_global1()

animal = 'fruitbat'


def change_local1():
    animal = 'wombat'
    print('locals:', locals())


change_local1()
print('globals:', globals())


def amazing():
    '''これはすばらしい関数だ。
    もう一度見る？'''
    print('この関数の名前:', amazing.__name__)
    print('docstring:', amazing.__doc__)


amazing()

short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]?')
    if value = 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index :', position)
    except Exception as other:
        print('Something else broke:', other)
