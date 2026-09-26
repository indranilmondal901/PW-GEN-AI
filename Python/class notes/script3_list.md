# Python Lists: Complete Guide & Cheat Sheet

---

## 1. What is a List?

A **List** is a built-in Python data structure used to store an ordered collection of items in a single variable.

* Lists are defined using square brackets `[]` or the `list()` constructor.
* Lists can contain elements of any data type, including primitive types and nested data structures.

```python
# List of integers
numbers = [10, 20, 30, 40, 50]

# List containing multiple data types (Heterogeneous)
mixed_list = ["Indranil", 28, 7.5, True, None]
```

---

## 2. Core Properties of Lists

| Property | Description |
| :--- | :--- |
| **Ordered** | Elements preserve the exact sequence in which they were added. |
| **Mutable** | Values can be modified, appended, or removed without changing identity. |
| **Indexed** | Elements are accessed via $0$-based positive or negative indices. |
| **Allows Duplicates** | Identical elements can occur multiple times. |
| **Heterogeneous** | Can contain arbitrary mixes of types (integers, strings, objects). |
| **Dynamic Size** | Automatically grows and shrinks as elements are added or deleted. |
| **Iterable** | Can be traversed sequentially using a loop (`for x in my_list:`). |
| **Sequence Type** | Supports indexing, slicing, concatenation, and `len()`. |
| **Nesting** | Can contain multidimensional lists (matrices) and other containers. |

---

## 3. Creating Lists

### 3.1 Basic Declaration

```python
# Empty lists
list1 = []
list2 = list()

print(list1)  # []
print(list2)  # []
print(len(list1))  # 0
```

### 3.2 Converting Iterables via `list()`

```python
# Convert a string
chars = list("hello")
print(chars)  # ['h', 'e', 'l', 'l', 'o']

# Convert a tuple
nums = list((10, 20, 30))
print(nums)  # [10, 20, 30]
```

---

## 4. Indexing & Slicing

### 4.1 Indexing

Python lists support both forward ($0$-indexed) and reverse (negative) indexing.

```
 Index (Pos):   0       1        2      3     4     5
 Values:     ["muskan", "rohit", "rahul",  50,   20,   10]
 Index (Neg):  -6      -5       -4     -3    -2    -1
```

```python
data = ["muskan", "rohit", "rahul", 50, 20, 10]

print(data[0])   # muskan
print(data[5])   # 10
print(data[-1])  # 10
print(data[-6])  # muskan
```

### 4.2 Slicing Syntax: `list[start : stop : step]`

* `start`: Included (defaults to `0`)
* `stop`: Excluded (defaults to `len(list)`)
* `step`: Step interval (defaults to `1`)

```python
nums = [10, 20, 30, 40, 50]

print(nums[1:4])   # [20, 30, 40]  (indices 1, 2, 3)
print(nums[:3])    # [10, 20, 30]  (start to index 2)
print(nums[2:])    # [30, 40, 50]  (index 2 to end)
print(nums[::2])   # [10, 30, 50]  (every 2nd element)
print(nums[::-1])  # [50, 40, 30, 20, 10] (reversed copy)
```

---

## 5. Modifying & Updating Lists

Lists are **mutable**, allowing in-place updates.

```python
data = ["muskan", "rohit", "rahul", 50, 20, 10]
data[1] = "indra"

print(data)  # ['muskan', 'indra', 'rahul', 50, 20, 10]
```

---

## 6. Adding Elements

### 6.1 `append(value)`
Appends a single item to the end of the list.

```python
nums = [10, 20, 30]
nums.append(40)
print(nums)  # [10, 20, 30, 40]

# Note: Appending an iterable inserts it as a single nested element
nums.append([50, 60])
print(nums)  # [10, 20, 30, 40, [50, 60]]
```

### 6.2 `insert(index, value)`
Inserts an element at a specified index, shifting existing items to the right.

```python
nums = [10, 20, 30]
nums.insert(1, 15)
print(nums)  # [10, 15, 20, 30]
```

### 6.3 `extend(iterable)`
Unpacks an iterable and appends each element individually.

```python
nums = [10, 20, 30]
nums.extend([40, 50, 60])
print(nums)  # [10, 20, 30, 40, 50, 60]
```

---

## 7. Removing Elements

### 7.1 `remove(value)`
Removes the **first occurrence** of a specified value. Returns `None`. Raises `ValueError` if the value is not present.

```python
nums = [10, 20, 10, 30]
nums.remove(10)
print(nums)  # [20, 10, 30]
```

### 7.2 `pop([index])`
Removes and **returns** the element at the given index. If no index is specified, removes and returns the **last element**.

