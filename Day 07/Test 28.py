"""Day 07 OOP """

# Create a base class named Vehicle with a method move that prints "Vehicle is moving". 
# Then, create a subclass Car that overrides the move method to print "Car is driving". 
# Instantiate an object of the Vehicle class and call the move method. Also, instantiate an object of the Car class and call the move method. 

# Expected Output:
# The move method of Vehicle should print "Vehicle is moving".
# The move method of Car should print "Car is driving".

# Constraint
# The move method in both the base class and the subclass should not return any values, only print the output.
# Ensure that the subclass method properly overrides the base class method.

class Vehicle:
    def  move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

vehicle=Vehicle()
vehicle.move()

