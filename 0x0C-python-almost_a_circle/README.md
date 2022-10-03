[](https://alx-intranet.hbtn.io/)

-   [](https://alx-intranet.hbtn.io/planning/me)

-   [](https://alx-intranet.hbtn.io/projects/current)

-   [](https://alx-intranet.hbtn.io/corrections/to_review)

-   [](https://alx-intranet.hbtn.io/dashboards/my_current_evaluation_quizzes)

* * * * *

-   [](https://alx-intranet.hbtn.io/dashboards/my_curriculums)

-   [](https://alx-intranet.hbtn.io/concepts)

-   [](https://alx-intranet.hbtn.io/dashboards/video_rooms)

-   [](https://alx-intranet.hbtn.io/servers)

-   [](https://alx-intranet.hbtn.io/user_containers/current)

* * * * *

-   [](https://alx-intranet.hbtn.io/users/peers)

-   [](https://alx-intranet.hbtn.io/dashboards/my_captain_log)

-   [](https://alx-students.slack.com)

    [](https://alx-intranet.hbtn.io/users/my_profile)

You just released the optional tasks of this project. Have fun!

0x0A. Python - Inheritance
==========================

PythonOOPInheritance

-   By: Guillaume
-   Weight: 1
-   Project over - took place from Sep 26, 2022 4:00 AM to Sep 27, 2022 4:00 AM
-   An auto review will be launched at the deadline

#### In a nutshell...

-   **Auto QA review:** 0.0/170 mandatory & 0.0/21 optional
-   **Altogether:**  **0.0%**
    -   Mandatory: 0.0%
    -   Optional: 0.0%
    -   Calculation:  0.0% + (0.0% * 0.0%)  == **0.0%**

Resources
---------

**Read or watch**:

-   [Inheritance](https://alx-intranet.hbtn.io/rltoken/ct-bhZHBxfE-aHYQoAcscQ "Inheritance")
-   [Multiple inheritance](https://alx-intranet.hbtn.io/rltoken/qq52YyYhDIbKBneA-u0PKw "Multiple inheritance")
-   [Inheritance in Python](https://alx-intranet.hbtn.io/rltoken/zQ6bnQUWn3e1B2-U3KaRyA "Inheritance in Python")
-   [Learn to Program 10 : Inheritance Magic Methods](https://alx-intranet.hbtn.io/rltoken/CFBGj9h1gP3eNLnEm2Ehhg "Learn to Program 10 : Inheritance Magic Methods")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/UJKcx5DE4cRGNq4Ayi-g9g "explain to anyone"), **without the help of Google**:

### General

-   Why Python programming is awesome
-   What is a superclass, baseclass or parentclass
-   What is a subclass
-   How to list all attributes and methods of a class or instance
-   When can an instance have new attributes
-   How to inherit class from another
-   How to define a class with multiple base classes
-   What is the default class every class inherit from
-   How to override a method or attribute inherited from the base class
-   Which attributes or methods are available by heritage to subclasses
-   What is the purpose of inheritance
-   What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

### Copyright - Plagiarism

-   You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
-   You will not be able to meet the objectives of this or any following project by copying and pasting someone else's work.
-   You are not allowed to publish any content of this project.
-   Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
------------

### Python Scripts

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the pycodestyle (version `2.8.*`)
-   All your files must be executable
-   The length of your files will be tested using `wc`

### Python Test Cases

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files should end with a new line
-   All your test files should be inside a folder `tests`
-   All your test files should be text files (extension: `.txt`)
-   All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)
-   We strongly encourage you to work together on test cases, so that you don't miss any edge case

### Documentation

-   Do not use the works `import` or `from` inside your comments, the checker will think you try to import some modules

### Quiz questions

**Great!** You've completed the quiz successfully! Keep going! (Show quiz)

Tasks
-----

### 0\. Lookup

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a function that returns the list of available attributes and methods of an object:

-   Prototype: `def lookup(obj):`
-   Returns a `list` object
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 0-main.py
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

guillaume@ubuntu:~/0x0A$ ./0-main.py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
guillaume@ubuntu:~/0x0A$

```

**No test cases needed**

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0A-python-inheritance`
-   File: `0-lookup.py`

### 1\. My list

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a class `MyList` that inherits from `list`:

-   Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
-   You can assume that all the elements of the list will be of type `int`
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 1-main.py
#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

guillaume@ubuntu:~/0x0A$ ./1-main.py
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
guillaume@ubuntu:~/0x0A$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0A-python-inheritance`
-   File: `1-my_list.py, tests/1-my_list.txt`

### 2\. Exact same object

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a function that returns `True` if the object is *exactly* an instance of the specified class ; otherwise `False`.

-   Prototype: `def is_same_class(obj, a_class):`
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 2-main.py
#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))

guillaume@ubuntu:~/0x0A$ ./2-main.py
1 is an instance of the class int
guillaume@ubuntu:~/0x0A$

```

**No test cases needed**

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0A-python-inheritance`
-   File: `2-is_same_class.py`

### 3\. Same class or inherit from

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.

-   Prototype: `def is_kind_of_class(obj, a_class):`
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 3-main.py
#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))

guillaume@ubuntu:~/0x0A$ ./3-main.py
1 comes from int
1 comes from object
guillaume@ubuntu:~/0x0A$

```

**No test cases needed**

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0A-python-inheritance`
-   File: `3-is_kind_of_class.py`

### 4\. Only sub class of

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.

-   Prototype: `def inherits_from(obj, a_class):`
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 4-main.py
#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

guillaume@ubuntu:~/0x0A$ ./4-main.py
True inherited from class int
True inherited from class object
guillaume@ubuntu:~/0x0A$

```

**No test cases needed**

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0A-python-inheritance`
-   File: `4-inherits_from.py`

### 5\. Geometry module

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write an empty class `BaseGeometry`.

-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 5-main.py
#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))

guillaume@ubuntu:~/0x0A$ ./5-main.py
<5-base_geometry.BaseGeometry object at 0x7f2050c69208>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
guillaume@ubuntu:~/0x0A$

```

**No test cases needed**

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0A-python-inheritance`
-   File: `5-base_geometry.py`

### 6\. Improve Geometry

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a class `BaseGeometry` (based on `5-base_geometry.py`).

-   Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 6-main.py
#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0A$ ./6-main.py
[Exception] area() is not implemented
guillaume@ubuntu:~/0x0A$

```

**No test cases needed**

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0A-python-inheritance`
-   File: `6-base_geometry.py`

### 7\. Integer validator

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a class `BaseGeometry` (based on `6-base_geometry.py`).

-   Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
-   Public instance method: `def integer_validator(self, name, value):` that validates `value`:
    -   you can assume `name` is always a string
    -   if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
    -   if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 7-main.py
#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0A$ ./7-main.py
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
guillaume@ubuntu:~/0x0A$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0A-python-inheritance`
-   File: `7-base_geometry.py, tests/7-base_geometry.txt`

### 8\. Rectangle

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).

-   Instantiation with `width` and `height`: `def __init__(self, width, height):`
    -   `width` and `height` must be private. No getter or setter
    -   `width` and `height` must be positive integers, validated by `integer_validator`

```
guillaume@ubuntu:~/0x0A$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0A$ ./8-main.py
<8-rectangle.Rectangle object at 0x7f6f488f7eb8>
['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
[AttributeError] 'Rectangle' object has no attribute 'width'
[TypeError] height must be an integer
guillaume@ubuntu:~/0x0A$

```

**No test cases needed**

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0A-python-inheritance`
-   File: `8-rectangle.py`

### 9\. Full rectangle

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)

-   Instantiation with `width` and `height`: `def __init__(self, width, height):`:
    -   `width` and `height` must be private. No getter or setter
    -   `width` and `height` must be positive integers validated by `integer_validator`
-   the `area()` method must be implemented
-   `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

```
guillaume@ubuntu:~/0x0A$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())

guillaume@ubuntu:~/0x0A$ ./9-main.py
[Rectangle] 3/5
15
guillaume@ubuntu:~/0x0A$

```

**No test cases needed**

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0A-python-inheritance`
-   File: `9-rectangle.py`

### 10\. Square #1

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):

-   Instantiation with `size`: `def __init__(self, size):`:
    -   `size` must be private. No getter or setter
    -   `size` must be a positive integer, validated by `integer_validator`
-   the `area()` method must be implemented

```
guillaume@ubuntu:~/0x0A$ cat 10-main.py
#!/usr/bin/python3
Square = __import__('10-square').Square

s = Square(13)

print(s)
print(s.area())

guillaume@ubuntu:~/0x0A$ ./10-main.py
[Rectangle] 13/13
169
guillaume@ubuntu:~/0x0A$

```

**No test cases needed**

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0A-python-inheritance`
-   File: `10-square.py`

### 11\. Square #2

mandatory

Score: 0.0% (Checks completed: 0.0%)

Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).

-   Instantiation with `size`: `def __init__(self, size):`:
    -   `size` must be private. No getter or setter
    -   `size` must be a positive integer, validated by `integer_validator`
-   the `area()` method must be implemented
-   `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`

```
guillaume@ubuntu:~/0x0A$ cat 11-main.py
#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())

guillaume@ubuntu:~/0x0A$ ./11-main.py
[Square] 13/13
169
guillaume@ubuntu:~/0x0A$

```

**No test cases needed**

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0A-python-inheritance`
-   File: `11-square.py`

### 12\. My integer

#advanced

Score: 0.0% (Checks completed: 0.0%)

Write a class `MyInt` that inherits from `int`:

-   `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 100-main.py
#!/usr/bin/python3
MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)

guillaume@ubuntu:~/0x0A$ ./100-main.py
3
False
True
guillaume@ubuntu:~/0x0A$

```

**No test cases needed**

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0A-python-inheritance`
-   File: `100-my_int.py`

### 13\. Can I?

#advanced

Score: 0.0% (Checks completed: 0.0%)

Write a function that adds a new attribute to an object if it's possible:

-   Raise a `TypeError` exception, with the message `can't add new attribute` if the object can't have new attribute
-   You are not allowed to use `try/except`
-   You are not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 101-main.py
#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)[](https://alx-intranet.hbtn.io/)

-   [](https://alx-intranet.hbtn.io/planning/me)

-   [](https://alx-intranet.hbtn.io/projects/current)

-   [](https://alx-intranet.hbtn.io/corrections/to_review)

-   [](https://alx-intranet.hbtn.io/dashboards/my_current_evaluation_quizzes)

* * * * *

-   [](https://alx-intranet.hbtn.io/dashboards/my_curriculums)

-   [](https://alx-intranet.hbtn.io/concepts)

-   [](https://alx-intranet.hbtn.io/dashboards/video_rooms)

-   [](https://alx-intranet.hbtn.io/servers)

-   [](https://alx-intranet.hbtn.io/user_containers/current)

* * * * *

-   [](https://alx-intranet.hbtn.io/users/peers)

-   [](https://alx-intranet.hbtn.io/dashboards/my_captain_log)

-   [](https://alx-students.slack.com)

    [](https://alx-intranet.hbtn.io/users/my_profile)

[

You have a captain's log due before 2022-10-02 (in 1 day)! Log it now!

](https://alx-intranet.hbtn.io/captain_logs/1053407/edit)

0x0C. Python - Almost a circle
==============================

PythonOOP

-   By: Guillaume
-   Weight: 1
-   Project will start Sep 29, 2022 4:00 AM, must end by Oct 4, 2022 4:00 AM
-   will be released at Oct 3, 2022 4:00 PM
-   **Manual QA review must be done** (request it when you are done with the project)
-   An auto review will be launched at the deadline

Background Context
------------------

The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

In this project, you will review everything about Python:

-   Import
-   Exceptions
-   Class
-   Private attribute
-   Getter/Setter
-   Class method
-   Static method
-   Inheritance
-   Unittest
-   Read/Write file

You will also learn about:

-   `args` and `kwargs`
-   Serialization/Deserialization
-   JSON

Resources
---------

**Read or watch**:

-   [args/kwargs](https://alx-intranet.hbtn.io/rltoken/7gc6UzxSL81HcuAwklUbuQ "args/kwargs")
-   [JSON encoder and decoder](https://alx-intranet.hbtn.io/rltoken/rGVU9mt57rVURGnjK6n4_Q "JSON encoder and decoder")
-   [unittest module](https://alx-intranet.hbtn.io/rltoken/soictNXCPE18ASL3INoeew "unittest module")
-   [Python test cheatsheet](https://alx-intranet.hbtn.io/rltoken/uI9iskBCcNo5pc7j9Vy86A "Python test cheatsheet")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/SBdRhGGBuqzWcwcuKyapSQ "explain to anyone"), **without the help of Google**:

### General

-   What is Unit testing and how to implement it in a large project
-   How to serialize and deserialize a Class
-   How to write and read a JSON file
-   What is `*args` and how to use it
-   What is `**kwargs` and how to use it
-   How to handle named arguments in a function

### Copyright - Plagiarism

-   You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
-   You will not be able to meet the objectives of this or any following project by copying and pasting someone else's work.
-   You are not allowed to publish any content of this project.
-   Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
------------

### Python Scripts

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the pycodestyle (version `2.8.*`)
-   All your files must be executable
-   The length of your files will be tested using `wc`
-   All your modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`
-   All your classes should be documented: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
-   All your functions (inside and outside a class) should be documented: `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
-   A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files should end with a new line
-   All your test files should be inside a folder `tests`
-   You have to use the [unittest module](https://alx-intranet.hbtn.io/rltoken/soictNXCPE18ASL3INoeew "unittest module")
-   All your test files should be python files (extension: `.py`)
-   All your test files and folders should start with `test_`
-   Your file organization in the tests folder should be the same as your project: ex: for `models/base.py`, unit tests must be in: `tests/test_models/test_base.py`
-   All your tests should be executed by using this command: `python3 -m unittest discover tests`
-   You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base.py`
-   We strongly encourage you to work together on test cases so that you don't miss any edge case

Tasks
-----

### 0\. If it's not tested it doesn't work

mandatory

All your files, classes and methods must be unit tested and be PEP 8 validated.

```
guillaume@ubuntu:~/$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/$

```

*Note that this is just an example. The number of tests you create can be different from the above example.*

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `tests/`

### 1\. Base class

mandatory

Write the first class `Base`:

Create a folder named `models` with an empty file `__init__.py` inside - with this file, the folder will become a Python package

Create a file named `models/base.py`:

-   Class `Base`:
    -   private class attribute `__nb_objects = 0`
    -   class constructor: `def __init__(self, id=None):`:
        -   if `id` is not `None`, assign the public instance attribute `id` with this argument value - you can assume `id` is an integer and you don't need to test the type of it
        -   otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`

This class will be the "base" of all other classes in this project. The goal of it is to manage `id` attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

guillaume@ubuntu:~/$ ./0-main.py
1
2
3
12
4
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/base.py, models/__init__.py`

### 2\. First Rectangle

mandatory

Write the class `Rectangle` that inherits from `Base`:

-   In the file `models/rectangle.py`
-   Class `Rectangle` inherits from `Base`
-   Private instance attributes, each with its own public getter and setter:
    -   `__width` -> `width`
    -   `__height` -> `height`
    -   `__x` -> `x`
    -   `__y` -> `y`
-   Class constructor: `def __init__(self, width, height, x=0, y=0, id=None)`:
    -   Call the super class with `id` - this super call with use the logic of the `__init__` of the `Base` class
    -   Assign each argument `width`, `height`, `x` and `y` to the right attribute

Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can "trust" these attributes.

```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

guillaume@ubuntu:~/$ ./1-main.py
1
2
12
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/rectangle.py`

### 3\. Validate attributes

mandatory

Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded):

-   If the input is not an integer, raise the `TypeError` exception with the message: `<name of the attribute> must be an integer`. Example: `width must be an integer`
-   If `width` or `height` is under or equals 0, raise the `ValueError` exception with the message: `<name of the attribute> must be > 0`. Example: `width must be > 0`
-   If `x` or `y` is under 0, raise the `ValueError` exception with the message: `<name of the attribute> must be >= 0`. Example: `x must be >= 0`

```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./2-main.py
[TypeError] height must be an integer
[ValueError] width must be > 0
[TypeError] x must be an integer
[ValueError] y must be >= 0
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/rectangle.py`

### 4\. Area first

mandatory

Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance.

```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())

guillaume@ubuntu:~/$ ./3-main.py
6
20
56
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/rectangle.py`

### 5\. Display #0

mandatory

Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#` - you don't need to handle `x` and `y` here.

```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()

guillaume@ubuntu:~/$ ./4-main.py
####
####
####
####
####
####
---
##
##
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/rectangle.py`

### 6\. __str__

mandatory

Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`

```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
""" 5-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

guillaume@ubuntu:~/$ ./5-main.py
[Rectangle] (12) 2/1 - 4/6
[Rectangle] (1) 1/0 - 5/5
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/rectangle.py`

### 7\. Display #1

mandatory

Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character `#` by taking care of `x` and `y`

```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()

guillaume@ubuntu:~/$ ./6-main.py | cat -e
$
$
  ##$
  ##$
  ##$
---$
 ###$
 ###$
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/rectangle.py`

### 8\. Update #0

mandatory

Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute:

-   1st argument should be the `id` attribute
-   2nd argument should be the `width` attribute
-   3rd argument should be the `height` attribute
-   4th argument should be the `x` attribute
-   5th argument should be the `y` attribute

This type of argument is called a "no-keyword argument" - Argument order is super important.

```
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)

guillaume@ubuntu:~/$ ./7-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (89) 10/10 - 10/10
[Rectangle] (89) 10/10 - 2/10
[Rectangle] (89) 10/10 - 2/3
[Rectangle] (89) 4/10 - 2/3
[Rectangle] (89) 4/5 - 2/3
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/rectangle.py`

### 9\. Update #1

mandatory

Update the class `Rectangle` by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes:

-   `**kwargs` can be thought of as a double pointer to a dictionary: key/value
    -   As Python doesn't have pointers, `**kwargs` is not literally a double pointer -- describing it as such is just a way of explaining its behavior in terms you're already familiar with
-   `**kwargs` must be skipped if `*args` exists and is not empty
-   Each key in this dictionary represents an attribute to the instance

This type of argument is called a "key-worded argument". Argument order is not important.

```
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
""" 8-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)

guillaume@ubuntu:~/$ ./8-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (1) 10/10 - 10/1
[Rectangle] (1) 2/10 - 1/1
[Rectangle] (89) 3/1 - 2/1
[Rectangle] (89) 1/3 - 4/2
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/rectangle.py`

### 10\. And now, the Square!

mandatory

Write the class `Square` that inherits from `Rectangle`:

-   In the file `models/square.py`
-   Class `Square` inherits from `Rectangle`
-   Class constructor: `def __init__(self, size, x=0, y=0, id=None):`:
    -   Call the super class with `id`, `x`, `y`, `width` and `height` - this super call will use the logic of the `__init__` of the `Rectangle` class. The `width` and `height` must be assigned to the value of `size`
    -   You must not create new attributes for this class, use all attributes of `Rectangle` - As reminder: a Square is a Rectangle with the same width and height
    -   All `width`, `height`, `x` and `y` validation must inherit from `Rectangle` - same behavior in case of wrong data
-   The overloading `__str__` method should return `[Square] (<id>) <x>/<y> - <size>` - in our case, `width` or `height`

As you know, a Square is a special Rectangle, so it makes sense this class Square inherits from Rectangle. Now you have a Square class who has the same attributes and same methods.

```
guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
""" 9-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()

guillaume@ubuntu:~/$ ./9-main.py
[Square] (1) 0/0 - 5
25
#####
#####
#####
#####
#####
---
[Square] (2) 2/0 - 2
4
  ##
  ##
---
[Square] (3) 1/3 - 3
9

 ###
 ###
 ###
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/square.py`

### 11\. Square size

mandatory

Update the class `Square` by adding the public getter and setter `size`

-   The setter should assign (in this order) the `width` and the `height` - with the same value
-   The setter should have the same value validation as the `Rectangle` for `width` and `height` - No need to change the exception error message (It should be the one from `width`)

```
guillaume@ubuntu:~/$ cat 10-main.py
#!/usr/bin/python3
""" 10-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./10-main.py
[Square] (1) 0/0 - 5
5
[Square] (1) 0/0 - 10
[TypeError] width must be an integer
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/square.py`

### 12\. Square update

mandatory

Update the class `Square` by adding the public method `def update(self, *args, **kwargs)` that assigns attributes:

-   `*args` is the list of arguments - no-keyworded arguments
    -   1st argument should be the `id` attribute
    -   2nd argument should be the `size` attribute
    -   3rd argument should be the `x` attribute
    -   4th argument should be the `y` attribute
-   `**kwargs` can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
-   `**kwargs` must be skipped if *args exists and is not empty
-   Each key in this dictionary represents an attribute to the instance

```
guillaume@ubuntu:~/$ cat 11-main.py
#!/usr/bin/python3
""" 11-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)

guillaume@ubuntu:~/$ ./11-main.py
[Square] (1) 0/0 - 5
[Square] (10) 0/0 - 5
[Square] (1) 0/0 - 2
[Square] (1) 3/0 - 2
[Square] (1) 3/4 - 2
[Square] (1) 12/4 - 2
[Square] (1) 12/1 - 7
[Square] (89) 12/1 - 7
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/square.py`

### 13\. Rectangle instance to dictionary representation

mandatory

Update the class `Rectangle` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle`:

This dictionary must contain:

-   `id`
-   `width`
-   `height`
-   `x`
-   `y`

```
guillaume@ubuntu:~/$ cat 12-main.py
#!/usr/bin/python3
""" 12-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(1, 1)
    print(r2)
    r2.update(**r1_dictionary)
    print(r2)
    print(r1 == r2)

guillaume@ubuntu:~/$ ./12-main.py
[Rectangle] (1) 1/9 - 10/2
{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
<class 'dict'>
[Rectangle] (2) 0/0 - 1/1
[Rectangle] (1) 1/9 - 10/2
False
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/rectangle.py`

### 14\. Square instance to dictionary representation

mandatory

Update the class `Square` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`:

This dictionary must contain:

-   `id`
-   `size`
-   `x`
-   `y`

```
guillaume@ubuntu:~/$ cat 13-main.py
#!/usr/bin/python3
""" 13-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)

guillaume@ubuntu:~/$ ./13-main.py
[Square] (1) 2/1 - 10
{'id': 1, 'x': 2, 'size': 10, 'y': 1}
<class 'dict'>
[Square] (2) 1/0 - 1
[Square] (1) 2/1 - 10
False
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/square.py`

### 15\. Dictionary to JSON string

mandatory

JSON is one of the standard formats for sharing data representation.

Update the class `Base` by adding the static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries`:

-   `list_dictionaries` is a list of dictionaries
-   If `list_dictionaries` is `None` or empty, return the string: `"[]"`
-   Otherwise, return the JSON string representation of `list_dictionaries`

```
guillaume@ubuntu:~/$ cat 14-main.py
#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))

guillaume@ubuntu:~/$ ./14-main.py
{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
<class 'dict'>
[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
<class 'str'>
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/base.py`

### 16\. JSON string to file

mandatory

Update the class `Base` by adding the class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file:

-   `list_objs` is a list of instances who inherits of `Base` - example: list of `Rectangle` or list of `Square` instances
-   If `list_objs` is `None`, save an empty list
-   The filename must be: `<Class name>.json` - example: `Rectangle.json`
-   You must use the static method `to_json_string` (created before)
-   You must overwrite the file if it already exists

```
guillaume@ubuntu:~/$ cat 15-main.py
#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())

guillaume@ubuntu:~/$ ./15-main.py
[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/base.py`

### 17\. JSON string to dictionary

mandatory

Update the class `Base` by adding the static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`:

-   `json_string` is a string representing a list of dictionaries
-   If `json_string` is `None` or empty, return an empty list
-   Otherwise, return the list represented by `json_string`

```
guillaume@ubuntu:~/$ cat 16-main.py
#!/usr/bin/python3
""" 16-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    list_input = [
        {'id': 89, 'width': 10, 'height': 4},
        {'id': 7, 'width': 1, 'height': 7}
    ]
    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))

guillaume@ubuntu:~/$ ./16-main.py
[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]
[<class 'str'>] [{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]
[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/base.py`

### 18\. Dictionary to Instance

mandatory

Update the class `Base` by adding the class method `def create(cls, **dictionary):` that returns an instance with all attributes already set:

-   `**dictionary` can be thought of as a double pointer to a dictionary
-   To use the `update` method to assign all attributes, you must create a "dummy" instance before:
    -   Create a `Rectangle` or `Square` instance with "dummy" mandatory attributes (width, height, size, etc.)
    -   Call `update` instance method to this "dummy" instance to apply your real values
-   You must use the method `def update(self, *args, **kwargs)`
-   `**dictionary` must be used as `**kwargs` of the method `update`
-   You are not allowed to use `eval`

```
guillaume@ubuntu:~/$ cat 17-main.py
#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)

guillaume@ubuntu:~/$ ./17-main.py
[Rectangle] (1) 1/0 - 3/5
[Rectangle] (1) 1/0 - 3/5
False
False
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/base.py`

### 19\. File to instances

mandatory

Update the class `Base` by adding the class method `def load_from_file(cls):` that returns a list of instances:

-   The filename must be: `<Class name>.json` - example: `Rectangle.json`
-   If the file doesn't exist, return an empty list
-   Otherwise, return a list of instances - the type of these instances depends on `cls` (current class using this method)
-   You must use the `from_json_string` and `create` methods (implemented previously)

```
guillaume@ubuntu:~/$ cat 18-main.py
#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

guillaume@ubuntu:~/$ ./18-main.py
[139785912033120] [Rectangle] (1) 2/8 - 10/7
[139785912033176] [Rectangle] (2) 0/0 - 2/4
---
[139785911764752] [Rectangle] (1) 2/8 - 10/7
[139785911764808] [Rectangle] (2) 0/0 - 2/4
---
---
[139785912058040] [Square] (5) 0/0 - 5
[139785912061848] [Square] (6) 9/1 - 7
---
[139785911764976] [Square] (5) 0/0 - 5
[139785911765032] [Square] (6) 9/1 - 7
guillaume@ubuntu:~/$

```

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0C-python-almost_a_circle`
-   File: `models/base.py`

Copyright © 2022 ALX, All rights reserved.

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x0A$ ./101-main.py
John
[TypeError] can't add new attribute
guillaume@ubuntu:~/0x0A$

```

**No test cases needed**

**Repo:**

-   GitHub repository: `alx-higher_level_programming`
-   Directory: `0x0A-python-inheritance`
-   File: `101-add_attribute.py`

Copyright © 2022 ALX, All rights reserved.