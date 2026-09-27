# Python Fundamentals — Detailed Notes

## Topics Covered

1. Variables
2. Data Types
3. Type Casting
4. User Input
5. Type Conversion
6. Operators
7. Strings
8. String Methods
9. f-Strings
10. Docstrings

---

# 1. Variables in Python

## What is a Variable?

A **variable** is a name that refers to an object/value stored in memory.

Example:

```python
name = "indra"
age = 25
height = 5.6
does_smoke = False
```

Here:

* `name` refers to a string object
* `age` refers to an integer object
* `height` refers to a float object
* `does_smoke` refers to a Boolean object

We can check the type of a value using the `type()` function.

```python
name = "indra"
height = 5.6
age = 25
does_smoke = False

print(name, type(name), sep=" <<-->> ")
print(height, type(height), sep=" <<-->> ")
print(age, type(age), sep=" <<-->> ")
print(does_smoke, type(does_smoke), sep=" <<-->> ")
```

### Output

```text
indra <<-->> <class 'str'>
5.6 <<-->> <class 'float'>
25 <<-->> <class 'int'>
False <<-->> <class 'bool'>
```

### Important

Python is **dynamically typed**.

This means you don't have to explicitly declare the data type of a variable.

```python
x = 10
```

Python automatically understands that `x` contains an `int`.

Later, the same variable can refer to another type:

```python
x = 10
print(type(x))

x = "Hello"
print(type(x))
```

Output:

```text
<class 'int'>
<class 'str'>
```

---

## Variable Naming Rules

A variable name:

### Can contain

* Letters: `a-z`, `A-Z`
* Numbers: `0-9`
* Underscore: `_`

### Cannot

* Start with a number
* Contain spaces
* Use Python keywords

Valid:

```python
name = "Indra"
age1 = 25
user_name = "Indra"
_total = 100
```

Invalid:

```python
1name = "Indra"       # Invalid
user name = "Indra"   # Invalid
class = "Python"      # Invalid
```

### Convention

Python commonly uses **snake_case**:

```python
first_name = "Indra"
total_marks = 100
student_age = 25
```

---

# 2. Data Types

A **data type** determines what kind of value an object contains and what operations can be performed on it.

Python has several built-in data types.

## Major Python Data Types

| Category | Data Types                         | Example             |
| -------- | ---------------------------------- | ------------------- |
| Numeric  | `int`, `float`, `complex`          | `10`, `5.5`, `2+3j` |
| Boolean  | `bool`                             | `True`, `False`     |
| Text     | `str`                              | `"Hello"`           |
| Sequence | `list`, `tuple`, `range`           | `[1,2,3]`           |
| Set      | `set`, `frozenset`                 | `{1,2,3}`           |
| Mapping  | `dict`                             | `{"name":"Indra"}`  |
| Binary   | `bytes`, `bytearray`, `memoryview` | `b"Hello"`          |
| None     | `NoneType`                         | `None`              |

For beginners, the most important ones are:

```text
int
float
bool
str
list
tuple
set
dict
complex
```

---

## 2.1 int

`int` represents whole numbers.

```python
age = 25
marks = 100
temperature = -5
```

```python
print(type(age))
```

Output:

```text
<class 'int'>
```

Examples:

```python
10
0
-25
1000
```

---

## 2.2 float

`float` represents decimal numbers.

```python
height = 5.6
price = 99.99
percentage = 85.5
```

```python
print(type(height))
```

Output:

```text
<class 'float'>
```

---

## 2.3 bool

Boolean represents logical values.

There are only two Boolean values:

```python
True
False
```

Example:

```python
is_student = True
does_smoke = False
```

```python
print(type(is_student))
```

Output:

```text
<class 'bool'>
```

Boolean values are commonly used in conditions.

```python
age = 25

print(age > 18)
```

Output:

```text
True
```

---

## 2.4 str

`str` represents text.

Strings can be created using:

* Single quotes
* Double quotes
* Triple quotes

```python
name = 'Indra'
city = "Katwa"
message = """Hello Python"""
```

```python
print(type(name))
```

Output:

```text
<class 'str'>
```

---

## 2.5 list

A list stores multiple values.

```python
numbers = [1, 2, 3]
names = ["Indra", "Rahul", "Amit"]
```

