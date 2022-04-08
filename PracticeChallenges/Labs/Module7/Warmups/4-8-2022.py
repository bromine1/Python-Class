class Vehicle:
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage

car = Vehicle

class Vehicle:
    def __init__(self, name, max_speed, mileage, color="red"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

class Car(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

Toyota = Car('Toyota', 60, 30)
Transportation = Bus('Wolfline', 40, 20)


print(Toyota.color)
print(Transportation.color)