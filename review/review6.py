class Thing():
    pass
print(Thing)
example=Thing()
print(example)

class Thing2():
    letters='abc'
print(Thing2.letters)

class Things3():
    def  __init__(self):
        self.letters='xyz'
thing3=Things3()
print(thing3.letters)

class Element():
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number
element1=Element('Hydrogen','H',1)

dic1={'name':'Hydrogen','symbol':'H','number':1}
element2=Element(**dic1)
print(element2.name,element2.symbol,element2.number)

class Element2():
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number
    def __str__(self):
        return 'name='+self.name + self.symbol + str(self.number)
hydrogen=Element2(**dic1)
#hydrogen.dump()

print(hydrogen)

class Element3():
    def __init__(self,name,symbol,number):
        self.__name=name
        self.__symbol=symbol
        self.__number=number
    @property
    def namae(self):
        return self.__name
    @property
    def kigou(self):
        return self.__symbol
    @property
    def banngou(self):
        return self.__number
hydrogen3=Element3('Hydrogen','H',1)
print(hydrogen3.namae,hydrogen3.kigou)

class Bear():
    def eats(self):
        return 'berries'
class Rabbit():
    def eats(self):
        return 'Clover'
class Octothorpe():
    def eats(self):
        return 'campers'
a,b,c=Bear(),Rabbit(),Octothorpe()
print(a.eats(),b.eats(),c.eats())

class Laser():
    def does(self):
        return 'disintegrate'
class Claw():
    def does(self):
        return 'crush'
class Smartphone():
    def does(self):
        return 'ring'
class Robot():
    def __init__(self):
        self.laser=Laser()
        self.claw=Claw()
        self.smartphone=Smartphone()
    def does(self):
        return self.laser.does(),\
        self.claw.does(),\
        self.smartphone.does()
robbie=Robot()
print(robbie.does())