Lists are:

* Ordered
* Mutable
* Allow duplicate values
* Can contain different data types

Example:

```python
data = [10, "Hello", 5.5, True]
```

---

## 2.6 tuple

A tuple is similar to a list but is **immutable**.

```python
numbers = (1, 2, 3)
```

Tuple:

* Ordered
* Immutable
* Allows duplicates

Example:

```python
student = ("Indra", 25, 85.5)
```

---

## 2.7 set

A set stores unique values.

```python
numbers = {1, 2, 3}
```

Duplicate values are automatically removed.

```python
numbers = {1, 2, 2, 3, 3}

print(numbers)
```

Output:

```text
{1, 2, 3}
```

Sets are useful when you want to store **unique values**.

---

## 2.8 dict

A dictionary stores data in **key-value pairs**.

```python
student = {
    "name": "Indra",
    "age": 25,
    "marks": 85
}
```

Here:

```text
"name"  → key
"Indra" → value
```

Accessing a value:

```python
print(student["name"])
```

Output:

```text
Indra
```

---

## 2.9 complex

Complex numbers contain a real and imaginary part.

```python
number = 1 + 2j
```

```python
print(type(number))
```

Output:

```text
<class 'complex'>
```

In Python, `j` represents the imaginary part.

---

# 3. Type Casting

## What is Type Casting?

**Type casting** means converting a value from one data type to another data type.

Common functions:

```python
int()
float()
str()
bool()
list()
tuple()
set()
```

Example:

```python
x = "10"

y = int(x)

print(y)
print(type(y))
```

Output:

```text
10
<class 'int'>
```

---

## String → Integer

```python
number = "100"

number = int(number)

print(number)
print(type(number))
```

Output:

```text
100
<class 'int'>
```

---

## String → Float

```python
number = "10.5"

number = float(number)

print(number)
print(type(number))
```

Output:

```text
10.5
<class 'float'>
```

---

## Integer → Float

```python
x = 10

y = float(x)

print(y)
```

Output:

```text
10.0
```

---

## Integer → String

```python
age = 25

age_string = str(age)

print(age_string)
print(type(age_string))
```

Output:

```text
25
<class 'str'>
```

---

## Float → Integer

```python
price = 99.99

price = int(price)

print(price)
```

Output:

```text
99
```

### Important

`int()` does **not round** the decimal.

It removes the fractional part.

```python
int(5.9)   # 5
int(5.1)   # 5
```

---

# 4. User Input

Python uses the `input()` function to take input from the user.

Syntax:

```python
input("message")
```

Example:

```python
name = input("Enter your name: ")

print(name)
```

If the user enters:

```text
Indra
```

Output:

```text
Indra
```

---

# Important: input() Always Returns str

This is extremely important.

```python
age = input("Enter your age: ")

print(type(age))
```

If the user enters:

```text
25
```

Output:

```text
<class 'str'>
```

Even though the user entered `25`, Python receives it as:

```python
"25"
```

---

## Problem with Numbers

Consider:

```python
a = input("Enter first number: ")
b = input("Enter second number: ")

print(a + b)
```

Suppose:

```text
Enter first number: 10
Enter second number: 20
```

Output:

```text
1020
```

Why?

Because:

```python
"10" + "20"
```

means string concatenation.

---

## Solution

Convert the input into `int`.

```python
a = input("Enter first number: ")
b = input("Enter second number: ")

print(int(a) + int(b))
```

Output:

```text
30
```

---

# 5. Type Conversion

The terms **type casting** and **type conversion** are often used interchangeably in beginner Python.

A useful distinction is:

### Type conversion

Changing a value from one type to another.

```python
x = "10"
y = int(x)
```

### Type casting

Explicitly forcing/converting a value into a particular type.

```python
int("10")
float("10")
str(10)
```

In Python tutorials, you will frequently see both terms used for the same thing.

---

## Taking Integer Input Directly

Instead of:

```python
age = input("Enter age: ")
age = int(age)
```

you can write:

```python
age = int(input("Enter age: "))
```

Example:

```python
age = int(input("Enter your age: "))

print(age)
print(type(age))
```

---

## Taking Float Input

```python
price = float(input("Enter price: "))

print(price)
print(type(price))
```

---

