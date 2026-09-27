"""
===============================================================================
                         PYTHON OOP (OBJECT-ORIENTED PROGRAMMING)
===============================================================================

TOPICS:

1. Introduction to OOP
2. Classes and Objects
3. Attributes and Methods
4. Constructor / __init__()
5. Magic / Dunder Methods
6. Encapsulation
7. Static Method
8. Inheritance
9. Types of Inheritance


===============================================================================
1. INTRODUCTION TO OOP
===============================================================================

OOP stands for:

    Object-Oriented Programming

OOP is a programming approach where we organize our program around:

    -> Classes
    -> Objects
    -> Attributes (Data)
    -> Methods (Behavior)

Real-world example:

    A STUDENT has:

        Data:
            name
            age
            course

        Behavior:
            introduce()
            study()
            attend_class()

In OOP, we can represent this real-world entity using a CLASS.


-------------------------------------------------------------------------------
IMPORTANT OOP IDEA
-------------------------------------------------------------------------------

Think:

    CLASS  = Blueprint / Template
    OBJECT = Real instance created from that blueprint


Example:

    Class:
        Student

    Objects:
        student1
        student2
        student3

Each object can have different data, even though they are created from
the same class.


===============================================================================
2. CLASS
===============================================================================

Definition:

A class is a blueprint or template used to create objects.

Syntax:

    class ClassName:
        # attributes
        # methods

Example:

    class Student:
        pass


-------------------------------------------------------------------------------
CLASS NAMING CONVENTION
-------------------------------------------------------------------------------

By convention, Python class names use PascalCase:

    Student
    Employee
    BankAccount
    Car

Instead of:

    student
    employee
    bankaccount

So we will use:

    class Student:

rather than:

    class student:


===============================================================================
3. OBJECT
===============================================================================

Definition:

An object is an instance of a class.

Example:

    student1 = Student()

Here:

    Student  -> Class
    student1 -> Object / Instance


Mind Map:

                    CLASS
                      |
                Blueprint
                      |
          -------------------------
          |           |           |
       Object 1    Object 2    Object 3
       student1    student2    student3


===============================================================================
4. ATTRIBUTES
===============================================================================

Definition:

Attributes are variables that belong to an object or class.

In our Student example:

    name
    age
    course

are attributes of the Student object.

Example:

    student1.name
    student1.age
    student1.course


===============================================================================
5. METHODS
===============================================================================

Definition:

A method is a function defined inside a class.

Methods usually represent the behavior/action of an object.

Example:

    introduce()

is a method of the Student class.

Important:

    Function outside a class  -> Function
    Function inside a class   -> Method


===============================================================================
6. CONSTRUCTOR / __init__()
===============================================================================

Python commonly uses __init__() to initialize an object.

Example:

    def __init__(self, name, age, course):

When we create:

    student1 = Student("Harsh", 25, "GenAI")

Python automatically calls:

    __init__()

and passes the supplied values to it.

-------------------------------------------------------------------------------
IMPORTANT TERMINOLOGY
-------------------------------------------------------------------------------

__init__() is technically an INITIALIZER in Python.

It is commonly called the "constructor" in beginner-level Python teaching,
because it is automatically executed when an object is initialized.

For learning purposes, you will often see:

    __init__() -> Constructor

This terminology is common, but technically Python's object creation process
uses __new__() first, followed by __init__() for initialization.


===============================================================================
7. self
===============================================================================

self represents the CURRENT OBJECT / INSTANCE.

Example:

    student1 = Student("Harsh", 25, "GenAI")

Inside __init__():

    self.name
    self.age
    self.course

refer to the attributes belonging to student1.

If we create another object:

    student2 = Student("Rahul", 22, "Python")

then inside that call:

    self

refers to student2.

-------------------------------------------------------------------------------
Think:

    self = "this current object"

Python requires us to explicitly write self as the first parameter of
normal instance methods.

"""


# ============================================================================
# 8. CREATING OUR STUDENT CLASS
# ============================================================================

class Student:

    # ------------------------------------------------------------------------
    # __init__() -> Initializer / commonly called constructor
    # ------------------------------------------------------------------------

    def __init__(self, arg_name, arg_age, arg_course):

        # Instance attributes
        self.name = arg_name
        self.age = arg_age
        self.course = arg_course

    # ------------------------------------------------------------------------
    # Instance Method
    # ------------------------------------------------------------------------

    def introduce(self):

        print(f"Hello, my name is {self.name}. I am a student.")


"""
At this point:

    Student
       |
       |---- name
       |---- age
       |---- course
       |
       |---- introduce()


name, age, course
    -> Attributes / Data

introduce()
    -> Method / Behavior
"""


# ============================================================================
# 9. CREATING OBJECTS
# ============================================================================

student1 = Student("Harsh", 25, "GenAI")

student2 = Student("Rahul", 22, "Python")


"""
Here:

    Student(...)
        -> Calling the class to create an object

    student1
        -> Object / Instance

    student2
        -> Another Object / Instance

Both objects come from the same class but contain different data.
"""


