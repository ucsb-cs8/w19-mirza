---
num: "lect04"
lecture_date: 2019-01-17
desc: "Testing and Floating Point inaccuracies"
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

```