## Example

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print(name)
print(age)
print(height)
```

---

# 6. Operators in Python

Operators are symbols/keywords used to perform operations on values.

Major categories:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators

---

# 6.1 Arithmetic Operators

Arithmetic operators are used for mathematical calculations.

| Operator | Meaning        |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `%`      | Modulus        |
| `**`     | Exponentiation |
| `//`     | Floor Division |

Example:

```python
a = 10
b = 3
```

### Addition

```python
print(a + b)
```

Output:

```text
13
```

### Subtraction

```python
print(a - b)
```

Output:

```text
7
```

### Multiplication

```python
print(a * b)
```

Output:

```text
30
```

### Division

```python
print(a / b)
```

Output:

```text
3.3333333333333335
```

Python `/` produces a float.

---

### Modulus `%`

Returns the remainder.

```python
print(10 % 3)
```

Output:

```text
1
```

Because:

```text
10 ÷ 3

Quotient = 3
Remainder = 1
```

Very useful for checking even/odd:

```python
number = 10

print(number % 2 == 0)
```

Output:

```text
True
```

---

### Exponentiation `**`

Used for powers.

```python
print(10 ** 3)
```

Output:

```text
1000
```

Meaning:

```text
10 × 10 × 10 = 1000
```

---

### Floor Division `//`

Returns the floor of the division result.

```python
print(10 // 3)
```

Output:

```text
3
```

Compare:

```python
10 / 3
```

gives approximately:

```text
3.3333333333333335
```

while:

```python
10 // 3
```

gives:

```text
3
```

---

# 6.2 Assignment Operators

Assignment operators assign/update values.

| Operator | Equivalent   |
| -------- | ------------ |
| `=`      | `a = b`      |
| `+=`     | `a = a + b`  |
| `-=`     | `a = a - b`  |
| `*=`     | `a = a * b`  |
| `/=`     | `a = a / b`  |
| `%=`     | `a = a % b`  |
| `**=`    | `a = a ** b` |
| `//=`    | `a = a // b` |

Example:

```python
a = 10
b = 3

a += b
print(a)
```

Output:

```text
13
```

Because:

```python
a += b
```

means:

```python
a = a + b
```

---

### `-=`

```python
a = 10
b = 3

a -= b

print(a)
```

Output:

```text
7
```

---

### `*=`

```python
a = 10
b = 3

a *= b

print(a)
```

Output:

```text
30
```

---

### `/=`

```python
a = 10
b = 3

a /= b

print(a)
```

Output:

```text
3.3333333333333335
```

---

### `%=`

```python
a = 10
b = 3

a %= b

print(a)
```

Output:

```text
1
```

---

### `**=`

```python
a = 10
b = 3

a **= b

print(a)
```

Output:

```text
1000
```

**Correction to the original notes:** `a **= b` here gives `10 ** 3 = 1000`, not `1`.

---

### `//=`

```python
a = 10
b = 3

a //= b

print(a)
```

Output:

```text
3
```

---

# 6.3 Comparison Operators

Comparison operators compare two values.

The result is always:

```python
True
```

or

```python
False
```

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

Example:

```python
a = 10
b = 3
```

```python
print(a == b)
```

Output:

```text
False
```

```python
print(a != b)
```

Output:

```text
True
```

```python
print(a > b)
```

Output:

```text
True
```

```python
print(a < b)
```

Output:

```text
False
```

```python
print(a >= b)
```

Output:

```text
True
```

```python
print(a <= b)
```

Output:

```text
False
```

---

## `=` vs `==`

Very important:

### `=`

Assignment

```python
age = 25
```

Means:

> Store 25 in `age`.

### `==`

Comparison

```python
age == 25
```

Means:

> Is `age` equal to 25?

---

# 6.4 Logical Operators

Logical operators combine or modify conditions.

Python has:

```python
and
or
not
```

---

## `and`

Returns `True` when **both conditions are True**.

```python
a = 10
b = 3

print(a > 5 and b < 5)
```

Both are true:

```text
10 > 5 → True
3 < 5  → True
```

Therefore:

```text
True
```

### Truth table

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

---

## `or`

Returns `True` if **at least one condition is True**.

```python
a = 10
b = 3

print(a > 5 or b > 5)
```

