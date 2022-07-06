from os import POSIX_SPAWN_DUP2
from xml.sax.xmlreader import AttributesImpl


numbers = [3, 90, 9, 12, 114, 16, 55]

def flatten_sort(numbers):
    print(sorted(numbers))

flatten_sort(numbers)

# The way the above code is written is working code but I believe is it 
#mutiable. I have to turn it into a string or tuple to make it immutable. 

#Yes it is a pure function. It does one thing only. 
#No my function is not a higher order function, there is only one function here, I did not add a function as an agruement. I believe this 
#style is find for this type of code but JS would probably be better 
#safer/ more secure code.
#Functional programming allows for multiple functions to be used inside of other functions. This allows for easier/cleaner programming skills.

#OOP

# Class podracers max_speed condition of car: perfect, trashed, repaired
# Price Attribute

# Define a repair() method that will update the condition of 

# pod1 = Podracers(250, 'repaired', 100000)
# pod2 = Podracers(300, 'perfect', 200000)    
# pod3 = Podracers(200, 'trashed', 50000)
class Podracers: 
    def __init__(self, name, max_speed, condition_of_car, price):
        self.name = name
        self.max_speed = max_speed
        self.condition_of_car = condition_of_car
        self.__price = price

    def __repr__(self):
        return f"{self.name}, Max Speeds: {self.max_speed}, Condition of car: {self.condition_of_car}, Price: {self.__price} "

class repair(Podracers):
    def __init__(self, condition_of_car):
        fixed.condition_of_car = condition_of_car
        if condition_of_car is "trashed":
                print("repaired")
        else:
                print("Awwww Damn it's not done yet!")
fixed = "repaired"

pod1 = Podracers("Pod1:", 250, 'repaired', 100000)
pod2 = Podracers("Pod2:", 300, 'perfect', 200000)    
pod3 = Podracers("Pod3:", 200, 'trashed', 50000)
class AnakinsPods(Podracers):
    def __init__(self, name, max_speed, condition_of_car, price):
        super().__init__(name, max_speed, condition_of_car, price)

    def __repr__(self):
        return f"Max Speeds: {self.max_speed}, Condition of car: {self.condition_of_car}, Price: {self.__price} "
        
print(pod1)
print(pod2) 
print(pod3)
print(fixed.replace("trashed", "repaired"))