# ============================================================================
# 10. ACCESSING ATTRIBUTES
# ============================================================================

print(student1.name)
# Harsh

print(student1.age)
# 25

print(student1.course)
# GenAI

print(student2.name)
# Rahul


# ============================================================================
# 11. CALLING METHODS
# ============================================================================

student1.introduce()
# Hello, my name is Harsh. I am a student.

student2.introduce()
# Hello, my name is Rahul. I am a student.


"""
Notice:

    student1.introduce()

and

    student2.introduce()

call the SAME method, but the result is different because self refers to
different objects.


student1.introduce()
        |
        -> self = student1


student2.introduce()
        |
        -> self = student2
"""


# ============================================================================
# 12. MAGIC / DUNDER METHODS
# ============================================================================

"""
Dunder means:

    Double UNDerscore

Dunder methods have double underscores before and after their names.

Example:

    __init__()
    __str__()
    __len__()
    __new__()
    __add__()

These methods are special methods recognized by Python.

They allow objects to interact with Python's built-in operations.

Examples:

    print(object)
        -> Python looks for __str__()

    len(object)
        -> Python looks for __len__()

    object + object
        -> Python can use __add__()


IMPORTANT:

    __init__() is a dunder method.
    __str__() is a dunder method.
    __len__() is a dunder method.

So:

    "Magic Method" / "Dunder Method"

are commonly used terms for these special methods.


===============================================================================
13. __str__()
===============================================================================

__str__() defines the user-friendly string representation of an object.

When we write:

    print(student1)

Python internally looks for:

    student1.__str__()


Without __str__(), printing a custom object usually produces a default
representation containing the class name and object information.

With __str__(), we can control what is displayed.
"""


class Student:

    def __init__(self, arg_name, arg_age, arg_course):

        self.name = arg_name
        self.age = arg_age
        self.course = arg_course

    def introduce(self):

        print(f"Hello, my name is {self.name}. I am a student.")

    # ------------------------------------------------------------------------
    # __str__() -> controls the string representation of the object
    # ------------------------------------------------------------------------

    def __str__(self):

        return f"Student: {self.name} | Age: {self.age} | Course: {self.course}"


student1 = Student("Harsh", 25, "GenAI")

print(student1)

# Student: Harsh | Age: 25 | Course: GenAI


"""
Important:

__str__() MUST return a STRING.

Correct:

    return "Hello"

Incorrect:

    return 100

because print(object) expects __str__() to return a string.
"""


# ============================================================================
# 14. __len__()
# ============================================================================

"""
__len__() defines what should happen when len() is used on our object.

Example:

    len(student1)

Python internally looks for:

    student1.__len__()


Here we decide that the "length" of a Student object will be the number
of characters in the student's name.
"""


class Student:

    def __init__(self, arg_name, arg_age, arg_course):

        self.name = arg_name
        self.age = arg_age
        self.course = arg_course

    def introduce(self):

        print(f"Hello, my name is {self.name}. I am a student.")

    def __str__(self):

        return f"Student: {self.name} | Age: {self.age} | Course: {self.course}"

    # ------------------------------------------------------------------------
    # __len__() -> defines the behavior of len(object)
    # ------------------------------------------------------------------------

    def __len__(self):

        return len(self.name)


student1 = Student("Harsh", 25, "GenAI")

print(student1)
# Student: Harsh | Age: 25 | Course: GenAI

print(len(student1))
# 5


"""
Why 5?

    "Harsh"

    H -> 1
    a -> 2
    r -> 3
    s -> 4
    h -> 5


Therefore:

    len(student1)
        |
        -> student1.__len__()
        |
        -> len(student1.name)
        |
        -> 5
"""


# ============================================================================
# 15. NORMAL OBJECT vs BUILT-IN DATA TYPE
# ============================================================================

"""
Python's built-in objects already know how to respond to operations.

For example:

    str_value = "GenAI"
    num1 = 100
    bool1 = True

"""

str_value = "GenAI"
num1 = 100
bool1 = True

print(bool1)
# True

print(num1)
# 100

print(str_value)
# GenAI

print(len(str_value))
# 5


"""
Why does len(str_value) work?

Because Python's string object provides the required behavior for len().

Similarly, when we define __len__() in our Student class, our custom object
can also work with len().

This is one of the important powers of DUNDER METHODS.


===============================================================================
16. COMPLETE EXAMPLE
===============================================================================
"""


class Student:

    # Constructor / Initializer
    def __init__(self, arg_name, arg_age, arg_course):

        self.name = arg_name
        self.age = arg_age
        self.course = arg_course

    # Instance Method
    def introduce(self):

        print(f"Hello, my name is {self.name}. I am a student.")

    # Dunder Method
    def __str__(self):

        return f"Student: {self.name} | Age: {self.age} | Course: {self.course}"

    # Dunder Method
    def __len__(self):

        return len(self.name)


student1 = Student("Harsh", 25, "GenAI")

print(student1)

student1.introduce()