```text
a > 5 → True
b > 5 → False
```

At least one is true, so:

```text
True
```

### Truth table

| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

---

## `not`

Reverses a Boolean value.

```python
a = 10

print(not(a > 5))
```

`a > 5` is:

```text
True
```

`not True` becomes:

```text
False
```

Therefore:

```text
False
```

### Truth table

| A     | not A |
| ----- | ----- |
| True  | False |
| False | True  |

---

# 6.5 Bitwise Operators

Bitwise operators work at the **binary/bit level** of integers.

Important operators:

| Operator | Meaning     |            |
| -------- | ----------- | ---------- |
| `&`      | Bitwise AND |            |
| `        | `           | Bitwise OR |
| `^`      | Bitwise XOR |            |
| `~`      | Bitwise NOT |            |
| `<<`     | Left shift  |            |
| `>>`     | Right shift |            |

Example:

```python
a = 5
b = 3
```

Binary:

```text
5 = 101
3 = 011
```

### Bitwise AND

```python
print(a & b)
```

```text
101
011
---
001
```

Output:

```text
1
```

### Bitwise OR

```python
print(a | b)
```

```text
101
011
---
111
```

Output:

```text
7
```

### Bitwise XOR

```python
print(a ^ b)
```

```text
101
011
---
110
```

Output:

```text
6
```

Bitwise operators become particularly important when studying low-level programming, networking, permissions, algorithms, and some interview questions.

---

# 6.6 Membership Operators

Membership operators check whether a value exists inside a sequence/container.

Operators:

```python
in
not in
```

Example:

```python
name = "Indra"

print("I" in name)
```

Output:

```text
True
```

```python
print("z" in name)
```

Output:

```text
False
```

Example with a list:

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

Output:

```text
True
```

---

# 6.7 Identity Operators

Identity operators check whether two variables refer to the **same object**.

Operators:

```python
is
is not
```

Example:

```python
a = None

print(a is None)
```

Output:

```text
True
```

### Important

Do not generally use `is` when you want to compare values.

Use:

```python
==
```

for value equality.

Use:

```python
is
```

for object identity.

---

# 7. Strings in Python

A string is a sequence of characters.

Strings can be written using:

### Single quotes

```python
name = 'Indra'
```

### Double quotes

```python
name = "Indra"
```

### Triple quotes

```python
message = """Hello Python"""
```

---

# Strings Are Immutable

Strings are **immutable**.

This means once a string object is created, its individual characters cannot be changed.

Example:

```python
word = "hello"

# word[0] = "H"
```

This produces an error because strings cannot be modified character-by-character.

Instead, create a new string:

```python
word = "hello"

word = "H" + word[1:]

print(word)
```

Output:

```text
Hello
```

---

# String Indexing

Each character has an index.

Consider:

```python
word = "Python"
```

Indexes:

```text
 P   y   t   h   o   n
 0   1   2   3   4   5
```

Python uses **zero-based indexing**.

Therefore:

```python
print(word[0])
```

Output:

```text
P
```

```python
print(word[3])
```

Output:

```text
h
```

---

## Negative Indexing

Python also supports negative indexes.

```text
 P   y   t   h   o   n
 0   1   2   3   4   5
-6  -5  -4  -3  -2  -1
```

Therefore:

```python
print(word[-1])
```

Output:

```text
n
```

`-1` means the last character.

---

# String Slicing

Syntax:

```python
string[start:stop:step]
```

Important:

> The `stop` index is excluded.

Example:

```python
word = "hello world Python"
```

```python
print(word[0:5])
```

Output:

```text
hello
```

Indexes:

```text
h e l l o
0 1 2 3 4
```

`5` is excluded.

---

## Slicing `world`

```python
print(word[6:11])
```

Output:

```text
world
```

---

## Step

```python
print(word[::2])
```

This takes every second character.

---

## Start, Stop and Step

```python
print(word[5:10:2])
```

Meaning:

```text
start = 5
stop  = 10
step  = 2
```

---

## Reverse a String

```python
print(word[::-1])
```

This reverses the string.

Example:

```python
word = "hello"

print(word[::-1])
```

Output:

```text
olleh
```

---

# 8. String Methods

Python provides many built-in string methods.

---

## 8.1 `len()`

Returns the number of characters.

