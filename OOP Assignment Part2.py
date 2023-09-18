# Assignment 6 - JSON and OOP Assignment

# Part 2 Create an assignment using OOP concept

'''
Create a class named Dog. It should have a constructor which accepts its name, age and coat color. 
You must perform the following operations:
1. It should have a function description() which prints the name and age of the dog.
2. It should have a function get_info() which prints the coat color of the dog.
3. Create child classes JackRussellTerrier and Bulldog which is inherited from the class Dog. 
It should have at least two methods of its own.
4. Create objects and implement the above functionalities.
'''

class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    def description(self):
        print('Name of the Dog: ',self.name)
        print('Age of the Dog: ',self.age,' months old')
    
    def get_info(self):
        print('Coat color of dog: ',self.color)

class JackRusellTerrier(Dog):
    def __init__(self, name, age, color):
        super().__init__(name,age,color)
        
    def Details(self):
        super().description()
        super().get_info()
        
    def Info(self):
        print(f'My Dog {self.name} is telling something as woof-woof, which means ')
        self.Details()
    
class Bulldog(Dog):
    def __init__(self, name, age, color):
        super().__init__(name,age,color)
        
    def Details(self):
        super().description()
        super().get_info()
    
    def Info(self):
        print(f'My Dog {self.name} is telling something as woof-woof, which means ')
        self.Details()

jrt = JackRusellTerrier('Lovely',6,'white')
jrt.Info()
print()
bd = Bulldog('Shamba',3,'Black')
bd.Info()
