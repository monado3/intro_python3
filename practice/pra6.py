class Person():
    pass
someone=Person()

class Person1():
    def __init__(self):
        pass

class Person2():
    def __init__(self,name):
        self.name=name

hunter=Person2('Elmer Fudd')
print('The mighty hunter:', hunter.name)

class Car():
    def exclaim(self):
        print("I'm a Car!")
class Yugo(Car):
    pass
give_me_a_car=Car()
give_me_a_yugo=Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

class Yugo1():
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
give_me_a_yugo1=Yugo1()
give_me_a_yugo1.exclaim()

class MDperson(Person2):
    def __init__(self,name):
        self.name='Doctor'+name
class JDPerson(Person2):
    def __init__(self,name):
        self.name=name+",Esquire"

class EmailPerson(Person2):
    def __init__(self,name,email):
        super().__init__(name)
        self.email=email
bob=EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name,bob.email)

class Duck():
    def __init__(self,input_name):
        self.hidden_name=input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self,input_name):
        print('inside the setter')
        self.hidden_name=input_name
    name=property(get_name, set_name)
fowl=Duck('Howard')
print(fowl.name)
fowl.get_name()
fowl.name='Daffy'
print(fowl.name)
fowl.set_name('daffy')
print(fowl.name)

class Duck1():
    def __init__(self,input_name):
        self.hidden_name=input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self,input_name):
        print('insdie the setter')
        self.hidden_name=input_name
fowl1=Duck1('Howard')
print(fowl1.name)
fowl.name='Donald'
print(fowl.name)

class Circle():
    def __init__(self, radius):
        self.radius=radius
    @property
    def diameter(self):
        return 2*self.radius
c=Circle(5)
print(c.radius)
print(c.diameter)

class Duck2():
    def __init__(self, input_name):
        self.__name=input_name
    @property
    def naming(self):
        return self.__name
    @naming.setter
    def name(self,input_name):
        self.__name=input_name
fowl2=Duck2('Howard2')
print(fowl2.naming)
fowl2.name='Donald2'
print(fowl2.naming)
print(fowl2._Duck2__name)

class A():
    count=0
    def __init__(self):
        A.count+=1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has",cls.count,"Little objects.")
easy_a=A()
breezy_a=A()
wheezy_a=A()
A.kids()

class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')

CoyoteWeapon.commercial()
class Quote():
    def __init__(self,person,words):
        self.person=person
        self.words=words
    def who(self):
        return self.person
    def says(self):
        return self.words+'.'

class QuestionQuote(Quote):
    def says(self):
        return self.words+'?'
class ExclamationQuote(Quote):
    def says(self):
        return self.words+'!'
class Bill():
    def __init__(self,description):
        self.description=description
class Tail():
    def __init__(self,length):
        self.length=length
class Duck():
    def __init__(self,bill,tail):
        self.bill=bill
        self.tail=tail
    def about(self):
        print('This duck has a',self.bill.description,\
        'bill and a', self.tail.length, 'tail')
tail=Tail('long')
bill=Bill('wide orange')
duck=Duck(bill,tail)
duck.about()
from collections import namedtuple
Duck=namedtuple('Duck','bill tail')
duck=Duck('wide orange','long')
print(duck)