```python
word = "hello"

print(len(word))
```

Output:

```text
5
```

Spaces are also counted.

```python
word = "hello world"

print(len(word))
```

Output:

```text
11
```

---

## 8.2 `upper()`

Converts characters to uppercase.

```python
word = "hello"

print(word.upper())
```

Output:

```text
HELLO
```

---

## 8.3 `lower()`

Converts characters to lowercase.

```python
word = "HELLO"

print(word.lower())
```

Output:

```text
hello
```

---

## 8.4 `strip()`

Removes leading and trailing whitespace.

```python
word = "   hello   "

print(word.strip())
```

Output:

```text
hello
```

It does not remove spaces in the middle.

```python
"hello   world".strip()
```

remains:

```text
hello   world
```

---

## 8.5 `replace()`

Replaces part of a string.

```python
word = "hello world"

print(word.replace("world", "Python"))
```

Output:

```text
hello Python
```

Important: strings are immutable, so `replace()` returns a **new string**.

---

## 8.6 `split()`

Splits a string into a list.

```python
word = "hello world Python"

print(word.split())
```

Output:

```text
['hello', 'world', 'Python']
```

You can specify a separator:

```python
data = "apple,banana,mango"

print(data.split(","))
```

Output:

```text
['apple', 'banana', 'mango']
```

---

## 8.7 `join()`

`join()` combines multiple strings into one string.

```python
words = ["Hello", "Python", "World"]

result = " ".join(words)

print(result)
```

Output:

```text
Hello Python World
```

Another example:

```python
words = ["2026", "09", "06"]

print("-".join(words))
```

Output:

```text
2026-09-06
```

### Remember

`split()`:

```text
String → List
```

`join()`:

```text
List of strings → String
```

---

## 8.8 `find()`

Returns the index of the first occurrence of a substring.

```python
word = "hello world"

print(word.find("world"))
```

Output:

```text
6
```

If the substring is not found:

```python
print(word.find("Python"))
```

Output:

```text
-1
```

---

## 8.9 `count()`

Counts how many times a substring occurs.

```python
word = "hello"

print(word.count("l"))
```

Output:

```text
2
```

---

## 8.10 `isalpha()`

Returns `True` if all characters are alphabetic.

```python
print("Hello".isalpha())
```

Output:

```text
True
```

But:

```python
print("Hello123".isalpha())
```

Output:

```text
False
```

---

## 8.11 `isdigit()`

Returns `True` if all characters are digits.

```python
print("12345".isdigit())
```

Output:

```text
True
```

```python
print("123a".isdigit())
```

Output:

```text
False
```

---

## 8.12 `isspace()`

Checks whether all characters are whitespace.

```python
print("   ".isspace())
```

Output:

```text
True
```

```python
print("Hello".isspace())
```

Output:

```text
False
```

---

## 8.13 `startswith()`

Checks whether a string starts with a particular value.

```python
word = "hello world"

print(word.startswith("hello"))
```

Output:

```text
True
```

---

## 8.14 `endswith()`

Checks whether a string ends with a particular value.

```python
word = "hello world"

print(word.endswith("world"))
```

Output:

```text
True
```

---

## 8.15 `capitalize()`

Makes the first character uppercase and the remaining characters lowercase.

```python
word = "hello WORLD"

print(word.capitalize())
```

Output:

```text
Hello world
```

---

## 8.16 `title()`

Converts the first character of each word to uppercase.

```python
text = "hello world python"

print(text.title())
```

Output:

```text
Hello World Python
```

---

# Important String Methods — Quick Revision

| Method         | Purpose                            |
| -------------- | ---------------------------------- |
| `len()`        | Length of string                   |
| `upper()`      | Uppercase                          |
| `lower()`      | Lowercase                          |
| `strip()`      | Remove leading/trailing whitespace |
| `replace()`    | Replace text                       |
| `split()`      | String → list                      |
| `join()`       | List of strings → string           |
| `find()`       | Find first index                   |
| `count()`      | Count occurrences                  |
| `isalpha()`    | Check alphabetic characters        |
| `isdigit()`    | Check digits                       |
| `isspace()`    | Check whitespace                   |
| `startswith()` | Check beginning                    |
| `endswith()`   | Check ending                       |
| `capitalize()` | Capitalize first character         |
| `title()`      | Title Case                         |

