"""
1. Exception Handling
2. Raising Custom Exception
3. Local vs Global Variable
4. File Handling - reading file
5. File Handling - writing file
6. File Handling - appending file
7. Built in Python Library
8. if __name__ = "__main__"
"""

# ============================================================================
# 1. Exception Handling
# 2. Raising Custom Exception
# ============================================================================

# class NegativeNumberError(Exception):
#     pass

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     if(num1<0):
#         raise NegativeNumberError("num1 is negative");
#     if(num2<0):
#         raise NegativeNumberError("num2 is negative")
#     else:
#      ans = num1 / num2

# except ValueError:
#     print("❌ Please enter numbers only!")

# except ZeroDivisionError:
#     print("❌ You cannot divide by zero!")

# except TypeError:
#     print("❌ Both values must be numbers!")

# except NegativeNumberError as error:
#     print("❌ custom error");
#     print(f"Here is the error {error}")

# else:
#     print("✅ Division successful!")
#     print("Answer =", ans)

# finally:
#     print("🔚 Program execution finished."); # This block always runs, no matter what

"""
----------------------------------------------------
Normal Case
---------------------------------------------------- 
Enter first number: 10
Enter second number: 5

✅ Division successful!
Answer = 2.0
🔚 Program execution finished.

try ✅
except ❌ (none)
else ✅
finally ✅
-------------------------------------------------------
ZeroDivisionError:
-------------------------------------------------------
10
0

❌ You cannot divide by zero!
🔚 Program execution finished.

try → ERROR → except ZeroDivisionError → finally

---------------------------------------------------------
ValueError
---------------------------------------------------------
10
abc

❌ Please enter numbers only!
🔚 Program execution finished.

why?
int("abc")
"""

# ============================================================================
# 3. Local vs Global Variable
# ============================================================================

# name = "Indranil"   # Global variable

# def greet():
#     print(name)

# greet() # Indranil
# print(name) # Indranil

"""
name = "Indranil"    ← GLOBAL
       ↓
   ┌─────────┐
   │ function│ ← can access it
   └─────────┘
       ↓
outside       ← can access it
"""
# def greet():
#     name = "Indranil"   # Local variable
#     print(name)

# greet()

# print(name)   # ❌ Error --> NameError: name 'name' is not defined

"""
GLOBAL
────────────────────

def greet():
    │
    │ name = "Indranil"  ← LOCAL
    │
    └────────────────────

name outside ❌
"""

# name = "Indranil"       # Global

# def greet():
#     name = "Rahul"      # Local
#     print(name)

# greet(); # Rahul

# print(name); # Indranil

"""
The two name variables are different variables.
Inside the function:
name = "Rahul"

Python creates a local name.
Outside:
name = "Indranil"

is the global name.
"""
# count = 10

# def increase():
#     count = count + 1
#     print(count)

# increase();

"""
You might expect:
11
But ❌ this gives an error.
Python sees:
count = count + 1

and assumes count is a local variable because you're assigning to it.
But you're also trying to read that local variable before it has a value.
"""
# count = 10

# def increase():
#     global count
#     count = count + 1

# increase()

# print(count); # 11

"""
Here:
global count

means:
"Don't create a local count. I want to use the global one."
"""

# company = "BudhanaTech"       # GLOBAL
# salary = 40000                # GLOBAL


# def employee_details():

#     name = "Indranil"         # LOCAL
#     salary = 50000            # LOCAL

#     print("Name:", name)
#     print("Salary:", salary)
#     print("Company:", company)


# employee_details()

# print("Global salary:", salary)

"""
🧠 The easiest rule to remember
Created outside function → Global
Created inside function → Local

And:
Local variable cannot normally be accessed from outside its function.

One more important point: global variables can be read inside a function without global; you need the global keyword when you want to assign/change that global variable from inside the function.
"""

# ============================================================================
# 4. File Handling - reading file
# 5. File Handling - writing file
# 6. File Handling - appending file
# ============================================================================

# -------------------------------------------
# write
# -------------------------------------------
with open("students.txt", "w") as file:
    file.write("First Line\n")
    file.write("First Line\n")

# this will overrite old text
# students = ["Rahul", "Priya", "Amit"]
# with open("students.txt", "w") as file:

#     for student in students:
#         file.write(student + "\n")

# -------------------------------------------
# read
# -------------------------------------------

# with open("students.txt", "r") as file:

#     content = file.read()

# print(content)

"""
Rahul
Priya
Amit
"""

# with open("students.txt", "r") as file:

#     line1 = file.readline()
#     line2 = file.readline()
#     line3 = file.readline()

# print(line1)
# print(line2)
# print(line3)
"""
Rahul

Priya

Amit
"""

# with open("students.txt", "r") as file:

#     students = file.readlines()

# print(students)
# ['Rahul\n', 'Priya\n', 'Amit\n']

# with open("students.txt", "r") as file:

#     for line in file:
#         print(line.strip())

# -------------------------------------------
# append
# -------------------------------------------
# with open("students.txt", "a") as file:

#     file.write("Sachin\n");
#     file.write("Prateek\n");


# ============================================================================
# Inbuilt Func
# ============================================================================
# import math

# print(math.sqrt(9))
# print(math.ceil(4.2))
# print(math.floor(4.2))

# import random

# print(random.randint(11, 30))

# from datetime import datetime

# current_time = datetime.now()
# print("Current date and time: ", current_time)

# ============================================================================
#  if __name__ == "__main__
# ============================================================================


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


print("Calculator loaded")
print(__name__)
# if you run this script5.py file it will show "__main__" but if you try to access it from other file it will show "script5.py"

if __name__ == "__main__":
    print(add(10, 5))
    print(subtract(10, 5))


# -----------------------------------------------------------------
# math_utils.py
def square(number):
    return number * number


def cube(number):
    return number * number * number


if __name__ == "__main__":

    print("Testing square:")
    print(square(5))

    print("Testing cube:")
    print(cube(5))

'''
# app.py
from math_utils import square

result = square(10)

print(result)

Output:
100
The testing code inside:
if __name__ == "__main__":

doesn't run.
'''