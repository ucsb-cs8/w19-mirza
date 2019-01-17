---
num: "lect04"
lecture_date: 2019-01-17
desc: "Testing, Lists and Tuples"
ready: true
pdfurl: /lectures/pdf/lect04.pdf
annotatedpdfurl: /lectures/lect04_ann.pdf
---

# Resources from lecture

* [Link to all code written in lecture](https://github.com/ucsb-cs8-w19-mirza/cs8-w19-lectures)

# Topics
```


''' Python Testing '''

# Software testing is essential to ensure behavior works
# as expected.

# Assert statements can be scattered throughout your code
# If an assert statement fails (i.e. not True), then
# your program execution terminates.

"""
print("1st line")
assert 3 == 3 # Test passes, resumes execution.
print("2nd line")

def double(n):
    ''' Returns 2 * n '''
    return 2 * n

assert double(5) == 10
assert double(-2) == -4
assert double("UCSB") == "UCSBUCSB"
"""

'''pytest is a formal testing framework for python'''
def double(n):
    return 2 * n

def test_double_5():
    assert double(5) == 10

def test_double_negative():
    assert double(-2) == -4

def test_double_string():
    assert double("UCSB") == "UCSBUCSB"

''' running pytest on functions that start with "test_" and have
an assert statement will "automate" execution of all tests and
show which ones passed and which ones failed.

- Important since this ensures software is working as expected if
many people try to modify the code at the same time
'''


'''
Lists
    - A list is a collection of multiple values
    (similar to how a str is a collection of
    characters).
    - Note: In python, lists can be of heterogenous
    (different) types
    - Lists can have duplicate values
'''

'''
#Examples
evenNumbers = [2, "4", 6, "8"]
print(evenNumbers)
print(type(evenNumbers))
print(evenNumbers[2])
print(evenNumbers[-1])
evenNumbers.append(10)
print(evenNumbers)
#print(evenNumbers[1] + evenNumbers[2]) # ERROR
print(int(evenNumbers[1]) + evenNumbers[2])

print(evenNumbers.pop(1))
print(evenNumbers)
print(evenNumbers.pop())
print(evenNumbers)

names = ["Rick", "Morty", "Summer"]
names.sort()
print(names)
oddNumbers = [5, 3, 1]
oddNumbers.sort()
print(oddNumbers)
names.append(2018)
print(names)
names.sort() # ERROR, incompatible types 2018 is int
print(names)
'''


''' Tuples
    - A tuple is similar to a list, but with small
    (but important) differences.
    - .sort() works for lists, but not tuples
    - inherently, tuples and lists are different,
    but logically they seem the same.
    - can change an element in a list, but can't
    change them in a tuple.
'''

'''
#Examples
oddNumbers = (1, 3, 5, 7)
print(oddNumbers)
print(type(oddNumbers))
print(oddNumbers[2]) #5

oddNumbers2 = [1, 3, 5, 7]
oddNumbers2[2] = 9
print(oddNumbers2)
# oddNumbers[2] = 9 ERROR, cannot change item in tuple
#print(oddNumbers)

oddNumbers = (1, 3, 9, 7)
print(oddNumbers)
'''
''' Namedtuples
    - Package heterogenous things into a multi-
    attribute item
    - We can represent more complex data into
    specific types
    - Ex: Students
        - Name, perm, major, DOB, address, GPA,
        full-time / part-time, international, ...
    - Creating multi-attribute things is the basis
    of object oriented programming.
'''
'''
#Example on using namedtuples

# Step 1: Allow your program to use namedtuples.
from collections import namedtuple

# Step 2: Design your object
Student = namedtuple("Student", "name perm major GPA")
# Parameters of function, 1st is name of the namedtuple
# type (Student).
# 2nd parameter is a string containing the names of
# attributes

# Step 3: Create objects
s1 = Student("John Doe", 1234567, "CS", 3.5)
s2 = Student("Jane Doe", 7654321, "MUSIC", 3.9)

print("Name of s1:", s1.name)
print("Perm of s1:", s1.perm)
print("GPA of s2:", s2.GPA)
print(s1)
print(s2)
print(type(s1))
'''
```



