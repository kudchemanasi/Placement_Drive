"""2. Demonstrate use of abstract class, multiple inheritance and decorator in
python using examples."""

# 1. abstract class

# abstract classes are blueprint for other classes.
# It is declared by using @abstractmethod decorater

from abc import ABC, abstractmethod
class Money(ABC):
    def print_slip(self , amount):
        print('Purchase amount:', amount)
    @abstractmethod
    def payment(self, amount):
        print("Your payment is:")

class CreditCardPayment(Money):
    def payment(self, amount):
        print('Credict card payment ',amount)

ob1 = CreditCardPayment()
ob1 = payment(100)




# 2. Multiple inheritance

# In this an object or class can inherit features from more than one parent
# or parent class

"""Syntax:

Class Base1:
    Body of the class
    
Class Base2:
    Body of the class
    
Class Derived(Base1, Base2):
    Body of the class

"""

class Employees():

    def name(self):
        name = input("Enter Name : ")
        print(name)

class salary():
    def Salary(self):
        salary = int(input('Enter Salary : '))
        print(salary)

class Designation(Employees,salary):
    def desig(self):
        desig = input('Enter Designation : ')
        print(desig)

obj = Designation()
obj.name()
obj.Salary()
obj.desig()



# 3. Decorator
# Decorater is used to change the behavior of a function without modifying
# the function itself.


def my_name():
    print("My name is Manasi")

new_name = my_name()
print(new_name())
