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


#print(f"Before - {student.getter_name()}, {student.getter_age()} ")
student.setter_name("Simon")
student.setter_age(25)
#print(f"After - {student.getter_name()}, {student.getter_age()}")

