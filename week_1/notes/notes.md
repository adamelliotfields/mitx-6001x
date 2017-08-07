# Week 1 Notes

### Goals
 - Represent knowledge with data structures.
 - Iteration and recursion as computational metaphors.
 - Abstraction of procedures and data types.
 - Organize and modularize systems using object classes and methods.
 - Different classes of algorithms and complexity of algorithms.
 - The syntax and semantics of the Python programming language.
 - Create “recipes” for solving a problem in a form that the computer can use.
 - Leverage a suite of methods to solve complex problems.

### Computational Thinking
 - The thought processes involved in formulating a problem and expressing its solutions in such a way that a computer can carry out.
 - A mode of thinking in which everything can be viewed formulaically.

### Computer Science
 - The study of automating algorithmic processes that scale.
 - A Computer Scientist specializes in the theory of computation and the design of computational systems.

### Declarative vs Imperative Knowledge
 - **Declarative:** A statement of fact (e.g., CSS, SQL).
 - **Imperative:** A set of rules or conditions (e.g., Python).

### Heron’s Method
 1. Start with a guess
 2. If g * g is close enough to x, stop
 3. Otherwise, make a new guess by averaging g and x divided by g
 4. Using the new g, repeat the process until close enough

### What Does a Computer Do?
 - Perform calculations (CPU) and remember things (RAM, storage).
 - Computers have limitations.
 - There are 10^120 possible chess moves (Shannon’s Number).
 - There are 10^80 atoms in the observable universe.
 - Therefore, it is impossible to store all of the possible chess moves on a computer.
 - Some problems are fundamentally impossible to computer (Turing Halting Problem).
 - Computers can be fixed program (a hand-held calculator) or stored program (Windows, UNIX-based).

### Basic Computer Architecture
 - **Storage:** Could be used to save programs or data
 - **Arithmetic Logic Unit:** A digital circuit used to perform arithmetic and logic operations
 - **Input:** A way to load things into the computer
 - **Output:** A way to print things out
 - **Control Unit:** Tells the computer’s storage, ALU, and I/O how to respond to a program’s instructions

### What is an Algorithm?
 - A sequence of steps.
 - A flow of control process that specifies when each step is to be executed.
 - A means of determining when to stop.
 - An algorithm is a conceptual idea; a program is a concrete instantiation of an algorithm.

### Interpreter vs Compiler
 - An interpreter is a program that directly executes instructions written in a programming or scripting language (Python Shell).
 - A compiler is a program that translates source code (written in a programming language) into object code (binary).
 - The Java Compiler (javac) compiles Java to bytecode which can be run on the Java Virtual Machine (JVM).

### Programming Language
 - **Turing Completeness:** Anything that’s computable in one programming language is computable in another.
 - A programming language is a set of primitive operations.
 - Basic primitive constructs are booleans, numbers, strings, arithmetic, and comparisons.
 - An expression is a complex set of primitives in a programming language.
 - Any legal expression in a programming language has a value.
 - Syntax is the legal combination of expressions.
 - Syntactic errors are common and easily caught.
 - Semantics is the meaning of a syntactically correct series of characters and symbols.
 - Static Semantics refers to the meaning of a particular string.
 - Semantic errors can cause unpredictable behavior in a program (e.g., infinite loop).
 - In a programming language, any expression that is syntactically and semantically correct will only have one meaning.
 - Abstraction is a means of taking a complex expression and treating it as a primitive.

### What is a Program?
 - A program is a sequence of definitions and commands:
   - Definitions are evaluated (variables)
   - Commands are executed (functions)
 - Commands can be typed directly into a shell (Python, Node), or stored in a file.

### Objects
 - Programs manipulate data objects.
 - Objects have a type (e.g., string vs integer) that defines what programs can do to them.
 - Objects can be either scalar (cannot be subdivided) or non-scalar.

### Scalar Objects

```python
int # represents integers (2)
float # represents real numbers (2.00)
bool # represents boolean values (True and False)
NoneType # has only one value (None)
type() # is a function that shows the type of an object
```

### Type Conversion

```python
float(3) # converts integer 3 to float 3.0
int(3.9) # truncates float 3.9 to integer 3
str(3) # converts integer 3 to string "3"
abs(-3) # converts negative integer -3 to positive integer 3
```

