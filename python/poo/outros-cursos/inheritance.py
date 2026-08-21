# Python Inheritance
# Bro Code
# 25/04/24

class Animal():
    
    alive = True

    def eat(self):
        print('This animal is eating')
    
    def sleep(self):
        print('This animal is sleeping')

class Rabbit(Animal):
    pass

class Hawk(Animal):
    pass

class Fish(Animal):
    pass



rabbit = Rabbit()

fish = Fish()

hawk = Hawk

print(rabbit.alive)