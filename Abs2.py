# import necessary packages 
from abc import ABC, abstractmethod
# create a base class 
class Animal(ABC):

    # absract method 
    # should be implemented by all sub_classes 
    def move(self):
        pass 

# sub classes 
class Human(Animal):

    def move(self):
        print("I can walk and run")

class Snakes(Animal):

    def move(self):
        print("I  can crawl")

class Dog(Animal):

    def move(self):
        print("I can bark")

class Lion(Animal):

    def move(self):
        print("I can roar")

# Driver code 
R = Human()
R.move()

K = Snakes()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()