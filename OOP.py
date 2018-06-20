"""
https://www.datacamp.com/community/tutorials/python-oop-tutorial
"""


class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    def birthday(self):
        self.age += 1

    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self

    def eat(self):
        print('yummy!')

d = Dog('Ozzy', 11)

d.bark()

d.eat()