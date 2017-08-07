# Week 2 Notes

### Approximate Solution Algorithm
 - A "good enough" solution.
 - Start with a guess and increment by a small value.
 - Establish an epsilon (how close your guess should be to the number).
 - Your epsilon should be greater than your increment.

```python
cube = int(input("Enter a number: "))
epsilon = 0.01
increment = 0.001
guess = 0
num_guesses = 0

while abs(guess ** 3 - cube) >= epsilon and guess <= cube:
    guess = guess + increment
    num_guesses = num_guesses + 1

print("Number of guesses: " + str(num_guesses))

print(str(guess) + " is close enough to the cube root of " + str(cube))
```

### Bisection Search
 - From what we know, the square root of x lies between 1 and x.
 - Rather than starting at 1, we can pick a number in the middle of the range and use that as a guess.
 - If the guess is not close enough, is it too big or too small?.

```python
x = int(input("Enter a number: "))
epsilon = 0.01
num_guesses = 0
low = 1.0
high = x
guess = (high + low) / 2.0

while abs(guess ** 2 - x) >= epsilon:
    print("low = " + str(low) + " high = " + str(high) + " guess = " + str(guess))
    num_guesses = num_guesses + 1
    if guess ** 2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0

print("Number of guesses: " + str(num_guesses))
print(str(guess) + " is close to square root of " + str(x))
```

### Floats
 - Floats approximate real numbers, but useful to understand how.
 - Decimal Number: 302 = (3 x 10^2) + (0 x 10^1) + (2 x 10^0).
 - Binary Number: 10011 = (1 x 2^4) + (0 x 2^3) + (0 x 2^2) + (1 x 2^1) + (1 x 2^0).
 - Computers represent numbers in binary.

### Newton-Raphson Algorithm
 - General approximation algorithm to find roots of a polynomial in one variable.

```python
n = 24.0
epsilon = 0.01
guess = n / 2.0
num_guesses = 0

while abs((guess * guess) - n) >= epsilon:
    num_guesses = num_guesses + 1
    guess = guess - (((guess ** 2) - n) / (2 * guess))

print("Number of guesses: " + str(num_guesses))
print("Square root of " + str(n) + " is approximately " + str(guess))
```

### Decomposition
 - **Decomposition:** Break problem into different self-contained pieces.
 - Divide code into modules:
   - are self-contained
   - used to break up code
   - inteded to be reusable
   - keep code organized
   - keep code coherent
 - Code can be used many times, but only has to be debugged once.

### Abstraction
 - **Abstraction:** Suppress details of method to compute something from use of that computation.
   - Cannot see details
   - Do not need to see details
   - Do not want to see details
   - Hide tedious coding details

### Functions
 - **Function:** Reusable piece/chunk of code.
   - Has a name
   - Has parameters
   - Has a docstring
   - Has a body
 - Functions are not run in a program until they are called or invoked.
 - If you don't include a return statement, Python will return "None".
 - Functions can take other functions as arguments.

### Variable Scope
 - Formal parameter gets bound to the value of actual parameter when function is called.
 - New scope created when inside a function.
 - Scope is the mapping of names to objects.
 - Inside a function, you can access a variable defined outside the function.
 - Inside a function, you cannot modify a variable defined outside the function.

### Return vs Print
 - Return
   - Only has meaning inside a function.
   - Only one return can be executed in a function.
   - Code inside function but after return statement is not executed.
   - Has a value associated with it, given to function caller.
 - Print
   - Able to be used outside functions.
   - Can execute many print statements inside a function.
   - Code inside function can be executed after a print statement.
   - Has a value associated with it, outputted to the console.

### Specifications
 - A contract between the implementer of a function and the clients who will use it.
 - **Assumptions:** Conditions that must be met by the function; typically constraints on values of parameters.
 - **Guarantees:** Conditions that must be met by a function, providing it has been called in the manner consistent with its assumptions.
 - Label you functions with a docstring or comment to explain the specifications of a function.

### Recursion
 - A programming technique where a function calls itself.
 - A way to design solutions to problems by breaking them up into reusable pieces.
 - In programming, the goal is not to have infinite recursion:
   - Must have 1 or more base cases that are easy to solve
   - Must solve the same problem on some other input with the goal of simplifying the larger problem input. 
 - Each recursive call to a function creates its own scope.
 - Binding of variables in a scope is not changed by a recursive call.
 - Flow of control passes back to previous scope once function call returns value.
 - **Recursive Step:** Think how to reduce the problem to a smaller version of the same problem.
 - **Base Case:** Keep reducing problem until you reach a simple case that can be solved directly.

