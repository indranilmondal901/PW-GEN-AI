# ============================================================================
#                              PYTHON LIST
# ============================================================================

'''
===============================================================================
1. WHAT IS A LIST?
===============================================================================

A List is a built-in Python data structure used to store multiple values
(elements) in a single variable.

A list is created using square brackets [ ].

Example:

numbers = [10, 20, 30, 40, 50]

A list can contain:
    - Numbers
    - Strings
    - Boolean values
    - None
    - Other lists
    - Tuples
    - Dictionaries
    - Sets
    - Objects
    - Different data types together

Example:

mixed_list = ["Indranil", 28, 7.5, True, None]

===============================================================================
2. MAJOR PROPERTIES OF LIST
===============================================================================

1. ORDERED
   ---------------------------------------------------------------------------

   List elements maintain their insertion order.

   Example:

   my_list = ["A", "B", "C"]

   Order:

       A -> B -> C

   If we add "D":

       A -> B -> C -> D


2. MUTABLE
   ---------------------------------------------------------------------------

   Lists are mutable.

   Mutable means the contents of an existing list can be changed
   after the list has been created.

   We can:
       - Update elements
       - Add elements
       - Remove elements
       - Sort elements
       - Reverse elements

   Example:

   numbers = [10, 20, 30]

   numbers[1] = 200

   Result:

   [10, 200, 30]


3. INDEXED
   ---------------------------------------------------------------------------

   Every element in a list has an index.

   Positive indexing starts from 0.

   Example:

       0 -> 10
       1 -> 20
       2 -> 30
       3 -> 40

   Python also supports negative indexing.

       -4 -> 10
       -3 -> 20
       -2 -> 30
       -1 -> 40


4. ALLOWS DUPLICATES
   ---------------------------------------------------------------------------

   A list can contain duplicate values.

   Example:

   numbers = [10, 20, 10, 30, 10]

   Here, 10 appears three times.


5. HETEROGENEOUS
   ---------------------------------------------------------------------------

   A list can contain elements of different data types.

   Example:

   mixed_list = [10, "hello", 3.14, True, None]

   All elements do NOT need to have the same data type.


6. DYNAMIC SIZE
   ---------------------------------------------------------------------------

   A list can grow or shrink during program execution.

   Elements can be added:

       numbers.append(60)

   Elements can be removed:

       numbers.pop()

   Therefore, the size of a list is not fixed.


7. ITERABLE
   ---------------------------------------------------------------------------

   A list is iterable.

   This means we can access its elements one by one using a loop.

   Example:

   numbers = [10, 20, 30]

   for number in numbers:
       print(number)


8. SEQUENCE TYPE
   ---------------------------------------------------------------------------

   List is a sequence data type in Python.

   Other common sequence types:

       - str
       - list
       - tuple
       - range

   Because List is a sequence, it supports:

       - Indexing
       - Slicing
       - Iteration
       - Membership testing
       - len()


9. NESTED
   ---------------------------------------------------------------------------

   A list can contain another list.

   This is called a nested list.

   Example:

   matrix = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ]

   A list can also contain other data structures such as:

       - List
       - Tuple
       - Dictionary
       - Set


===============================================================================
3. CREATING LISTS
===============================================================================

A list can be created mainly in two ways:

    1. Using square brackets []
    2. Using list() constructor

Example:

mylst1 = []
mylst2 = list()

Both create an empty list.

'''

mylst1 = []
mylst2 = list()

print(mylst1)
# []

print(mylst2)
# []


'''
list() can also convert another iterable into a list.

Examples:
'''

print(list("hello"))
# ['h', 'e', 'l', 'l', 'o']

print(list((10, 20, 30)))
# [10, 20, 30]


# ============================================================================
# 4. EMPTY LIST
# ============================================================================

'''
An empty list is a list containing zero elements.

Examples:

list1 = []
list2 = list()

Both are empty lists.

We can check the number of elements using len().
'''

list1 = []
list2 = list()

print(len(list1))
# 0

print(len(list2))
# 0


# ============================================================================
# 5. LIST WITH DIFFERENT DATA TYPES
# ============================================================================

