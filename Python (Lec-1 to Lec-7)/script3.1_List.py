"""
1. List
2. Tuples
3. Dictionaries
4. Set
"""

# ============================================================================
#                              LIST
# ============================================================================

'''
===============================================================================
1. WHAT IS A LIST?
===============================================================================

A List is a built-in Python data structure used to store multiple values
(elements) in a single variable.

A list is written using square brackets [ ].

Example:

numbers = [10, 20, 30, 40, 50]

A list can contain:
    - Numbers
    - Strings
    - Boolean values
    - Other lists
    - Tuples
    - Dictionaries
    - Objects
    - Different data types together


Example of mixed data types:

mixed_list = ["Indranil", 28, 7.5, True, None]

===============================================================================
2. MAJOR PROPERTIES OF LIST
===============================================================================

1. ORDERED
   ----------------

   List elements maintain their insertion order.

   Example:

   my_list = ["A", "B", "C"]

   The order remains:

   A -> B -> C


2. MUTABLE
   ----------------

   A list can be modified after it has been created.

   We can:
       - Change an existing element
       - Add elements
       - Remove elements
       - Sort elements
       - Reverse elements

   Example:

   numbers = [10, 20, 30]

   numbers[1] = 200

   Result:

   [10, 200, 30]


3. ALLOWS DUPLICATE VALUES
   ----------------

   A list can contain the same value multiple times.

   Example:

   numbers = [10, 20, 10, 30, 10]

   Here, 10 appears three times.


4. INDEXED
   ----------------

   Every element has an index.

   Index starts from 0.

   Example:

   numbers = [10, 20, 30, 40]

   Index:

       0 -> 10
       1 -> 20
       2 -> 30
       3 -> 40

   Python also supports negative indexing:

      -4 -> 10
      -3 -> 20
      -2 -> 30
      -1 -> 40


5. SUPPORTS SLICING
   ----------------

   We can extract a portion of a list using slicing.

   Syntax:

   list[start : stop : step]

   Example:

   numbers = [10, 20, 30, 40, 50]

   numbers[1:4]

   Result:

   [20, 30, 40]


6. HETEROGENEOUS
   ----------------

   A Python list can contain elements of different data types.

   Example:

   mixed_list = [10, "hello", 3.14, True, None]

   Therefore, all elements do NOT need to be of the same data type.


7. DYNAMIC SIZE
   ----------------

   Python lists can grow or shrink during program execution.

   We can add elements:

   numbers.append(60)

   We can remove elements:

   numbers.pop()

   Therefore, the size of a list is not fixed.


8. CAN CONTAIN NESTED LISTS
   ----------------

   A list can contain another list.

   This is called a nested list.

   Example:

   matrix = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ]


9. CAN BE ITERATED
   ----------------

   We can use loops to access each element.

   Example:

   numbers = [10, 20, 30]

   for number in numbers:
       print(number)


10. SUPPORTS MEMBERSHIP TESTING
    ----------------

    We can check whether an element exists using:

        in
        not in

    Example:

    numbers = [10, 20, 30]

    print(20 in numbers)
    # True

    print(50 in numbers)
    # False


11. CAN BE NESTED WITH OTHER DATA STRUCTURES
    ----------------

    Lists can contain dictionaries, tuples, sets, other lists, etc.

    Example:

    students = [
        {"name": "Rahul", "age": 20},
        {"name": "Rohit", "age": 21}
    ]


12. LIST IS A SEQUENCE TYPE
    ----------------

    List belongs to Python's sequence data types.

    Common sequence types include:

        - str
        - list
        - tuple
        - range

    Because a list is a sequence, it supports:

        - Indexing
        - Slicing
        - Iteration
        - Membership testing
        - len()


===============================================================================
3. LIST CREATION
===============================================================================

We can create a list using:

    1. Square brackets []
    2. list() constructor


Example 1:

mylst1 = []


Example 2:

mylst2 = list()


Both create an empty list.

'''

mylst1 = []
mylst2 = list()

print(mylst1)
# []

print(mylst2)
# []


# ============================================================================
# 4. TYPE OF LIST
# ============================================================================

'''
The type of a list is:

<class 'list'>
'''

print(type(mylst1))
# <class 'list'>


# ============================================================================
# 5. EMPTY LIST
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
# 6. LIST WITH DIFFERENT DATA TYPES
# ============================================================================

'''
A list can contain different data types at the same time.
'''

mixed_list = [
    "Indranil",
    28,
    7.5,
    True,
    None
]

print(mixed_list)

'''
Possible output:

['Indranil', 28, 7.5, True, None]
'''


# ============================================================================
# 7. LIST WITH DUPLICATE VALUES
# ============================================================================

'''
Lists allow duplicate values.
'''

duplicate_list = [10, 20, 10, 30, 10]

print(duplicate_list)

# [10, 20, 10, 30, 10]


# ============================================================================
# 8. ORDERED PROPERTY
# ============================================================================

'''
Lists preserve the order in which elements are inserted.

Example:

my_list = ["A", "B", "C"]

The order is:

A -> B -> C

If we append "D":

A -> B -> C -> D
'''

my_list = ["A", "B", "C"]

my_list.append("D")

print(my_list)
# ['A', 'B', 'C', 'D']


# ============================================================================
# 9. MUTABLE PROPERTY
# ============================================================================

'''
Lists are mutable.

Mutable means:

    The contents of an existing list can be changed after creation.

Example:
'''

numbers = [10, 20, 30]

numbers[1] = 200

print(numbers)
# [10, 200, 30]


# ============================================================================
# 10. INDEXING
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

Positive:

    0 -> muskan
    1 -> rohit
    2 -> rahul
    3 -> 50
    4 -> 20
    5 -> 10

