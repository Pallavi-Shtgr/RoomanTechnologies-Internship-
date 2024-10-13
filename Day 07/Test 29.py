"""Day 07 OOP """

# Create two classes, Dog and Cat, each having a method named sound.
#  In the Dog class, sound should print "Bark", and in the Cat class, sound should print "Meow". 

# Write a function make_sound that takes an animal object (either a Dog or Cat) and calls its sound method. 
# Test your function with both a Dog and a Cat object.

# Expected Output:
# The sound method of the Dog class should print "Bark".
# The sound method of the Cat class should print "Meow".
# The make_sound function should correctly call the sound method of either class.


class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

dog=Dog()
cat=Cat()

make_sound(dog)
make_sound(cat)