```python
nums = [10, 20, 30, 40]

last = nums.pop()
print(last)  # 40
print(nums)  # [10, 20, 30]

item = nums.pop(1)
print(item)  # 20
print(nums)  # [10, 30]
```

### 7.3 `clear()`
Removes all elements, leaving the list empty.

```python
nums = [10, 20, 30]
nums.clear()
print(nums)  # []
```

### 7.4 `del` Statement
A Python keyword (not a method) to delete items, slices, or entire references.

```python
nums = [10, 20, 30, 40, 50]

# Delete single item
del nums[2]
print(nums)  # [10, 20, 40, 50]

# Delete a slice
del nums[1:3]
print(nums)  # [10, 50]
```

---

## 8. Searching & Membership

```python
nums = [10, 20, 10, 30, 10]

# Membership testing
print(30 in nums)      # True
print(100 not in nums)  # True

# Counting occurrences
print(nums.count(10))  # 3
print(nums.count(50))  # 0

# Finding index of first match (raises ValueError if absent)
print(nums.index(10))  # 0
print(nums.index(30))  # 3
```

---

## 9. Sorting & Reversing

### 9.1 Sorting

| Approach | Mutates Original? | Returns |
| :--- | :--- | :--- |
| `list.sort(reverse=False)` | **Yes** (in-place) | `None` |
| `sorted(iterable, reverse=False)` | **No** (leaves source unchanged) | New sorted `list` |

```python
data = [100, 20, 10, 50]

# Built-in sorted()
new_data = sorted(data)
print(new_data)  # [10, 20, 50, 100]
print(data)      # [100, 20, 10, 50]

# Method .sort()
data.sort()
print(data)      # [10, 20, 50, 100]

# Descending order
data.sort(reverse=True)
print(data)      # [100, 50, 20, 10]
```

### 9.2 Reversing

```python
nums = [1, 2, 3, 4]

# 1. In-place reversal
nums.reverse()
print(nums)  # [4, 3, 2, 1]

# 2. Slicing (new list)
rev_slice = nums[::-1]
print(rev_slice)  # [1, 2, 3, 4]

# 3. reversed() iterator
rev_iter = reversed(nums)
print(list(rev_iter))  # [1, 2, 3, 4]
```

---

## 10. List Operators

```python
a = [1, 2, 3]
b = [4, 5, 6]

# Concatenation (+)
combined = a + b
print(combined)  # [1, 2, 3, 4, 5, 6]

# Repetition (*)
repeated = a * 2
print(repeated)  # [1, 2, 3, 1, 2, 3]
```

---

## 11. Nested Lists (Matrices)

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])     # [1, 2, 3]
print(matrix[0][1])  # 2
print(matrix[2][2])  # 9
```

---

## 12. Aliasing vs. Shallow Copying

### 12.1 Reference Assignment (Aliasing)
Assigning via `=` copies the memory address, pointing to the identical list object.

```python
list1 = [10, 20, 30]
list2 = list1

list2[0] = 999
print(list1)  # [999, 20, 30] -> mutated!
```

### 12.2 Shallow Copy Methods
Creates an independent list container.

```python
list1 = [10, 20, 30]

# Method 1: .copy()
c1 = list1.copy()

# Method 2: full slice
c2 = list1[:]

# Method 3: constructor
c3 = list(list1)

c1[0] = 999
print(list1)  # [10, 20, 30] -> unaffected
```

---

## 13. Summary Quick Reference

| Method / Operator | Action | Returns | In-Place? |
| :--- | :--- | :--- | :--- |
| `list.append(x)` | Adds `x` to the end | `None` | Yes |
| `list.insert(i, x)` | Inserts `x` at index `i` | `None` | Yes |
| `list.extend(iterable)` | Appends items from iterable | `None` | Yes |
| `list.remove(x)` | Removes first instance of `x` | `None` | Yes |
| `list.pop([i])` | Removes and returns item at `i` (default last) | Element | Yes |
| `list.clear()` | Removes all elements | `None` | Yes |
| `del list[i]` | Deletes item or slice at index `i` | `None` | Yes |
| `list.index(x)` | Returns index of first occurrence of `x` | `int` | No |
| `list.count(x)` | Returns total count of `x` | `int` | No |
| `list.sort()` | Sorts items in ascending order | `None` | Yes |
| `sorted(list)` | Produces a sorted duplicate | New `list` | No |
| `list.reverse()` | Reverses items in-place | `None` | Yes |
| `list[::-1]` | Slices into a reversed copy | New `list` | No |
| `list.copy()` | Produces a shallow copy | New `list` | No |