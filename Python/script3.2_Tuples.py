# ============================================================================
#                              PYTHON TUPLES
# ============================================================================

"""
===============================================================================
1. WHAT IS A TUPLE?
===============================================================================

A Tuple is a built-in Python data structure used to store multiple values
(elements) in a single variable.

A tuple is:
    - Ordered
    - Immutable
    - Allows duplicate values
    - Allows different data types
    - Supports indexing and slicing

A tuple is created using parentheses ( ).

Example:

    colors = ("red", "green", "yellow")

Think of a tuple as:

    List  ->  [10, 20, 30]   -> Mutable   -> Can be changed
    Tuple ->  (10, 20, 30)   -> Immutable -> Cannot be changed


===============================================================================
2. WHY DO WE NEED TUPLES IF LISTS ALREADY EXIST?
===============================================================================

The main difference is MUTABILITY.

LIST:
    - Mutable
    - Elements can be added, removed, or changed.

TUPLE:
    - Immutable
    - Once created, its elements cannot be changed.

Therefore, use a tuple when the collection of values should remain fixed.

Examples:
    - Days of the week
    - Months
    - Coordinates
    - Fixed configuration values
    - RGB color values

Example:

    coordinates = (10, 20)

Here, if the coordinates should remain fixed, a tuple is appropriate.


===============================================================================
3. CHARACTERISTICS OF TUPLES
===============================================================================

1. Ordered
   ------------------------------------------------
   Elements maintain their insertion order.

2. Immutable
   ------------------------------------------------
   Existing elements cannot be changed, added, or removed.

3. Allows Duplicate Values
   ------------------------------------------------
   Example:
       numbers = (10, 20, 10, 30)

4. Allows Different Data Types
   ------------------------------------------------
   Example:
       data = ("Python", 100, 10.5, True)

5. Supports Indexing
   ------------------------------------------------
   Each element has an index starting from 0.

6. Supports Slicing
   ------------------------------------------------
   We can extract a portion of a tuple using [start:stop].

7. Can Be Nested
   ------------------------------------------------
   A tuple can contain another tuple or other collections.


===============================================================================
4. CREATING A TUPLE
===============================================================================
"""

colors = ("red", "green", "yellow")

print(type(colors))
# <class 'tuple'>

print(colors)
# ('red', 'green', 'yellow')


"""
IMPORTANT:

Although parentheses are commonly used to create tuples, technically
the COMMA is what makes an object a tuple.

This is especially important when creating a tuple with only one element.
"""


# ============================================================================
# 5. TUPLE INDEXING
# ============================================================================

colors = ("red", "green", "yellow")

print(colors[0])
# red

print(colors[1])
# green

print(colors[2])
# yellow


"""
Indexing:

        ("red", "green", "yellow")
          0       1         2

Negative indexing:

        ("red", "green", "yellow")
         -3      -2        -1

So:

    colors[-1] -> "yellow"
    colors[-2] -> "green"
"""

print(colors[-1])
# yellow

print(colors[-2])
# green


# ============================================================================
# 6. TUPLE SLICING
# ============================================================================

"""
Syntax:

    tuple[start : stop]

IMPORTANT:
    start -> included
    stop  -> excluded

Example:

    colors[0:2]

means:

    index 0 -> included
    index 1 -> included
    index 2 -> excluded
"""

print(colors[0:2])
# ('red', 'green')


# Another example:

print(colors[1:3])
# ('green', 'yellow')


# ============================================================================
# 7. IMMUTABILITY
# ============================================================================

"""
A tuple is IMMUTABLE.

Immutable means:

    Once the tuple is created, its existing elements cannot be changed.

Example:

    colors[1] = "blue"

This produces:

    TypeError:
    'tuple' object does not support item assignment
"""

# colors[1] = "blue"
# TypeError: 'tuple' object does not support item assignment


"""
This is one of the most important differences between List and Tuple.

LIST:
    colors = ["red", "green", "yellow"]
    colors[1] = "blue"       # Allowed

TUPLE:
    colors = ("red", "green", "yellow")
    colors[1] = "blue"       # NOT Allowed


Mind Map:

                    COLLECTION
                        |
                -------------------
                |                 |
               LIST             TUPLE
                |                 |
             Mutable          Immutable
                |                 |
          Can be changed    Cannot be changed
"""


# ============================================================================
# 8. TUPLE SLICING CREATES A NEW TUPLE
# ============================================================================

colors = ("red", "green", "yellow")

colors2 = colors[0:2]

print(f"new tuple --> colors2 : {colors2}")
# new tuple --> colors2 : ('red', 'green')


"""
colors2 is a new tuple containing the selected elements.

Original tuple:

    colors = ("red", "green", "yellow")

Sliced tuple:

    colors2 = ("red", "green")
"""


# ============================================================================
# 9. SINGLE-ELEMENT TUPLE
# ============================================================================

"""
This is a VERY IMPORTANT concept.

Consider:

    single_item = ("Python")

This is NOT a tuple.

Why?

Because the comma is what makes it a tuple.

Python interprets:

    ("Python")

as simply:

    "Python"

Therefore:
"""

single_item = ("Python")

print(type(single_item))
# <class 'str'>

print(single_item)
# Python


