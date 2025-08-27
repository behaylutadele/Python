
# Activity 1: Design Your Own Class
# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")
    
    def charge(self):
        self.battery = 100
        print(f"{self.brand} {self.model} is fully charged! 🔋")

# Child Class (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system
    
    # Overriding method (Polymorphism)
    def charge(self):
        self.battery = 100
        print(f"{self.brand} {self.model} charges faster with {self.cooling_system}! ⚡")

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S22", "128GB", 50)
phone2 = GamingPhone("Asus", "ROG Phone 6", "256GB", 30, "Liquid Cooling")

# Test methods
phone1.call("0911223344")
phone2.charge()


#Activity 2: Polymorphism Challenge
class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Boat:
    def move(self):
        print("Sailing 🚤")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()

