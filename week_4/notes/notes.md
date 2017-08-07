# Week 4 Notes

### Defensive Programming
 - Write specifications for functions.
 - Modularize programs.
 - Check conditions on inputs and outputs (assertions).
 - Set yourself up for easy testing and debugging.
   - Break program into modules that can be tested individually.
   - Document constraints on modules.
   - Document assertions behind code design.

### Testing/Validation
 - Compare input/output pairs to specification.
 - Think about how to break the program.

### Debugging
 - Study events leading up to the error.
 - Think about how to fix the program.

### Classes of Tests
 - Unit testing
   - Validate each piece of the program
   - Test each function separately
 - Regression testing
   - Test for bugs as you find them in a function
   - Catch reintroduced errors that were previously fixed
 - Integration testing
   - Does the overall program work?

### Testing Approaches
 - Intuition about natural boundaries to the problem.
 - If no natural partitions exist, might do random testing.
 - Black box testing explores all paths through specifications in the code.
 - Glass box testing explores all paths through the code itself.

### Black Box Testing
 - Designed without looking at the code.
 - Can be done by somebody other than the implementer. 
 - Testing can be reused if the implementation changes.

### Glass Box Testing
 - Uses code directly to guide the design of test cases.
 - Called path-complete if every potential path through the code is tested at least once.
 - Guidelines are to look at all branches and loops (and look for paths out of loops).

### Runtime Bugs
 - Overt bugs have an obvious manifestation: crashes or infinite loops.
 - Covert bugs have no obvious manifestation: code can return a value, but may be incorrect.
 - Persistent bugs occur every time.
 - Intermittent bugs only occur occassionally.

### Debugging Skills
 - Treat as a search problem: look for an explaination for incorrect behavior:
   - Study available data - both correct test cases and incorrect ones.
   - For a hypothesis consistent with the data.
   - Design and run a repeatable experiment with potential to refute hypothesis.
   - Keep record of experiments performed.

### Exceptions and Assertions
 - Exceptions happen when procedure execution hits an unexpected condition; an exception to what was expected.
 - Common error types:
   - `SyntaxError` - Python cannot parse the program.
   - `NameError` - Local or global name not found.
   - `AttributeError` - Attribute reference fails.
   - `TypeError` - Operand doesn't have correct type.
   - `ValueError` - Operand value is illegal.
   - `IOError` - IO system reports malfunction (e.g., file not found).

### Dealing with Exceptions
 - Python code can provide handlers for exceptions.
 - Exceptions raised by any statement in the body of `try` are handled by the `except` statement and execution continues after the body of the `except` statement.

```python
try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print(a/b)
    print("Okay")
except:
    print("Bug in user input.")

print("Outside")
```

### Handling Specific Exceptions
 - Have separate `except` clauses to deal with a particular type of exception.

```python
try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a / b = ", a/b)
    print("a + b = ", a+b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero.")
except:
    print("Something went wrong.")
```

### Other Exceptions
 - `else` - body of this is executed when execution of associated `try` completes with no exceptions.
 - `finally` - body of this is always executed after `try`, `else`, and `except`.

### Exceptions as Control Flow
 - Don't return special values when an error occured and then check whether error value was returned.
 - Instead, raise an exception when unable to produce a result consistent with function's specification.

```python
def get_ratios(L1, L2):
    '''Assumes: L1 and L2 are lists of equal length of numbers.
       Returns: a list containing L1[i]/L2[i]'''
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float("NaN"))
        except:
            raise ValueError("get_ratios called with bad argument")
    return ratios
```

### Assertions
 - Want to be sure that assumptions on state of computation are as expected.
 - Use an assert statement to raise an `AssertionError` exception if assumptions are not met.
 - An example of good defensive programming.

```python
def avg(grades):
    assert not len(grades) == 0, "no grades data"
    return sum(grades)/len(grades)
```

### Where to Use Assertions
 - Goal is to spot bugs as soon as introduced and make clear where they happened.
 - Use as a supplement to testing.
 - Raise exceptions if user supplies bad data input.
 - Check types of arguments or values.
 - Check that invariants on data structures are met.
 - Check constraints on return values.
 - Check for violations of constraints on procedure (e.g., not duplicates in a list).