'''
A Python list can contain different data types at the same time.
'''

mixed_list = [
    "Indranil",
    28,
    7.5,
    True,
    None
]

print(mixed_list)
# ['Indranil', 28, 7.5, True, None]


# ============================================================================
# 6. LIST WITH DUPLICATE VALUES
# ============================================================================

'''
Lists allow duplicate values.
'''

duplicate_list = [10, 20, 10, 30, 10]

print(duplicate_list)
# [10, 20, 10, 30, 10]


# ============================================================================
# 7. ORDERED PROPERTY
# ============================================================================

'''
Lists preserve the order in which elements are inserted.
'''

my_list = ["A", "B", "C"]

my_list.append("D")

print(my_list)
# ['A', 'B', 'C', 'D']


# ============================================================================
# 8. MUTABLE PROPERTY
# ============================================================================

'''
Lists are mutable.

Mutable means the contents of an existing list can be changed.
'''

numbers = [10, 20, 30]

numbers[1] = 200

print(numbers)
# [10, 200, 30]


# ============================================================================
# 9. INDEXING
# ============================================================================

'''
Positive indexing:

    0 -> first element
    1 -> second element
    2 -> third element
    ...

Negative indexing:

    -1 -> last element
    -2 -> second-last element
    -3 -> third-last element
    ...

Example:

random_list = ["muskan", "rohit", "rahul", 50, 20, 10]

Positive indexing:

    0 -> muskan
    1 -> rohit
    2 -> rahul
    3 -> 50
    4 -> 20
    5 -> 10

Negative indexing:

    -6 -> muskan
    -5 -> rohit
    -4 -> rahul
    -3 -> 50
    -2 -> 20
    -1 -> 10
'''

random_list = ["muskan", "rohit", "rahul", 50, 20, 10]

print(random_list)
# ['muskan', 'rohit', 'rahul', 50, 20, 10]

print(random_list[0])
# muskan

print(random_list[5])
# 10

print(random_list[-1])
# 10

print(random_list[-6])
# muskan


# ============================================================================
# 10. SLICING
# ============================================================================

'''
Syntax:

    list[start : stop : step]

Important:

    start -> included
    stop  -> excluded
    step  -> optional

Example:

numbers = [10, 20, 30, 40, 50]

numbers[1:4]

Indexes 1, 2 and 3 are included.

Index 4 is excluded.

Result:

[20, 30, 40]
'''

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
# [20, 30, 40]

print(numbers[:3])
# [10, 20, 30]

print(numbers[2:])
# [30, 40, 50]

print(numbers[::2])
# [10, 30, 50]

print(numbers[::-1])
# [50, 40, 30, 20, 10]


# ============================================================================
# 11. UPDATING ELEMENTS
# ============================================================================

'''
Because List is mutable, we can update an existing element using its index.
'''

random_list = ["muskan", "rohit", "rahul", 50, 20, 10]

random_list[1] = "indra"

print(random_list)
# ['muskan', 'indra', 'rahul', 50, 20, 10]


# ============================================================================
# 12. ADDING ELEMENTS
# ============================================================================


# ----------------------------------------------------------------------------
# 12.1 append()
# ----------------------------------------------------------------------------

'''
append(value)

Adds ONE element at the end of the list.

Syntax:

    list.append(value)

The element is added as a single element.
'''

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
# [10, 20, 30, 40]


'''
If we append a list, the entire list becomes ONE element.
'''

numbers = [10, 20, 30]

numbers.append([40, 50])

print(numbers)
# [10, 20, 30, [40, 50]]


# ----------------------------------------------------------------------------
# 12.2 insert()
# ----------------------------------------------------------------------------

'''
insert(index, value)

Adds an element at a particular index.

Syntax:

    list.insert(index, value)

Existing elements are shifted to the right.
'''

numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)
# [10, 15, 20, 30]


# ----------------------------------------------------------------------------
# 12.3 extend()
# ----------------------------------------------------------------------------

'''
extend(iterable)

Adds multiple elements to the existing list.

Each element of the iterable is added individually.
'''

numbers = [10, 20, 30]

numbers.extend([40, 50, 60])

print(numbers)
# [10, 20, 30, 40, 50, 60]


