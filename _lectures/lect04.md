---
num: "lect04"
lecture_date: 2019-01-17
desc: "Lists and Tuples"
ready: false
pdfurl: /lectures/pdf/lect04.pdf
annotatedpdfurl: /lectures/lect04_ann.pdf
---

# Resources from lecture

* [Link to all code written in lecture](https://github.com/ucsb-cs8-w19-mirza/cs8-w19-lectures)

# Topics
```

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
```



