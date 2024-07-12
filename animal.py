class Animal(object):
    def echo(self):
        print("Animal")


class Dog(Animal):
    def __init__(self, name):
        self.__name = name

    def echo(self):
        print("Dog-" + self.__name)


class Cat(Animal):
    def __init__(self, name):
        self.__name = name

    def echo(self):
        print("Cat-" + self.__name)


animal = Dog("wongwong")
animal.echo()

animal = Cat("miaomiao")
animal.echo()


class Person(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


p = Person("liuheng")
print(p.name)
p.name = "lucas"
print(p.name)
