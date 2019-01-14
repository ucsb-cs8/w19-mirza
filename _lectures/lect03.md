---
num: "lect03"
lecture_date:  2019-01-15
desc: "Python Functions and Test Framework"
ready: true
pdfurl: /lectures/pdf/lect03.pdf
annotatedpdfurl: /lectures/lect03_ann.pdf
---


# Resources from lecture

* [Link to all code written in lecture](https://github.com/ucsb-cs8-w19-mirza/cs8-w19-lectures)

## Today's lecture:

* Working with strings and lists
* Functions: Using existing ones, defining new functions

## Concept Questions

* Check your understanding: [Lect 03 Concept Questions](lect03-concept.md){:data-ajax ="false"}
* You'll need your iclickers to participate in class



# Function definition
def double(n):
    ''' Returns 2 times the parameter '''
    return 2 * n

'''
- The "def" indicates a function definition
- "double" is the name of the function
- (n) denotes the parameter(s) of a function
- name + parameters is known as a function SIGNATURE
- The actual code (instructions) (ex: return 2 * n)
is known as the function BODY
- Note: The function body needs to be indented so python
can associate the body's instructions as part of the
function's definition
- If the function returns a value, then a RETURN statement
is needed
'''
# Examples calling double()
print(double(10)) # --> print(20)
print(double(double(2))) # --> print(double(4)) --> print(8)
value = double(5) + double(6)
print(value)

print(double("2"))
print(type(double("2")))
print(double(2.5))
print(type(double(2.5)))
print(double([2,4,6]))

# pytest
Good defensive coding style means that you think about how you would
test your code.
* Overview of lab01 and how to use the pytest framework

```
















