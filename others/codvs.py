class register:
    def __init__(self, name, age, weight, height):      
        self.name = name
        self.age = age 
        self.weight = weight
        self.height = height
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}kg, Height: {self.height}m"    
        
print("Enter your details below:")
name = input("Name: ")
age = input("Age: ")
weight = input("Weight (in kg): ")
height = input("Height (in meters): ")
user = register(name, age, weight, height)
print("\nYour details are:")
print(user)


    