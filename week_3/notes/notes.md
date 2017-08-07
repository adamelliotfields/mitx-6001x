# Week 3 Notes

### Tuples
 - Tuples are an ordered sequence of elements.
 - Can be heterogeneous.
 - Are immutable (cannot be changed).
 - Represented by parens.
 - Can be indexed, concatenated, and sliced like a string. 
 - You must include a comma, even if the tuple only has one element, otherwise Python will ignore the parens.
 - Tuples can be used to swap variable values or return multiple values from a function:

```python
''' Invalid '''
x = y
y = x

''' Valid '''
(x, y) = (y, x)
```

```python
def quotient_remainder(x, y)
    q = x / y
    r = x % y
    return (q, r)
```

### Manipulating Tuples
 - Like strings, tuples can be iterated over:

```python
def get_data(tuple):
    nums = ()
    words = ()
    for t in tuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)
```

### Lists
 - Lists are an ordered sequence of information, accessible by index.
 - A list is denoted by square brackets.
 - Lists can be heterogeneous. 
 - List are mutable (can be changed).
 - Can be indexed, concatenated, and sliced like a string.
 - Lists are iterable.
 - Lists can also include other lists. 

```python
total = 0
for i in range(len(L)):
    total += L[i]
return total

total = 0
for i in L:
    total += i
return total
```

### List Operations
 - Add elements to the end of the list with the `.append()` function (this mutates the list).
 - Lists are Python objects, with methods associated with them, and dot notation accesses those methods.
 - You can extend a list with the `.extend()` function and passing in another list. 
 - You can insert an element into a specific index with the `.insert()` function.
 - You can sort a list with the `.sort()` function (this mutates the list); alternatively, you can use the `sorted()` function to return the sorted version of the list (does not mutate the original list).
 - You can delete a specific index from a list with the `del()` function and passing in a list and index.
 - You can remove an element with the `.remove()` function and passing in a specific element (not the index). If the element exists in the list, it will be removed; if it appears multiple times, only the first element will be removed; if it doesn't exist, it will return an error.
 - You can also remove an element and simultaneously return the element with the `.pop()` function.
 - You can convert a string into a list with the `list()` function. 
 - You can split a string into a list at a specific character with the `.split()` function 
 - You can join a list of characters into a string with the `''.join()` function.
 - `range()` is a special procedure that returns a tuple:

```python
for i in range(5)
    pass

for i in (0,1,2,3,4):
    pass
```

### Lists in Memory
 - Lists are mutable. 
 - Lists behave differently than immutable types.
 - Lists are an object in memory.
 - Variable name points to object.
 - Any variable pointing to that object is affected.
 - Keep in mind side effects when working with lists. 
 - Avoid mutating a list when iterating over it.

### Aliases and Clones
 - When assigning a variable name to an existing variable, you are giving that variable an alias.
 - If you change the value of the original variable, the alias will change as well.
 - When cloning a list, you make a copy of it at that point in time; the clone will not mutate if you change the original list. 

### Functions as Objects
 - Functions are first class objects:
   - Have types
   - Can be elements of data structures like lists
   - Can appear in expressions:
     - As part of an assignment statement
     - As an argument to a function
- It is particularly useful to use functions as arguments when coupled with lists
  - AKA higher order programming

```python
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i]):
            L[i] = f(L[i])

L = [1, -2, 3.4]

applyToEach(L, abs) # [1, 2, 3.4]
applyToEach(L, int) # [1, 2, 3]
applyToEach(L, fact) # [1, 2, 6]
applyToEach(L, fib) # [1, 2, 13]
```

```python
def applyFuncs(L, x):
    for f in L:
        print(f(x))

L = [abs, int, fact, fib]

applyFuncs(L, 4)
# 4
# 4
# 24
# 5
```

### Generalizations of HOPs
 - **HOP:** Higher Order Procedure.
 - `map` is a HOP.

```python
for i in map(abs, [1, -2, 3, -4]
    print(i)

# [1, 2, 3, 4]
```

```python
L1 = [1, 28, 36]
L2 = [2, 57, 9]

for i in map(min, L1, L2):
    print(i)

# [1, 28, 9]
```

### Common Operations of Scalar Data Types

```python
seq[i] # ith element of sequence
len(seq) # length of sequence
seq1 + seq2 # concatenation of sequences
n * seq # sequence that repeats seq n times
seq[start:end] # slice of a sequence
e in seq # True if e contained in sequence
e not in seq # True if e not contained in sequence
for e in seq # iterates over elements of sequence
```

### Properties of Scalar Data Types

| Type   | Elements   | Examples                       | Mutable |
|--------|------------|--------------------------------|---------|
| string | characters | `''`, `'a'`, `'abc'`           | No      |
| tuple  | any type   | `()`, `(3,)`, `('abc', 4)`     | No      |
| range  | integers   | `range(10)`, `range(1, 10, 2)` | No      |
| list   | any type   | `[]`, `[3]`, `['abc', 4]`      | Yes     |

### Dictionaries
 - Index the item of interest directly (not always an integer).
 - Nice to use one data structure, no separate lists.
 - Stores key-value pairs of data.

| Keys  | Values  |
|-------|---------|
| Key 1 | Value 1 |
| Key 2 | Value 2 |
| Key 3 | Value 3 |

### Dictionary Lookup
 - Similar to indexing a list.
 - Looks up the key and returns the value associated with that key.
 - If the key isn't found, returns an error.

### Dictionary Operations
 - Dictionaries are mutable, you can add and delete entries. 
 - You can test if a key is in the dictionary.
 - You can get an iterable that acts like a tuple of all keys using the `.keys()` function.
 - You can get an iterable that acts like a tuple of all values using the `.values()` function.

### Fibonacci and Dictionaries
 - Do a lookup first in case already calculated the value.
 - Modify dictionary as progress through function calls.

```python
def fibonacci(n):
    d = {1:2, 2:2}
    if n in d:
        return d[n]
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        d[n] = result
        return result
```

### Global Variables
 - Can be dangerous to use:
   - Breaks the scoping of variables by function call.
   - Allows for side effects of changing variable values in ways that affect other computation.
 - Can be convenient when we want to keep track of information inside a function.