'''
Difference between append() and extend():

append():

    list1 = [1, 2]
    list1.append([3, 4])

    Result:
    [1, 2, [3, 4]]


extend():

    list2 = [1, 2]
    list2.extend([3, 4])

    Result:
    [1, 2, 3, 4]
'''


# ============================================================================
# 13. REMOVING ELEMENTS
# ============================================================================


# ----------------------------------------------------------------------------
# 13.1 remove()
# ----------------------------------------------------------------------------

'''
remove(value)

Removes the FIRST occurrence of the specified value.

It modifies the original list.

Return value:
    None

If the value does not exist:
    ValueError
'''

numbers = [10, 20, 10, 30]

result = numbers.remove(10)

print(result)
# None

print(numbers)
# [20, 10, 30]


# ----------------------------------------------------------------------------
# 13.2 pop()
# ----------------------------------------------------------------------------

'''
pop()

Removes and RETURNS an element.

Without an index:
    Removes the LAST element.

With an index:
    Removes the element at that index.

Important:
    pop() returns the removed element.
'''

numbers = [10, 20, 30, 40]

removed_item = numbers.pop()

print(removed_item)
# 40

print(numbers)
# [10, 20, 30]


removed_item = numbers.pop(1)

print(removed_item)
# 20

print(numbers)
# [10, 30]


# ----------------------------------------------------------------------------
# 13.3 clear()
# ----------------------------------------------------------------------------

'''
clear()

Removes ALL elements from the list.

The list itself still exists.
'''

numbers = [10, 20, 30]

numbers.clear()

print(numbers)
# []


# ----------------------------------------------------------------------------
# 13.4 del
# ----------------------------------------------------------------------------

'''
del is a Python keyword, NOT a List method.

It can be used to delete:

    - A specific element
    - A range of elements
    - The entire variable
'''

numbers = [10, 20, 30, 40, 50]

del numbers[2]

print(numbers)
# [10, 20, 40, 50]


'''
Deleting multiple elements using slicing:
'''

numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print(numbers)
# [10, 50]


# ============================================================================
# 14. SEARCHING / CHECKING
# ============================================================================


# ----------------------------------------------------------------------------
# 14.1 in
# ----------------------------------------------------------------------------

'''
"in" checks whether a value exists in the list.

It returns True or False.
'''

numbers = [10, 20, 30, 40, 50]

print(30 in numbers)
# True

print(100 in numbers)
# False


# ----------------------------------------------------------------------------
# 14.2 not in
# ----------------------------------------------------------------------------

'''
"not in" checks whether a value does NOT exist in the list.
'''

print(100 not in numbers)
# True

print(30 not in numbers)
# False


# ----------------------------------------------------------------------------
# 14.3 count()
# ----------------------------------------------------------------------------

'''
count(value)

Returns the number of times a value occurs in the list.
'''

numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))
# 3

print(numbers.count(50))
# 0


# ----------------------------------------------------------------------------
# 14.4 index()
# ----------------------------------------------------------------------------

'''
index(value)

Returns the index of the FIRST occurrence of the specified value.

If the value does not exist:
    ValueError
'''

numbers = [10, 20, 10, 30]

print(numbers.index(10))
# 0

print(numbers.index(30))
# 3


# ============================================================================
# 15. SORTING
# ============================================================================


# ----------------------------------------------------------------------------
# 15.1 sorted()
# ----------------------------------------------------------------------------

'''
sorted(list)

Returns a NEW sorted list.

The original list remains unchanged.
'''

random_number_list = [100, 20, 10, 50, 90, 80, 5, 15, 2]

print(sorted(random_number_list))
# [2, 5, 10, 15, 20, 50, 80, 90, 100]

print(random_number_list)
# [100, 20, 10, 50, 90, 80, 5, 15, 2]


# ----------------------------------------------------------------------------
# 15.2 sort()
# ----------------------------------------------------------------------------

'''
list.sort()

Sorts the ORIGINAL list.

It modifies the existing list.

Return value:
    None
'''

random_number_list.sort()

print(random_number_list)
# [2, 5, 10, 15, 20, 50, 80, 90, 100]