### Expressions
 - Form expressions by combining objects and operators.
 - An expression has a value, which has a type.
 - Syntax for a simple expression: Object + Operator + Object.

### Simple Operations
 - Python uses the PEMDAS order of operations.
 - Parentheses can be used to tell Python which operations to do first.

### Variables
 - Equal sign (=) is an assignment of a value to a variable name.
 - The value is stored in computer memory.
 - Left hand side is the variable, right hand side is the value.
 - Values can be retrieved by invoking the name of the variable.
 - Variables can be assigned a new value.
 - Names should be descriptive and meaningful.
 - Keywords (e.g., int or float) cannot be used as variables.

```python
pi = 3.14159
pi_approx = 22/7
```

### Abstracting Expressions
 - By assigning expressions to variables, you can reuse names instead of values in your code.
 - This makes your code easier to read/change later.

```python
pi = 3.14159
radius = 2.2
area = pi * (radius ** 2)
```

### Comparison Operators on Integers and Floats
 - Comparisons return either True or False

```python
i > j # i is greater than j
i >= j # i is greater than or equal to j
i < j # i is less than j
i <= j # i is less than or equal to j
i == j # i is equal to j
i != j # i is not equal to j
```

### Logical Operators on Booleans

```python
not a # True if a is False; False if a is True
a and b # True if both are True
a or b # True if either or both are True
```

### Branching Programs
 - The simplest branching statement is a conditional.
 - Start with a test (an expression that evaluates to True or False).
 - Add a block of code to run if the test is True.
 - Optionally, add a block of code to run if the test is False.

```python
x = 3
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Compound Booleans

```python
if x < y and x < z:
    print("x is least")
elif y < z:
    print("y is least")
else:
    print("z is least")
```

### Strings
 - A sequence of letters, special characters, spaces, or digits.
 - Enclose in quotation marks or single quotes.
 - Strings can be concatenated.

```python
name = "Adam"
greet = "Hello"
greeting = greet + " " + name
```

### String Operations

```python
"string" + "string" # concatenation
3 * "string" # successive concatenation
len("string") # length
"string"[0] # indexing
"string"[1:4] # slicing
```

### Input/Output

```python
name = input("What is your name?: ") # input
print("Hello " + name) # output
```

### Integrated Development Environment
 - Text Editor
 - Shell
 - Debugger

### Control Flow
 - Simple branching programs make choices, but the path is still linear.
 - Branching structures (conditionals) let us jump to different pieces of code, based on a test, in constant time.
 - Sometimes you may want to reuse parts of code an indeterminate number of times.
 - Looping structures (for, while) let us repeat pieces of code until a condition is satisfied.

### While Loops
 - While a condition is True, the while loop will repeat the code block.
 - Use while loops when you do not know the number of iterations.
 - You may not be able to rewrite a while loop using a for loop.
 - Can end early via the break statement.

```python
n = 0
while n < 10:
    print(n)
    n = n + 2
```

### For Loops
 - Each time through the loop, the variable increments by 1 until it reaches the end of the range.
 - Range can have a start, stop, and step.
 - Use for loops when you know the number of iterations.
 - You can rewrite a for loop using a while loop.
 - Can end early via the break statement.

```python
for n in range(0, 10, 2):
    print(n)
```

### Classes of Algorithms
 - Iterative algorithms allow us to do more complex things than simple algorithms.
 - We can repeat a sequence of steps multiple times based on a decision.

### Guess and Check Algorithm
 - Heron's Method is an example of a guess and check algorithm.
 - You are able to guess a value for a solution.
 - You are able to check if the solution is correct.
 - You keep guessing until you find the solution or have guessed all possible values.
 - Guess and check can work on problems with a finite number of possibilities.
 - This process is known as "exhaustive enumeration".
 - Exhaustive enumeration is a good way to generate guesses in an organized manner.

```python
cube = 8
for i in range(cube + 1):
    if i ** 3 >= cube:
        break
if i ** 3 != cube:
    print(cube + " is not a perfect cube")
else:
    print("The cube root of " + str(cube) + " is " + str(i))
```