"""
To create a tuple containing ONE element:

    ("Python",)

Notice the comma after "Python".
"""

single_item = ("Python",)

print(type(single_item))
# <class 'tuple'>

print(single_item)
# ('Python',)


"""
Remember:

    ("Python")   -> String
    ("Python",)  -> Tuple


The comma is the important part.

You can also write:

    single_item = "Python",

This is also a tuple because of the comma.
"""


# ============================================================================
# 10. TUPLE WITH DIFFERENT DATA TYPES
# ============================================================================

"""
A tuple can contain different types of values.
"""

mixed_data = ("Python", 100, 10.5, True)

print(mixed_data)
# ('Python', 100, 10.5, True)


# ============================================================================
# 11. DUPLICATE VALUES IN A TUPLE
# ============================================================================

"""
Tuples allow duplicate values.
"""

numbers = (10, 20, 30, 40, 50, 80, 10, 20, 900, 100, 2000)

print(numbers)


# ============================================================================
# 12. TUPLE METHODS
# ============================================================================

"""
Tuple has only TWO main built-in methods:

    1. count()
    2. index()

Why only two?

Because tuples are immutable.

Since we cannot modify a tuple, methods such as:

    append()
    remove()
    insert()
    pop()

are not available for tuples.

Those are List methods.


===============================================================================
12.1 count()
===============================================================================

count() returns the total number of times a particular element occurs
inside the tuple.

Syntax:

    tuple.count(value)
"""

numbers = (10, 20, 30, 40, 50, 80, 10, 20, 900, 100, 2000)

print(numbers.count(20))
# 2

print(numbers.count(10))
# 2

print(numbers.count(500))
# 0


"""
If the element does not exist, count() returns 0.
"""


# ============================================================================
# 13. index()
# ============================================================================

"""
index() returns the INDEX of the first occurrence of a specified value.

Syntax:

    tuple.index(value)

Example:
"""

numbers = (10, 20, 30, 40, 50, 80, 10, 20, 900, 100, 2000)

print(numbers.index(20))
# 1


"""
Why 1?

    Index:     0   1   2   3   4   5   6   7    8    9    10
    Value:    10  20  30  40  50  80  10  20  900  100  2000

The first 20 is at index 1.

There is another 20 at index 7.

index() returns the FIRST occurrence by default.
"""

print(numbers.index(20))
# 1


# ============================================================================
# 14. index() WITH START AND STOP
# ============================================================================

"""
Syntax:

    tuple.index(value, start, stop)

Parameters:

    value -> element to search for
    start -> starting index (included)
    stop  -> ending index (excluded)

Example:

    numbers.index(20, 0, 11)

means:

    Search for 20
    starting from index 0
    up to (but NOT including) index 11
"""

print(numbers.index(20, 0, 11))
# 1


"""
If we want to search after the first occurrence:

    numbers.index(20, 2, 11)

Python will ignore index 0 and 1 and search from index 2.
"""

print(numbers.index(20, 2, 11))
# 7


# ============================================================================
# 15. len() WITH TUPLES
# ============================================================================

"""
len() is NOT a tuple method.

It is a Python built-in function that returns the total number of elements
in a tuple.

Syntax:

    len(tuple)
"""

print(len(numbers))
# 11


"""
For our tuple:

    numbers = (
        10, 20, 30, 40, 50, 80,
        10, 20, 900, 100, 2000
    )

There are 11 elements.

Therefore:

    len(numbers) -> 11
"""


# ============================================================================
# 16. QUICK COMPARISON: LIST vs TUPLE
# ============================================================================

"""
                    LIST              TUPLE
------------------------------------------------------
Syntax              [ ]               ( )
Mutable              YES               NO
Ordered              YES               YES
Duplicates            YES               YES
Indexing              YES               YES
Slicing               YES               YES
Different types       YES               YES
append()              YES               NO
remove()              YES               NO
count()               YES               YES
index()               YES               YES

Main idea:

    LIST  -> Use when data may need to change.
    TUPLE -> Use when data should remain fixed.


===============================================================================
17. TUPLE MIND MAP
===============================================================================

                            TUPLE
                              |
             ---------------------------------
             |               |               |
          Ordered         Immutable       Duplicates
             |               |               |
          Indexing      Cannot modify       Allowed
             |
          Slicing
             |
      ----------------
      |              |
   count()         index()
      |              |
  occurrence     first index


===============================================================================
18. IMPORTANT POINTS TO REMEMBER
===============================================================================

1. Tuple is an ordered collection.

2. Tuple is immutable.

3. Tuple allows duplicate values.

4. Tuple can store different data types.

5. Indexing starts from 0.

6. Slicing follows:

       [start : stop]

   start is included.
   stop is excluded.

7. The comma creates a tuple, especially for a single element:

       ("Python")   -> str
       ("Python",)  -> tuple

8. Tuple has two main methods:

       count()
       index()

9. len() is a built-in function, NOT a tuple method.

10. A tuple cannot be modified using item assignment:

       colors[1] = "blue"    # TypeError

11. Lists are generally used for changeable collections.
    Tuples are generally used for fixed collections.
"""


# ============================================================================
# END OF TUPLE NOTES
# ============================================================================