'''
Descending order:

list.sort(reverse=True)
'''

random_number_list.sort(reverse=True)

print(random_number_list)
# [100, 90, 80, 50, 20, 15, 10, 5, 2]


# ============================================================================
# 16. REVERSING
# ============================================================================


# ----------------------------------------------------------------------------
# 16.1 reversed()
# ----------------------------------------------------------------------------

'''
reversed(list)

Returns a reverse iterator.

It does NOT return a list directly.

Therefore:

    print(reversed(mylist))

will show something similar to:

    <list_reverseiterator object at 0x000001...>

To convert it into a list:

    list(reversed(mylist))
'''

random_number_list = [2, 5, 10, 15, 20, 50, 80, 90, 100]

print(reversed(random_number_list))
# <list_reverseiterator object at 0x000001...>

print(list(reversed(random_number_list)))
# [100, 90, 80, 50, 20, 15, 10, 5, 2]

print(random_number_list)
# [2, 5, 10, 15, 20, 50, 80, 90, 100]

'''
Important:

reversed(list)
    -> returns reverse iterator
    -> original list is NOT changed
'''


# ----------------------------------------------------------------------------
# 16.2 reverse()
# ----------------------------------------------------------------------------

'''
list.reverse()

Reverses the ORIGINAL list.

Return value:
    None
'''

random_number_list.reverse()

print(random_number_list)
# [100, 90, 80, 50, 20, 15, 10, 5, 2]


# ----------------------------------------------------------------------------
# 16.3 [::-1]
# ----------------------------------------------------------------------------

'''
[::-1]

Creates a NEW reversed list using slicing.

The original list remains unchanged.
'''

numbers = [10, 20, 30, 40, 50]

reversed_numbers = numbers[::-1]

print(reversed_numbers)
# [50, 40, 30, 20, 10]

print(numbers)
# [10, 20, 30, 40, 50]


# ============================================================================
# 17. LIST OPERATORS
# ============================================================================


# ----------------------------------------------------------------------------
# 17.1 + Operator
# ----------------------------------------------------------------------------

'''
+ is used for List concatenation.

It combines two lists into a NEW list.
'''

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)
# [1, 2, 3, 4, 5, 6]

print(list1)
# [1, 2, 3]

print(list2)
# [4, 5, 6]


# ----------------------------------------------------------------------------
# 17.2 * Operator
# ----------------------------------------------------------------------------

'''
* is used for List repetition.

Example:

list * 2

repeats the list two times.
'''

numbers = [1, 2, 3]

print(numbers * 2)
# [1, 2, 3, 1, 2, 3]


# ============================================================================
# 18. NESTED LISTS
# ============================================================================

'''
A list inside another list is called a Nested List.

Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

We can use multiple indexes to access nested elements.
'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
# [1, 2, 3]

print(matrix[0][1])
# 2

print(matrix[2][2])
# 9


# ============================================================================
# 19. LIST COPY / REFERENCE
# ============================================================================


# ----------------------------------------------------------------------------
# 19.1 Reference Assignment
# ----------------------------------------------------------------------------

'''
When we do:

    list2 = list1

Python does NOT create a new list.

Both variables refer to the SAME list object.

Therefore, changing list2 also affects list1.
'''

list1 = [10, 20, 30]

list2 = list1

list2[0] = 100

print(list1)
# [100, 20, 30]

print(list2)
# [100, 20, 30]


# ----------------------------------------------------------------------------
# 19.2 copy()
# ----------------------------------------------------------------------------

'''
copy()

Creates a SHALLOW COPY of the list.

The new list is a separate list object.
'''

list1 = [10, 20, 30]

list2 = list1.copy()

list2[0] = 100

print(list1)
# [10, 20, 30]

print(list2)
# [100, 20, 30]


# ----------------------------------------------------------------------------
# 19.3 Copy using slicing
# ----------------------------------------------------------------------------

'''
We can also create a shallow copy using:

    list2 = list1[:]
'''

list1 = [10, 20, 30]

list2 = list1[:]

list2[0] = 100

print(list1)
# [10, 20, 30]

print(list2)
# [100, 20, 30]


# ----------------------------------------------------------------------------
# 19.4 Copy using list()
# ----------------------------------------------------------------------------

'''
Another way to create a shallow copy:

    list2 = list(list1)
