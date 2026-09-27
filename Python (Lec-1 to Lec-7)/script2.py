'''
1. variable
2. Data Types
3. Type Casting
4. User Input
5. Type Conversion
6. Operators
7. strings
8. String Methods
9. f-strings
10. Doc strings
'''

# ============================================================================
# Variables in Python 
# ============================================================================
'''
# 1. variable

name="indra" 
height=5.6 
age=25 
does_smoke=False

print(name,type(name),sep=" <<-->> ") # name is nothing but a variable which is holding the value of -> string class object
print(height,type(height),sep=" <<-->> ") # height is holding the value of -> float class object
print(age,type(age),sep=" <<-->> ") # age is holding the value of -> int class object
print(does_smoke,type(does_smoke),sep=" <<-->> ") # does_smoke is holding the value of -> bool class object

Output:
indra <<-->> <class 'str'>
5.6 <<-->> <class 'float'>
25 <<-->> <class 'int'>
False <<-->> <class 'bool'>

print(age+10); # ✅ - 33
# print(age+"10"); #TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

# ============================================================================
# Data Types in Python 
# ============================================================================
'''
# Data Types:
a. numerical_data_types = [int,float,complex]
b. dictionary_data_types = [dict]
c. boolean_data_types = [bool]
d. set_data_types = [set]
e. sequence_data_types = [str,list,tuple]

# with examples:
i. int - 1
ii. float - 1.5
iii. bool - True/False
iv. str - "Hello"
v. list - [1,2,3]
vi. tuple - (1,2,3)
vii. set - {1,2,3}
viii. dict - {"name":"indra","age":25}
ix. complex - 1+2j
'''

# ============================================================================
# Type Casting in Python
# ============================================================================

'''
# 3. User Input
# 4. Type Conversion

# Type Casting --> Converting a value from one data type to another.

name=input("Enter your name: ") # input() function is used to take input from user as STRING datatype
city=input("Enter your city: ")
hobby=input("Enter your hobby: ")
print("Hello",name,"from",city,"who likes",hobby) 

# Input():
# It always takes input from user in the form of string. So, if you want to take input of any other data type, you need to convert it into that data type using type casting.

number_first=input("Enter first number: ") # input() function is used to take input from user
number_second=input("Enter second number: ")
print("Sum of two numbers is: ",int(number_first)+int(number_second)) # TYPE CASTING from string to int

user_input=input("Enter string number: ")
# print type of user_input
print(type(user_input)) # <class 'str'>
user_input_int=int(user_input) # type casting from string to int
print(type(user_input_int)) # <class 'int'>
user_input_float=float(user_input) # type casting from string to float
print(type(user_input_float)) # <class 'float'>

'''
# ============================================================================
# Operators in Python 
# ============================================================================
'''
# Operators:
# i. Arithmetic Operators
# ii. Assignment Operators
# iii. Comparison Operators
# iv. Logical Operators
# v. Bitwise Operators