```python
def multiply(a, b):
    if b == 1:
        return a
    else:
        return a + multiply(a, b - 1)
```

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n)
```

```python
def exponent(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * exponent(base, exp - 1)
```

```python
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
```

### Iterative Algorithms
 - Looping constructs lead to iterative algorithms.
 - Can capture computation in a set of state variables that update on each iteration through the loop.

```python
def multiply(a, b):
  result = 0
  for i in range(b):
      result += a
  return result
```

```python
def factorial(num):
    result = 1
    for i in range(num):
        result *=   i + 1
    return result
```

```python
def exponent(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        result = base
        for i in range(exp - 1):
            result = result * base
    return result
```

```python
def gcd(a, b):
    if a > b:
        result = b
    else:
        result = a
    while a % result != 0 or b % result != 0:
        divisor -= 1
    return result
```

### Iterative vs Recursive
 - Recursion may be simpler and more intuitive.
 - Recursion may be efficient from a programmer POV.
 - Recursion my be inefficient from a computer POV.

### Mathematical Induction
 - To prove a statement indexed on integers is true for all values of n:
   - Prove it is truen when n is smallest value (e.g., n == 0 or n == 1)
   - Then if one can prove it is true for an arbitrary value of n, one can show that it must be true for n + 1

### Towers of Hanoi Problem
 - 3 tall spikes
 - Stack of 64 different sized discs on 1 spike
 - Need to move stack to 2nd spike (at which point the universe ends)
 - Can only move 1 disc at a time, and a larger disc can never cover a smaller disc

```python
# print an individual move from the "from" stack to the "to" stack
def print_move(frm, to):
    print("Move from " + str(frm) + " to " + str(to))

def towers(n, frm, to, spare):
    # if a stack of size 1, print_move
    if n == 1:
        print_move(frm, to)
    else:
        # move a smaller stack from the "from" to the "spare" stack
        towers(n - 1, frm, spare, to)
        # move from the "from" stack to the "to" stack
        towers(1, frm, to, spare)
        # move a smaller stack from the "spare" to the "to" stack
        towers(n - 1, spare, to, frm)

towers(64, "S1", "S2", "S3")
```

### Fibonacci Numbers
 - Newborn pair of rabbits (1 female, 1 male) are put in a pen
 - Rabbits mate at age 1 month
 - Rabbits have a 1 month gestation period
 - Female rabbits always produce 1 pair (1 female, 1 male)
 - Rabbits never die

| Month | Females |
| ----- | ------- |
| 0     | 1       |
| 1     | 1       |
| 2     | 2       |
| 3     | 3       |
| 4     | 5       |
| 5     | 8       |
| 6     | 13      |

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

| fibonacci(n) | return |
| ------------ | ------ |
| fibonacci(0) | 1      |
| fibonacci(1) | 1      |
| fibonacci(2) | 2      |
| fibonacci(3) | 3      |
| fibonacci(4) | 5      |
| fibonacci(5) | 8      |
| fibonacci(6) | 13     |

### Recursion on Non-numerics
 - How to check if a string of characters is a palindrome (reads the same forwards and backwards)
 - "Able was I, ere I saw Elba" - Napoleon
 - "Are we not drawn onward, we few, drawn onward to new era" - Anne Michaels

```python
def palindrome(s):
    # Convert the string to just characters, by stripping out punctuation and lowering case
    def just_chars(s):
        s = s.lower()
        answer = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                answer = answer + c
        return answer

    def is_pal(s):
        # Base Case: a string of 0 or 1 is a palindrome
        if len(s) <= 1:
            return True
        # Recursive Case: if first character matches the last character, then is a palindrome if middle section is a palindrome
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])
```

### Divide and Conquer Algorithm
 - Solve a hard problem by breaking it into a set of sub-problems.
 - Sub-problems are easier to solve than the original.
 - Solutions of the sub-problems can be combined to solve the original.

### Modules and Files
 - A module is a Python file containing a collection of Python definitions and statements.
 - Python has an operating system independent way to access files using a file handle.