'''

list1 = [10, 20, 30]

list2 = list(list1)

list2[0] = 100

print(list1)
# [10, 20, 30]

print(list2)
# [100, 20, 30]


# ============================================================================
# 20. IMPORTANT DIFFERENCES
# ============================================================================

'''
===============================================================================
APPEND vs EXTEND
===============================================================================

append():

    list1 = [1, 2]
    list1.append([3, 4])

    Result:

    [1, 2, [3, 4]]


extend():

    list2 = [1, 2]
    list2.extend([3, 4])

    Result:

    [1, 2, 3, 4]


===============================================================================
REMOVE vs POP
===============================================================================

remove(value):

    - Removes by VALUE
    - Removes first occurrence
    - Returns None

pop(index):

    - Removes by INDEX
    - Returns the removed element
    - Without index -> removes last element


===============================================================================
SORTED vs SORT
===============================================================================

sorted(list):

    - Built-in function
    - Returns a NEW sorted list
    - Original list remains unchanged

list.sort():

    - List method
    - Modifies the ORIGINAL list
    - Returns None


===============================================================================
REVERSED vs REVERSE
===============================================================================

reversed(list):

    - Built-in function
    - Returns a reverse iterator
    - Original list remains unchanged

list.reverse():

    - List method
    - Reverses the ORIGINAL list
    - Returns None


===============================================================================
REFERENCE vs COPY
===============================================================================

list2 = list1

    -> Same list object
    -> Changes affect both variables


list2 = list1.copy()

    -> New list object
    -> Changes to list2 do not affect list1


list2 = list1[:]

    -> New shallow copy


list2 = list(list1)

    -> New shallow copy
'''


# ============================================================================
# 21. QUICK REVISION TABLE
# ============================================================================

'''
+---------------------------+-----------------------------------------------+
| Method / Operation        | Purpose                                       |
+---------------------------+-----------------------------------------------+
| []                        | Create a list                                 |
| list()                    | Create / convert to a list                    |
| len(list)                 | Returns number of elements                    |
| list[index]               | Access element                               |
| list[start:stop]         | Slicing                                       |
| list[index] = value       | Update element                               |
| append(value)             | Add ONE element at the end                   |
| insert(index, value)     | Add element at a specific index              |
| extend(iterable)          | Add multiple elements                        |
| remove(value)             | Remove first matching value                  |
| pop()                     | Remove & return last element                 |
| pop(index)                | Remove & return element at index             |
| clear()                   | Remove all elements                          |
| del list[index]           | Delete element                               |
| value in list             | Check membership                             |
| value not in list         | Check non-membership                         |
| count(value)              | Count occurrences                            |
| index(value)              | First index of value                         |
| sorted(list)              | Return NEW sorted list                       |
| list.sort()               | Sort ORIGINAL list                           |
| reversed(list)            | Return reverse iterator                      |
| list.reverse()            | Reverse ORIGINAL list                        |
| list[::-1]                | Return NEW reversed list                     |
| list1 + list2             | Concatenate lists                            |
| list * n                  | Repeat list                                  |
| list.copy()               | Create shallow copy                          |
| list1 = list2             | Create reference, NOT a new list             |
+---------------------------+-----------------------------------------------+


===============================================================================
LIST MAJOR PROPERTIES
===============================================================================

    1. Ordered
    2. Mutable
    3. Indexed
    4. Allows duplicate values
    5. Heterogeneous
    6. Dynamic / Resizable
    7. Iterable
    8. Sequence type
    9. Supports slicing
    10. Supports membership testing
    11. Can contain nested lists
    12. Can contain different data structures


===============================================================================
IMPORTANT METHODS TO REMEMBER
===============================================================================

Adding:
    append()
    insert()
    extend()

Removing:
    remove()
    pop()
    clear()

Searching:
    count()
    index()

Sorting:
    sort()

Reversing:
    reverse()

Copying:
    copy()


===============================================================================
END OF LIST NOTES
===============================================================================
'''