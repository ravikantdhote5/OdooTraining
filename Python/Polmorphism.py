

#Method Overriding
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):  # Overrides the parent method
        print("Car is starting")


v = Vehicle()
v.start()   # Output: Vehicle is starting

c = Car()
c.start()   # Output: Car is starting


#Method Overloading
class Calculator:
    def add(self, *args):
        if len(args) == 0:
            return 0
        else:
            return sum(args)
calc = Calculator()

print(calc.add())             # Output: 0
print(calc.add(5))            # Output: 5
print(calc.add(3, 4, 7))      # Output: 14


#Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(2, 3)
p2 = Point(4, 5)

result = p1 + p2

print("Result Point:")
print("x =", result.x)
print("y =", result.y)
