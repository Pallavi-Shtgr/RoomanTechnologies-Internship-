"""Day 07 OOP """

# Write a Python class called Laptop that has two attributes: brand (a string) and ram (an integer representing RAM in GB). 

# Implement a method upgrade_ram that takes an additional RAM value (integer) and adds it to the existing RAM.  After upgrading, the method prints the updated RAM.

# Expected Output:
# The upgrade_ram method should print the updated RAM value in the format: "RAM upgraded to <new_ram>GB".


class Laptop:
    def __init__(self,brand:str,ram:int):

        if not isinstance(brand,str):
            raise ValueError("Brand must be a string")

        if not isinstance(ram, int) or ram<=0:
            raise ValueError("RAM must be a positive integer")

        self.brand=brand
        self.ram=ram

    def upgrade_ram(self,additional_ram:int):
        if not isinstance(additional_ram,int) or additional_ram<=0:
            raise ValueError("Additional RAM must be a positive integer")

        self.ram+= additional_ram

        print(f"RAM upgraded to {self.ram}GB")

laptop=Laptop("Dell",8)
laptop.upgrade_ram(4)