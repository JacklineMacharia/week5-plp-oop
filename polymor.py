#Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Animal:
    def __init__(self, name, color, gender):
        self.name = name
        self.color = color
        self.gender = gender
        
    def __str__(self):
        return f"{self.__clas__.__name__}: {self.name}, Color: {self.color}, Gender: {self.gender}"
    
    #Polymorphism
    def move(self):
        raise NotImplementedError("This method should be overriden by sub....")
    
#Inheritance
class Pet(Animal):
    def __init__(self, name, color, gender, classification):
        super().__init__(name, color, gender)
        self.classification = classification
        
        def move(self):
            return f"{self.name} is walking."

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
        def __str__(self):
            return f"{self.__clas__.__name__}: {self.make} {self.model}"
        
        #Polymorphism method
        def move(self):
            raise NotImplementedError("This method should be overridden")
        
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"
    
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"
    
puppy = Pet("Brey", "white", "male", "Dog")
car = Car("Toyota", "Corolla")
plane = Plane("Boeing", "747")

objects = [puppy, car, plane]

for obj in objects:
    print(f"{obj}: {obj.move()}")