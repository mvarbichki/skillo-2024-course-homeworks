"""Problem 0: Create a class "Person" with a special method "__str__" to provide a string representation. Instantiate
an object of this class and print it."""


class Person:

    def __init__(self, name, gender, height, eyes_color):
        self.name = name
        self.gender = gender
        self.height = height
        self.eyes_color = eyes_color

    def __str__(self):
        return f"The person {self.name} is {self.gender} tall {self.height} and has {self.eyes_color} eyes."


person_one = Person("Sam", "male", 185, "brown")
person_two = Person("Ema", "female", 155, "blue")

# print(person_one)
# print(person_two)

"""Problem 1: Define a class "Email" with special methods "__eq__" and "__ne__" to compare two email addresses. Test 
the equality and inequality operators with different email instances."""


class Email:

    def __init__(self, email):
        self.email = email

    def __eq__(self, other):
        return self.email == other

    def __ne__(self, other):
        return self.email != other


email_one = Email("astefanov@somemail.com")
email_two = Email("mivanova@othermail.com")

# print(f"Is emails same? {email_one == email_two}")
# print(f"Is the email different? {email_one != email_two}")
# print(f"Is emails same? {email_two == email_two}")


"""Problem 2: Create a class "Student" with private attributes for name and age. Implement getter and setter methods 
for these attributes. Demonstrate their usage."""


class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getter_name(self):
        return self.__name

    def getter_age(self):
        return self.__age

    def setter_name(self, value_name):
        self.__name = value_name

    def setter_age(self, value_age):
        self.__age = value_age


student = Student("Stephan", 22)

# print(f"Before - {student.getter_name()}, {student.getter_age()} ")
student.setter_name("Simon")
student.setter_age(25)
# print(f"After - {student.getter_name()}, {student.getter_age()}")

"""Problem 3: Design a class "BankAccount" with methods for deposit, withdrawal, and balance inquiry. Use 
encapsulation to protect the account balance. Demonstrate proper usage of the class."""


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, deposit_sum):
        self.__balance += deposit_sum
        return f"Deposit succeed"

    def withdrawal(self, withdrawal_sum):
        # checks if withdrawal sum is bigger than the balance
        if withdrawal_sum > self.__balance:
            return f"Balance is exceed. Your balance: {self.__balance}"
        else:
            self.__balance -= withdrawal_sum
            return "Withdrawal succeed"

    def balance_inquiry(self):
        return self.__balance


# object with initiate balance
customer_acc = BankAccount(5000)

# print(f"Balance before transaction: {customer_acc.balance_inquiry()}")
# print(customer_acc.deposit(500))
# print(f"Balance after transaction: {customer_acc.balance_inquiry()}")
# print(customer_acc.withdrawal(5600))
# print(customer_acc.withdrawal(1500))
# print(f"Balance after transaction: {customer_acc.balance_inquiry()}")


"""Problem 4: Implement a class "Rectangle" with private attributes for length and width. Include special methods 
"__eq__" and "__lt__" to compare rectangles based on area and perimeter. Test the comparison operators with multiple 
instances."""


class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area_of_rectangle(self):
        return self.__length * self.__width

    def __eq__(self, other):
        return (self.__length == other.__length) and (self.__width == other.__width)

    def __lt__(self, other):
        return self.__length < other.__length and self.__width < other.__width


r1 = Rectangle(3, 5)
r2 = Rectangle(3, 5)
r3 = Rectangle(6, 10)

# print(f"Is r1 equal to r2?: {r1 == r2}")
# print(f"Is r1 smaller than r2?: {r1 < r2}")
# print(f"Is r2 smaller then r3?: {r2 < r3}")
# print(f"IS r1 area equal to r2 area?: {r1.area_of_rectangle() == r2.area_of_rectangle()}")
# print(f"Is r1 area smaller than r2 area?: {r1.area_of_rectangle() < r2.area_of_rectangle()}")
# print(f"Is r1 area smaller than r3 area?: {r1.area_of_rectangle() < r3.area_of_rectangle()}")


"""Problem 5: Design an abstract class "Vehicle" with a method "start_engine()". Create two subclasses, 
"Car" and "Bicycle," implementing the "start_engine()" method differently. Demonstrate polymorphism by calling the 
method on instances of both subclasses."""

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start_engin(self):
        pass


class Car(Vehicle):

    def start_engin(self):
        return "Makes a sound of working engine"


class Bicycle(Vehicle):

    def start_engin(self):
        return "Does not have engine"


car = Car()
bicycle = Bicycle()

# print(car.start_engin())
# print(bicycle.start_engin())


"""Problem 6: Implement a class "Book" with special methods "__str__" and "__len__" to provide a string 
representation and the number of pages. Create instances of "Book" and demonstrate the use of these methods."""


class Book:

    def __init__(self, book_name, pages):
        self.book_name = book_name
        self.pages = pages

    def __len__(self):
        return len(self.pages)

    def __str__(self):
        return f"The book name is {self.book_name} and has {self.__len__()} pages"


book_one = Book("WWII history", [i for i in range(1, 101)])

# print(book_one)

"""Problem 7: Create a class "Animal" with a special method "__init__" that sets a species attribute. Implement 
subclasses "Dog" and "Cat" with their own "__str__" methods. Use polymorphism to display species information."""


class Animal:

    def __init__(self, species):
        self.species = species


class Dog(Animal):
    def __repr__(self):
        return f"Dogs are {self.species} and can bark"


class Cat(Animal):

    def __repr__(self):
        return f"Cats are {self.species} and can meow"


dog = Dog("mammals")
cat = Cat("mammals")

# print(dog.__str__())
# print(cat.__str__())
