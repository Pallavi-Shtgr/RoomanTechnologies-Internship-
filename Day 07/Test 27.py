"""Day 07 OOP """

# Create a class named Employee that contains a private attribute called __salary (a float). 
# Implement a method get_salary that prints and returns the current salary, and a method set_salary that updates the salary, but prints the updated salary.
# You should create an object of the Employee class and first call the get method, and then the set method.

# Expected Output:
# get_salary should print the current salary.
# set_salary should only update and print the new salary if it's greater than 0.


class Employee:
    def __init__(self,salary:float):
        if salary>0:
            self.__salary=salary
        else:
            raise ValueError("Salary must be positive")
        
    def get_salary(self)-> float:
        print(f"Current salary:{self.__salary}")
        return self.__salary
        
    def set_salary(self, new_salary: float):
            
        if new_salary > 0:
            self.__salary = new_salary
            print(f"Updated salary: {self.__salary}")
        else:
            print("Error: Salary must be greater than 0. Salary not updated.")