Negative:

   -6 -> muskan
   -5 -> rohit
   -4 -> rahul
   -3 -> 50
   -2 -> 20
   -1 -> 10
'''

random_list = ["muskan", "rohit", "rahul", 50, 20, 10]

print(random_list[0])
# muskan

print(random_list[-1])
# 10


# ============================================================================
# 11. SLICING
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

Result:

[20, 30, 40]
'''

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
# [20, 30, 40]


# ============================================================================
# 12. LIST CAN BE MODIFIED
# ============================================================================

'''
Because List is mutable, we can:

    - Update
    - Insert
    - Append
    - Extend
    - Remove
    - Pop
    - Clear
    - Sort
    - Reverse
'''

# ============================================================================
# List
# ============================================================================
mylst1 = list()
mylst2 = []

print(mylst1, mylst2)
# [],[]

print(type(mylst1)); # <class 'list'>
print(type(mylst2)); # <class 'list'>

random_list = ["muskan", "rohit", "rahul", 50, 20, 10] ; 

# ----------------------------------------------------------
# indexing in list
# ----------------------------------------------------------
# indexing like --> [negative indexing like string ]
# 0: muskan -------> -6
# 1: rohit  -------> -5
# 2: rahul  -------> -4
# 3: 50     -------> -3
# 4: 20     -------> -2
# 5: 10     -------> -1


print(random_list); #['muskan', 'rohit', 'rahul', 50, 20, 10]
# print(random_list.length)
print(random_list[0]); # muskan
print(random_list[5]); # 10

print(random_list[-1]); # 10
print(random_list[-6]); # muskan

# ----------------------------------------------------------
# update list value
# ----------------------------------------------------------
random_list[1] = "indra"; # "rohit" ---> "indra"
print("after update ----> ", random_list);

# ----------------------------------------------------------
# Slicing
# ----------------------------------------------------------
print(random_list);
# print(random_list[:1]); # print(random_list[0:1]); ---> splice start -> 0 and end at starting of 1st index ---> 0 index will be there
# print(random_list[2:1]); # [] --> it is actually wrong ---> splice start -> 2 and end at starting of 1st index
print(random_list[2:5]); # ['rahul', 50, 20] ---> splice start -> 2 and end at starting of 5th index ---> 2,3,4 indexes will be there

# ----------------------------------------------------------
# insert --> add in the particular index provided
# ----------------------------------------------------------
random_list.insert(0,"0 index")
random_list.insert(2,"2nd index")
print(random_list);

# ----------------------------------------------------------
# append --> add in the last index of list
# ----------------------------------------------------------
random_list.append("append");
print(random_list);

# ----------------------------------------------------------
#  extened --> we can add multiple item ata a time
# ----------------------------------------------------------
new_list = ["new1","new2","new30"];
random_list.extend(new_list);
print(random_list);

# ----------------------------------------------------------
#  remove: remove an element (not return new list)
# ----------------------------------------------------------
print(random_list); # ['0 index', 'muskan', '2nd index', 'indra', 'rahul', 50, 20, 10, 'append', 'new1', 'new2', 'new30']
random_list.remove("muskan");
print(random_list); # ['0 index', '2nd index', 'indra', 'rahul', 50, 20, 10, 'append', 'new1', 'new2', 'new30']

# ----------------------------------------------------------
#  pop: remove an element (return new list)
# ----------------------------------------------------------
print(random_list); # ['0 index', 'muskan', '2nd index', 'indra', 'rahul', 50, 20, 10, 'append', 'new1', 'new2', 'new30']
random_list.pop(); # without index always pop out last one

print(random_list); # ['0 index', '2nd index', 'indra', 'rahul', 50, 20, 10, 'append', 'new1', 'new2']

random_list.pop(2); # it will pop out index 2
print(random_list); # ['0 index', '2nd index', 'rahul', 50, 20, 10, 'append', 'new1', 'new2']

# ----------------------------------------------------------
#  clear: remove all element from list
# ----------------------------------------------------------
random_list.clear();
print(random_list);

# ----------------------------------------------------------
#  length of list
# ----------------------------------------------------------
numbers = [10,20,30,40,50];
#length
print(len(numbers)); # 5

# ----------------------------------------------------------
#  membership operator : return true/false 
# ----------------------------------------------------------
print(30 in numbers); # true
print(300 in numbers); # false

# ----------------------------------------------------------
#  sorting method
# ----------------------------------------------------------
random_number_list = [100,20,10,50,90,80,5,15,2];
print(sorted(random_number_list)); # [2, 5, 10, 15, 20, 50, 80, 90, 100]
print(random_number_list); # [100, 20, 10, 50, 90, 80, 5, 15, 2]
random_number_list.sort();
print(random_number_list); # [2, 5, 10, 15, 20, 50, 80, 90, 100]

# ----------------------------------------------------------
#  reverse method
# ----------------------------------------------------------
print(random_number_list); # [2, 5, 10, 15, 20, 50, 80, 90, 100]
print(reversed(random_number_list)); # <list_reverseiterator object at 0x000001...> ---> reversed() returns an iterator object, not a list.
print(list(reversed(random_number_list))); #[100, 90, 80, 50, 20, 15, 10, 5, 2]
print(random_number_list); # [2, 5, 10, 15, 20, 50, 80, 90, 100]
random_number_list.reverse();
print(random_number_list); # [100, 90, 80, 50, 20, 15, 10, 5, 2]

'''
|       Method                  |                   Result                   |
| `reversed(mylist)`            |           Reverse iterator                 |
| `list(reversed(mylist))`      |           New reversed list                |
| `mylist[::-1]`                |           New reversed list                |
| `mylist.reverse()`            |           Reverses the original list       |
'''