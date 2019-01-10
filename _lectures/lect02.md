---
num: "lect02"
lecture_date:  2019-01-10
desc: "Python Strings and Functions"
ready: true
pdfurl: /lectures/pdf/lect02.pdf
annotatedpdfurl: /lectures/lect02_ann.pdf
---


# Resources from lecture

* [Link to all code written in lecture](https://github.com/ucsb-cs8-w19-mirza/cs8-w19-lectures)

## Announcements: 

* Office hours today


## Today's lecture:

## Review
* Python as a calculator
* Storing data using variables
* More than just a calculator (working with other data types)

 
## Strings
* Indexing strings and substrings
    - In a string, we can extract certain pieces from it.
    - This is known as "parsing" a string
    - Positions in a string start at index 0

```python
schoolName = "UCSB"
print(len(schoolName)) # 4
print(type(schoolName)) # str
print(schoolName[0])
print(schoolName[3])
#print(schoolName[4]) #ERROR
print(schoolName[-1]) # B - refers to the last index
#print(schoolName[-5]) # ERROR

#Extract a substring
print(schoolName[1:3]) # from position 1 up to (but not
                       # including) position 3
                       
# compute salary
hours = 40
rate = 10
salary = hours * rate
print("Salary is $", salary) # Notice quotes aren't displayed on the string in the outpout


 
# We use something called ESCAPE CHARACTERS to print
# special characters including quotes.

print("\"Hi!\"") # \" is the double quote characters
print("Hi\nthere\n!") # \n is the newline character


# Another larger example
TAX_RATE = 0.1
print("Hi, please enter your name: ")
userName = input()
print("Hi", userName, ". What is the amount of your bill \
(not including tax and tip)?")
totalBill = float(input()) #be careful, will crash if not float
print("What is the tip percentage you would like to leave?")
tipPercentage = float(input())
taxAmount = totalBill * TAX_RATE
tipAmount = totalBill * (tipPercentage / 100)
print("The total amount to pay is $", totalBill + taxAmount + tipAmount)


## Functions
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

```






