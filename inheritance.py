"""
TYPES of Inheritance:-
1)Single Inheritance:-child class inherits from single parent class
2)Multiple Inheritance:-child class inherits from multiple parent class
3)Multilevel Inheritance:-child class inherits from parent class which also inherits from grandparents class
4)Heirarchial Inheritance:-single class is inherited in multiple child classes
5) Hybrid Inheritance:- combination of two or more inheritance types
"""

#=========SINGLE INHERITANCE============
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Animal makes a sound")


class Mammal:
    def __init__(self):
        print("Mammal can give birth to thier child")
    
    
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def speak(self):
        super().speak()#calls speak method from parent class
        print("Dog Barks")
    def show(self):
        print("Dog's Name:",self.name.capitalize())
        print("Dog's Name:",self.breed.capitalize())

ob=Dog("buddy","german shephard")
ob.speak()#function speak in dog overrides function speak in animal
ob.show()
    
#=========MULTILEVEL INHERITANCE by inheriting class Dog===========
#=========hybird inheritance as single and multilevel inheritance are being performed simultaneously
class puppy(Dog,Mammal):
    def __init__(self,name,breed):
        super().__init__(name,breed)
        Mammal.__init__(self)
        print("Puppy yelps")
ob1=puppy("kutte","labrador")

#=========MUlTIPLE INHERITANCE=============
class cow(Animal,Mammal):
    def __init__(self, name):
        Animal.__init__(self,name)
        Mammal.__init__(self)
        print(self.name)
        self.speak()
ob2=cow("gayya") 

#============hierarchial inheritance has been performed already as thier is only one parent with multiple child in this inheritance
"""
         Animal
       /       \
      /         \
    dog         cow
"""