# Week 6 Notes

### Big Oh Notation
Big Oh notation `O()` measures an upper bound on the asymptotic growth, often called order of growth.

Big Oh is used to describe the worst case:
 - Worst case occurs often and is the bottleneck when a program runs
 - Express rate of growth of program relative to the input size
 - Evaluate algorithm not machine or implementation

### Complexity Classes Ordered Low to High
 - Constant:    `O(1)`
 - Logarithmic: `O(log n)`
 - Linear:      `O(n)`
 - Loglinear:   `O(n log n)`
 - Polynomial:  `O(n^c)`
 - Exponential: `O(c^n)`

### Analyzing Programs and Their Complexity
Combine complexity classes:
 - Analyze statements inside functions
 - Apply some rules, focus on dominant term

Law of Addition for O():
 - Used with sequential statements
 - `O(f(n)) + O(g(n)) = O(f(n) + g(n))`

Law of Multiplication for O():
 - Used with nested statements/loops
 - `O(f(n)) * O(g(n)) = O(f(n) * g(n))`

### Constant Complexity Algorithms
 - Complexity independent of inputs
 - Very few interesting algorithms in this class
 - Can have loops or recursive calls, but number of iterations is independant of size of input

### Logarithmic Complexity Algorithms
 - Complexity grows as log of size of one of its inputs
 - bisection search, binary search

### Linear Complexity Algorithms
 - Searching a list in sequence to see if an element is present
 - Add characters of a string assumed to be composed of decimal digits'
 - Complexity can depend on number of recursive calls

### Loglinear Complexity Algorithms
 - Many practical algorithms are loglinear
 - Very commonly used loglinear algorithm is merge sort

### Polynomial Complexity Algorithms
 - Most common polynomial algorithms are quadratic, i.e., complexity grows with square of size of input
 - Commonly occurs when we have nested loops or recursive function calls

### Exponential Complexity Algorithms
 - Recursive functions where more than one recursive call for each size of problem, i.e., Towers of Hanoi problem
 - Many important problems are inherently exponential

### Search Algorithms
 - Method for finding an item or group of items with specific properties within a collection of items
 - Collection could be implicit, i.e., find square root as a search problem
 - Collection could be explicit, i.e., is a record stored in a collection of data
 - **Linear Search:** brute force search, list does not have to be sorted
 - **Bisection Search:** list must be sorted

### Sorting Algorithms
 - **Bogo sort:**
   - AKA monkey sort, stupid sort, slow sort, permutation sort, shotgun sort
   - Throw a deck of cards in the air, pick them up off the ground, and see if they are sorted
 - **Bubble sort:**
   - Compare consecutive pairs of elements
   - Swap elements in pair such that smaller is first
   - When reaching end of the list, start over again
   - Stop when no more swaps have been made
 - **Selection sort:**
   - Extract minimum element, swap it with element at index 0
   - In remaining sublist, extract minimum element and swap with element at index 1
   - Keep the left portion of the list sorted
 - **Merge sort:**
   - If list is of length 0 or 1, already sorted
   - If last has more than one element, split into two lists and merge sorted sublists