# ============================================================================
# i. Arithmetic Operators
# ============================================================================
a=10
b=3
print("Addition: ",a+b) # 13
print("Subtraction: ",a-b) # 7
print("Multiplication: ",a*b) # 30
print("Division: ",a/b) # 3.333...
print("Modulus: ",a%b) # 1
print("Exponentiation: ",a**b) # 1000 --> 10^3
print("Floor Division: ",a//b) # 3

# ============================================================================
# ii. Assignment Operators
# ============================================================================
a=10
b=3
a+=b # a=a+b --> 10+3=13
print(a) # 13
a=10
a-=b # a=a-b --> 10-3=7
print(a) # 7
a=10
a/=b # a=a/b --> 10/3=3.333...
print(a) # 3.333...
a=10
a%=b # a=a%b --> 10%3=1
print(a) # 1
a**=b # a=a**b --> 1^3=1
print(a) # 1
a=10
a//=b # a=a//b --> 10//3=3
print(a) # 3

# ============================================================================
# iii. Comparison Operators
# ============================================================================
a=10
b=3
print("Equal: ",a==b) # False
print("Not Equal: ",a!=b) # True
print("Greater Than: ",a>b) # True
print("Less Than: ",a<b) # False
print("Greater Than or Equal: ",a>=b) # True
print("Less Than or Equal: ",a<=b) # False

# ============================================================================
# iv. Logical Operators
# ============================================================================
a=10
b=3
# and, or, not
# and : If both the conditions are True, then it will return True, otherwise False
# or : If any one of the condition is True, then it will return True, otherwise False
# not : It will return the opposite of the condition

print("Logical AND: ",a>5 and b<5) # True 
print("Logical OR: ",a>5 or b>5) # True
print("Logical NOT: ",not(a>5)) # False
'''
# ============================================================================
# Strings in Python 
# ============================================================================
'''
# Strings are a sequence of characters enclosed in single quotes, double quotes or triple quotes.
# Strings are immutable, which means once a string is created, it cannot be changed.
# Strings can be indexed and sliced.
'''
# ============================================================================
# String Methods in Python
# ============================================================================
'''
# String Methods (Important ones):
# 1. len() - returns the length of the string
# 2. upper() - converts the string to uppercase
# 3. lower() - converts the string to lowercase
# 4. strip() - removes the leading and trailing whitespaces
# 5. replace() - replaces a substring with another substring
# 6. split() - splits the string into a list of substrings
# 7. join() - joins a list of strings into a single string
# 8. find() - returns the index of the first occurrence of a substring
# 9. count() - returns the number of occurrences of a substring
# 10. isalpha() - returns True if all characters in the string are alphabetic
# 11. isdigit() - returns True if all characters in the string are digits
# 12. isspace() - returns True if all characters in the string are whitespace
# 13. startswith() - returns True if the string starts with a specified substring
# 14. endswith() - returns True if the string ends with a specified substring
# 15. capitalize() - capitalizes the first character of the string
# 16. title() - converts the string to title case

word = "hello world Python"
print("Length of the string: ",len(word)) # 18 --> it will return the length of the string
print("Uppercase: ",word.upper()) # HELLO WORLD PYTHON --> it will convert the string to uppercase
print("Lowercase: ",word.lower()) # hello world python --> it will convert the string to lowercase
print("Strip: ",word.strip()) # hello world Python --> it will remove leading and trailing whitespaces if any
print("Replace: ",word.replace("world","Python1")) # hello Python1 Python --> it will replace the substring "world" with "Python1"
print("Split: ",word.split(" ")) # ['hello', 'world', 'Python'] --> it will split the string into a list of substrings
print("Join: ",(" ".join(["hello", "Python Lang"]))) # hello Python Lang Python ❌ hello Python Lang✅ --> it will join a list of strings into a single string
print("Find: ",word.find("world")) # 6 --> it will return the index of the first occurrence of the substring "world"
print("Count: ",word.count("o")) # 3 --> it will return the number of occurrences of the substring "o"
print("Startswith: ",word.startswith("hello")) # True --> it will return True if the string starts with the substring "hello"
print("Endswith: ",word.endswith("Python")) # True --> it will return True if the string ends with the substring "Python"

#indexing and slicing in detail
print("Character at index 0: ",word[0]) # h
# print("Character at index 18: ",word[18]) # string index out of range
# print("Character at index 20: ",word[20]) # string index out of range
print("Character at index 6: ",word[17]) # n
print("Character at index -1: ",word[-1]) # n
print("Characters from index 6 to 11: ",word[6:11]) # world
print("Characters from index 0 to 5: ",word[0:5]) # hello
print("Every second character: ",word[::2]) # hlo ol
print("Characters from index 5 to 10 with step 2: ",word[5:10:2]) #  ol
print("Reverse the string: ",word[::-1]) # dlrow olleh

'''
# ============================================================================
# f-strings in Python 
# ============================================================================
'''
# f-strings (formatted string literals) are a way to embed expressions inside string literals, using curly braces {}. They were introduced in Python 3.6 and provide a more readable and concise way to format strings.

name = "Alice"
age = 30
# at the beginining we didn't use f-string: we didn't use f-string, we used concatenation and type casting to format the string. But with f-string, we can directly embed the variables inside the string using curly braces {}.
print("Hello, " + name + "! You are " + str(age) + " years old.") # Hello, Alice! You are 30 years old.
print(f"Hello, {name}! You are {age} years old.")
print("without f-string: Hello, {}! You are {} years old.".format(name, age))

total_marks = 10
marks_obtained = 3

ans = total_marks / marks_obtained

print(f"{ans:.4f}")  # 3.3333
print(f"{ans:.2f}")  # 3.33
print(f"{ans:.1f}")  # 3.3
print("{:.2f}".format(ans)) # 3.33

'''

# ============================================================================
# Doc strings in Python
# ============================================================================
'''
# Docstrings (documentation strings) are a way to document your code in Python. They are written using triple quotes (""" or [['''''']) and are placed at the beginning of a module, class, or function. Docstrings provide a convenient way to associate #documentation with Python code.

#Example of docstring in a function:
def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b

print(add_numbers.__doc__)  # Print the docstring of the function
print(add_numbers(5, 10))  # Output: 15

'''