print(f"Number of characters in student object name: {len(student1)}")


# ============================================================================
# 17. ENCAPSULATION
# ============================================================================

"""
Definition:

Encapsulation means bundling data and the methods that operate on that data
inside a class, while controlling how that data is accessed or modified.

Example:

    Student
       |
       |---- name
       |---- age
       |---- course
       |
       |---- introduce()


Python does not have strict private variables in the same way as some
languages.

Python commonly uses:

    _variable
        -> Convention: intended for internal use.

    __variable
        -> Name mangling is applied; used to discourage direct access.

Example:

    class Student:

        def __init__(self):
            self.__age = 25


The double underscore does NOT make the variable absolutely private.

It triggers name mangling.


===============================================================================
18. STATIC METHOD
===============================================================================

A static method is a method that does not depend on a particular object's
instance data.

It is created using:

    @staticmethod

Example:

    class Student:

        @staticmethod
        def college_info():
            print("This is a college information method.")


We can call it using:

    Student.college_info()

No self is required.

Compare:

    Instance Method
        -> uses self
        -> works with object-specific data

    Static Method
        -> does not require self
        -> generally performs a utility-related operation


===============================================================================
19. INHERITANCE
===============================================================================

Definition:

Inheritance allows one class to acquire/reuse attributes and methods from
another class.

The existing class is called:

    Parent / Base / Superclass

The new class is called:

    Child / Derived / Subclass


Example:

    class Animal:
        def eat(self):
            print("Eating")


    class Dog(Animal):
        pass


Dog inherits from Animal.

Therefore:

    dog = Dog()
    dog.eat()

works because Dog inherited eat() from Animal.


Mind Map:

                  Animal
                  Parent
                     |
                 Inheritance
                     |
                    Dog
                  Child


===============================================================================
20. TYPES OF INHERITANCE
===============================================================================

Python supports different inheritance structures.

1. Single Inheritance

        A
        |
        B


2. Multilevel Inheritance

        A
        |
        B
        |
        C


3. Multiple Inheritance

        A       B
         \     /
           C


4. Hierarchical Inheritance

             A
           /   \
          B     C


5. Hybrid Inheritance

A combination of multiple inheritance patterns.


===============================================================================
21. COMPLETE OOP MIND MAP
===============================================================================

                         OOP
                          |
        -----------------------------------------
        |           |           |               |
      Class       Object    Attributes        Methods
        |           |           |               |
    Blueprint    Instance      Data          Behavior
        |
        |
   __init__()
        |
   Initialization
        |
   Dunder Methods
        |
   ------------------------------
   |            |              |
 __str__()    __len__()    __init__()
   |            |              |
 print()      len()        initialization


                     OOP
                      |
        --------------------------------
        |              |               |
   Encapsulation   Inheritance    Polymorphism
        |              |
    Data +         Parent ->
    Methods        Child


Inheritance
    |
    -----------------------------------------
    |          |          |        |        |
  Single    Multilevel  Multiple  Hierarchical  Hybrid


===============================================================================
22. MOST IMPORTANT THINGS TO REMEMBER
===============================================================================

1. CLASS
   -> Blueprint / template.

2. OBJECT
   -> Instance of a class.

3. ATTRIBUTE
   -> Data/variable belonging to an object or class.

4. METHOD
   -> Function defined inside a class.

5. self
   -> Refers to the current object/instance.

6. __init__()
   -> Initializes the object.
   -> Commonly called the constructor.

7. DUNDER METHODS
   -> Special methods with double underscores.

8. __str__()
   -> Controls the user-friendly string representation of an object.

9. __len__()
   -> Defines what len(object) should return.

10. ENCAPSULATION
    -> Bundling data and methods together and controlling access.

11. STATIC METHOD
    -> Method that does not require object-specific self data.

12. INHERITANCE
    -> Allows a child class to reuse/extend a parent class.

13. CLASS vs OBJECT

        Class  -> Blueprint
        Object -> Actual instance


===============================================================================
END OF OOP INTRODUCTION NOTES
===============================================================================
"""

'''
class BankAccount:

    # Class Attribute
    bank_name = "OpenAI Bank"

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        
        self.__balance = balance

    def deposit(self, amount):
        if amount>0:
            self.__balance += amount
            print(f"Rs.{amount}/- deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Rs.{amount}/- withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance
    
    @staticmethod
    def calculate_interest(balance):
        return balance * 0.05
    
    def __str__(self):
        return f"{self.holder_name} <<->> {self.account_number}"
    
    def __len__(self):
        return len(str(self.account_number))



acc1 = BankAccount(1001, "Rahul", 5000)
acc2 = BankAccount(1002, "Omkar", 50000)

print(acc1)
print(acc2)

acc1.deposit(10000)
acc1.withdraw(8000)

print(f"Current balance: {acc1.get_balance()}")
print(f"Current balance: {acc2.get_balance()}")

interest = BankAccount.calculate_interest(acc2.get_balance())
print(f"Estimated interest: {interest}")

'''