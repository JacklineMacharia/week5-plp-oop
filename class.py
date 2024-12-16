#Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
#Add attributes and methods to bring the class to life!
#Use constructors to initialize each object with unique values
#Add an inheritance layer to explore polymorphism or encapsulation.

#A class representing a smartphone
class SmartPhone:
    #Attributes of the class Smartphone
    def __init__(self, product_type, color, year, space):
        self.color = color
        self.product_type = product_type
        self.space = space
        self.year = year


#methods
def inStock(self):
    return f"The {self.product_type} {self.color} {self.space} {self.year} is in stock."

def outOfStock(self):
    return f"The {self.product_type} {self.color} {self.space} {self.year} is out of stock."
        
smartPhone1 = SmartPhone("Samsung", "Blue", "32gb", 2024)
smartPhone2 = SmartPhone("Nokia", "Blue", "64gb", 2024)
smartPhone3 = SmartPhone("Itel", "Black", "32gb", 2024)
smartPhone4 = SmartPhone("Tecno", "Red", "168gb", 2024)
smartPhone5 = SmartPhone("Motorolla", "Black", "64gb", 2024)
 