---

# 9. f-Strings

## What is an f-string?

An **f-string** is a convenient way to insert variables and expressions directly inside a string.

Syntax:

```python
f"some text {variable}"
```

Example:

```python
name = "Alice"
age = 30

print(f"Hello, {name}! You are {age} years old.")
```

Output:

```text
Hello, Alice! You are 30 years old.
```

---

# Without f-string

You could write:

```python
print("Hello, " + name + "! You are " + str(age) + " years old.")
```

Notice that `age` needs to be converted to a string:

```python
str(age)
```

---

# Using `.format()`

Another approach is:

```python
print("Hello, {}! You are {} years old.".format(name, age))
```

---

# Using f-string

The modern and cleaner approach:

```python
print(f"Hello, {name}! You are {age} years old.")
```

### Comparison

```python
# Concatenation
"Hello " + name

# format()
"Hello {}".format(name)

# f-string
f"Hello {name}"
```

For modern Python code, f-strings are usually the most readable option.

---

# Expressions inside f-strings

You can put expressions inside `{}`.

```python
a = 10
b = 20

print(f"Sum = {a + b}")
```

Output:

```text
Sum = 30
```

Another example:

```python
age = 25

print(f"Next year you will be {age + 1}")
```

Output:

```text
Next year you will be 26
```

---

# Decimal Formatting with f-strings

This is especially useful when displaying marks, prices, percentages, averages, etc.

```python
total_marks = 10
marks_obtained = 3

ans = total_marks / marks_obtained

print(ans)
```

Output:

```text
3.3333333333333335
```

To display exactly 4 digits after the decimal:

```python
print(f"{ans:.4f}")
```

Output:

```text
3.3333
```

To display exactly 2 digits:

```python
print(f"{ans:.2f}")
```

Output:

```text
3.33
```

To display exactly 1 digit:

```python
print(f"{ans:.1f}")
```

Output:

```text
3.3
```

---

## Understanding `.2f`

```python
f"{ans:.2f}"
```

Breakdown:

```text
:    → formatting starts
.2   → 2 digits after decimal
f    → floating-point format
```

Therefore:

```python
ans = 3.333333

print(f"{ans:.2f}")
```

Output:

```text
3.33
```

---

## `.format()` alternative

```python
print("{:.2f}".format(ans))
```

Output:

```text
3.33
```

---

# 10. Docstrings

## What is a Docstring?

A **docstring** is a string used to document a:

* Module
* Function
* Class

Docstrings are generally written immediately after the definition.

Example:

```python
def add_numbers(a, b):
    """
    Adds two numbers and returns the result.
    """
    return a + b
```

The string:

```python
"""
Adds two numbers and returns the result.
"""
```

is the function's docstring.

---

# Accessing a Docstring

Python stores a function's documentation in:

```python
__doc__
```

Example:

```python
def add_numbers(a, b):
    """
    This function takes two numbers
    and returns their sum.
    """
    return a + b


print(add_numbers.__doc__)
```

Output:

```text
This function takes two numbers
and returns their sum.
```

---

# Complete Docstring Example

```python
def add_numbers(a, b):
    """
    Add two numbers.

    Parameters:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        int or float: Sum of a and b.
    """
    return a + b


print(add_numbers(5, 10))
print(add_numbers.__doc__)
```

Output:

```text
15

    Add two numbers.

    Parameters:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        int or float: Sum of a and b.
```

---

# Comments vs Docstrings

This is important.

## Comment

A comment starts with `#`.

```python
# This function adds two numbers
```

Comments are mainly for developers reading the source code.

## Docstring

A docstring is a string placed in the appropriate documentation position.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

Python can access the docstring:

```python
print(add.__doc__)
```

So:

```text
Comment → #
Docstring → """ ... """
```

---

# Complete Revision Sheet

## Variables

```python
name = "Indra"
age = 25
height = 5.6
is_student = True
```

A variable refers to an object/value.

Python is dynamically typed.

---

## Data Types

```python
int
float
complex
bool
str
list
tuple
set
dict
```

Examples:

```python
10
10.5
1 + 2j
True
"Hello"
[1, 2, 3]
(1, 2, 3)
{1, 2, 3}
{"name": "Indra"}
```

