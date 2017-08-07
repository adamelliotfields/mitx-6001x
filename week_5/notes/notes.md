# Week 5 Notes

### Standard Data Objects
 - Some object types built in to Python:
   - lists (e.g., `[1, 2, 3, 4]`)
   - tuples (e.g., `(1, 2, 3, 4)`)
   - strings (e.g., `"abcd"`)

### Objects
 - Every object has a type, an internal data representation, and a set of procedures to interact with them.
 - Each instance is particular type of object:
   - `1234` is an instance of `int`
   - `"abcd"` is an instance of `str`

### Object Oriented Programming
 - Everything in Python is an object and has a type.
 - Objects are a data abstraction that capture:
   - An internal representation through data attributes
   - An interface for interacting with objects through methods (procedures) that defines behaviors but hides implementation. 
   - The ability to create new instances of objects. 

### Advantages of OOP
 - Bundle data into packages together with procedures that work on them through well-defined interfaces.
 - Divide-and-conquer development:
   - Implement and test behavior of each class separately
   - Increase modularity reduces complexity
 - Classes make it easy to reuse code
   - Many Python modules define new classes
   - Each class has separate environment
   - Inheritance allows subclasses to redefine or extend a selected subset of a superclass' behavior.

### Define Your Own Types
 - Use the `class` keyword to define a new type.
 - Similar to `def`, indent code to indicate which statements are part of the class definition.

### What Are Attributes?
 - Data and procedures that belong to the class.
 - Think of data as other objects that make up the class.
 - Think of methods as functions that only work with the class.

### Create an Instance of a Class
 - Use a special method called `__init__()` to initialize some data attributes.
 - `__init__()`'s first argument is always `self`.
 - Data attributes of an instance are called instance variables.

### What is a Method?
 - A procedural attribute, like a function that works only with this class.
 - Python always passes the actual object as the first argument.
 - Convention is to use self as the name of the first argument of all methods.
 - The `.` (dot) operator is used to access any attribute.
