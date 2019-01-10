---
num: "lect01"
lecture_date: 2019-01-08
desc: "Orientation to the course"
ready: true
pdfurl: /lectures/pdf/lect01.pdf
annotatedpdfurl: /lectures/lect1_ann.pdf
annotatedready: false
---

# Resources from lecture

* [Link to all code written in lecture](https://github.com/ucsb-cs8-w19-mirza/cs8-w19-lectures)

# Intro to Course Logistics

* Review the syllabus at this link:  <{{site.url}}/info/syllabus/>

# Learning Something New

* Basketball: drills vs. playing the game
* Swimming, Painting, Guitar

# Intro to the Unix environment

* Unix file system
* Navigating the file system using Command Line
* Learn a few unix commands: ls, pwd, mkdir, cd, cp, mv

# Getting started with Python and IDLE

* Python REPL (Read Eval Print Loop)

Also called the Python Shell Prompt

```

Python 3.4.3 (default, Aug  9 2016, 15:36:17)
[GCC 5.3.1 20160406 (Red Hat 5.3.1-6)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 3
5
>>> 2 + 7 *4
30
>>> 2 ** 3
8
>>> 2 ** 3 ** 2
512
>>> 2 * 3 * 4
24
>>> (2 * 3) * 4
24
>>> 2 * (3 * 4)
24
>>> (2 ** 3) ** 2
64
>>> 2 ** (3 ** 2)
512
>>>
```

Note that `**` is right associative, not left associative.


* Writing simple programs in the editor
### Python as a calculator

* Numerical data types
    - Integer representing non-decimal values
    - float: Floating point number representing a decimal
        (fractional) value
* Operations with numeric types
    - Arithmetic (+ - * /), Comparison(== < > <= >=)

* Evaluating expressions:
    - Just like writing math expressions
    - Mixed types are okay     

Numerical type examples (type these in the shell to see what happens)


```python

>>> 1

>>> 1+2

>>> 4/2

>>> 1/3

>>> 6/2

>>> 1/0

>>> 1+2*4

```
 
### Storing data using variables

* Think of a variable as a box with a name
* Just like you can store things in a box, you can store values in a variable (for now we'll only store numeric values, but you can store other types as well)
* Names of variables must...
    - Start with a letter or underscore (the former is more common)
    - Remaining letters in variables names can consist of letters, numbers,
           or underscores
    - Names are case-sensitive (name and NAME are considered two different
           variables).

```python
>>>x = 10 #What is the value of x?

>>>x = x * 10 # 10 * current value of x is stored back into x


```

### More than just a calculator
* Other data types
    - int: Integer representing non-decimal values
    - float: Floating point number representing a decimal
        (fractional) value.
    - string: Represents a collection of characters
        - Examples of characters: 'A', 'a', '1', ' ', ...
    - bool: Evaluates to either True or False
        - Ex: 4 <= 6 True
        - Ex: 1 == 2 False
    - Note: 3 and 3.0 are considered different types
        - 3 is an integer
        - 3.0 is a float
    - Python knows what type these numbers are based on
        its value.

* Numerical type examples

```python
x = 1
print(x)
print(type(x))

x = 4 / 2
print(x)
print(type(x))

y = 4 * 2
print(y)
print(type(y))

z = 4 * 2.0
print(z)
print(type(z))

x = "CS 8"
print(x)
print(x*2)

x = "8.0" # string not float
print(x) #8.0
print(type(x)) #str

print(x + 2) #ERROR
print(x + "2") # No error, uses concatenation

print(float(x) + 2) # No error, 10.0

x = "8.0" # Be careful ...
print(int(x)) #crashes

x = "8"
print(int(x))

x = "8.0"
y = "8.0"
z = "8.00"

print(x == y) #True
print(x == z) #False
print(float(x) == float(z)) #True
print(2 * 3 > 5) #True
print(type(2 * 3 > 5)) # bool

```


### Interacting with a program using `print` and `input`
* When we write software, we're modeling the real world
    - ... or at least we do it as best we can
    - You can think of everything with respect to things
        and actions.
        - Things (nouns) - Objects
        - Actions (verbs) - Functions, operators, ...
    - Python (and generally all languages) gives some way
        to represent and combine these.
    - There are also ways to interact with the program
        - Generally, we call this "user input"
        - Reading files
        - clicking on buttons
        - keyboard characters
    - In order to interact with our program using text,
        Python has the input() function for us to use

```python
# Example
print("Hi, please enter your name: ")
userName = input()
print("Hello", userName)