---

## Type Conversion

```python
int("10")
float("10.5")
str(100)
bool(1)
```

---

## User Input

```python
name = input("Enter name: ")
```

`input()` always returns a string.

For integer:

```python
age = int(input("Enter age: "))
```

For float:

```python
height = float(input("Enter height: "))
```

---

## Arithmetic Operators

```text
+    Addition
-    Subtraction
*    Multiplication
/    Division
%    Modulus
**   Exponentiation
//   Floor division
```

---

## Assignment Operators

```text
=
+=
-=
*=
/=
%=
**=
//=
```

---

## Comparison Operators

```text
==
!=
>
<
>=
<=
```

Result:

```text
True / False
```

---

## Logical Operators

```text
and
or
not
```

---

## Bitwise Operators

```text
&
|
^
~
<<
>>
```

---

## Membership Operators

```text
in
not in
```

---

## Identity Operators

```text
is
is not
```

---

## Strings

```python
name = "Indra"
```

Strings:

* Are sequences of characters
* Are immutable
* Support indexing
* Support slicing

---

## Indexing

```python
word = "Python"

word[0]     # P
word[-1]    # n
```

---

## Slicing

```python
word[start:stop:step]
```

Examples:

```python
word[0:3]
word[::2]
word[::-1]
```

---

## Important String Methods

```python
len()
upper()
lower()
strip()
replace()
split()
join()
find()
count()
isalpha()
isdigit()
isspace()
startswith()
endswith()
capitalize()
title()
```

---

## f-Strings

```python
name = "Indra"
age = 25

print(f"My name is {name} and I am {age} years old.")
```

Decimal formatting:

```python
print(f"{3.333333:.2f}")
```

Output:

```text
3.33
```

---

## Docstrings

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

Access:

```python
print(add.__doc__)
```

---

# Important Corrections from the Original Class Notes

### 1. `a **= b`

Your original note showed:

```python
a = 10
a **= b
```

with output `1`.

That is incorrect if `b = 3`.

Correct:

```python
a = 10
b = 3

a **= b

print(a)
```

Output:

```text
1000
```

because:

```text
10 ** 3 = 1000
```

---

### 2. `age + 10`

If:

```python
age = 25
```

then:

```python
age + 10
```

gives:

```text
35
```

not `33`.

---

### 3. Division

Python's `/` operator returns a float:

```python
10 / 3
```

Output:

```text
3.3333333333333335
```

If you want:

```text
3.33
```

use:

```python
f"{10 / 3:.2f}"
```

---

### 4. `int()` does not round

```python
int(5.9)
```

gives:

```text
5
```

It removes the decimal portion.

---

### 5. `find()` vs `index()`

`find()` returns:

```text
-1
```

when the substring is not found.

```python
"hello".find("z")
```

Output:

```text
-1
```

`index()` behaves differently and raises an exception if the substring isn't found.

---

# Most Important Things to Remember

```text
Variable
    ↓
Name referring to an object

Data Type
    ↓
Defines what kind of object/value it is

input()
    ↓
Always returns str

Type Conversion
    ↓
int(), float(), str(), bool(), etc.

Operators
    ↓
Perform operations

String
    ↓
Sequence of characters
    ↓
Immutable
    ↓
Supports indexing and slicing

f-string
    ↓
Easy string formatting

Docstring
    ↓
Documentation for modules/classes/functions
```

## One-Line Interview Revision

**Variable:** A name that refers to an object.

**Dynamic typing:** Python determines the type at runtime, so explicit type declaration isn't required.

**Type casting/conversion:** Converting a value from one data type to another.

**`input()`:** Takes user input and returns it as a string.

**String:** An immutable sequence of Unicode characters.

**Indexing:** Accessing an individual character using its position.

**Slicing:** Extracting a portion of a sequence using `[start:stop:step]`.

**f-string:** A formatted string literal that allows expressions inside `{}`.

**Docstring:** A string used to document a module, class, or function.

**`==`:** Compares values.

**`=`:** Assigns a value.

**`is`:** Checks object identity.

**`in`:** Checks membership.

**`/`:** Normal division, returns a float.

**`//`:** Floor division.

**`%`:** Returns the remainder.

**`**`:** Exponentiation/power.
