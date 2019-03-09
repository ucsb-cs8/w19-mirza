---
num: "lect15"
desc: "Dictionaries contd"
pdfurl: /lectures/pdf/lect15.pdf
ready: true
lecture_date:  2019-03-07
annotatedpdfurl: /lectures/pdf/lect15_ann.pdf
annotatedready: true
---

''' Dictionaries
- New Tool: DICTIONARIES
- Otherwise known as TABLES or MAPS
    - Works where a KEY maps to a VALUE
    - Use dictionaries for two main reasons:
        - Gives us more precise indexing than Lists
        - L['someString'] - allows us to index elements
        based on some key
        - Performance is MUCH better than searching through
        Lists.
            - keys are HASHED to a specific index value
                - keys are passed through some math equation
                and an index is computed
                - Provides DIRECT ACCESS to the value given a
                key.
            - Details of hashing is not discussed in this class,
            but you may see it sometime...
'''
''' Syntax for Dictionaries
{<key1>:<value1>,<key2>:<value2>, ... , <keyn>:valuen>}
'''

D = {} # Empty dictionary. Notice the curly braces instead of []

D = {'Jane':18, 'Jen':19, 'Joe':20, 'John':21}

'''
print(D)
print("Jane's age is:", D['Jane'])
print(len(D))

# Simple way to get key / value
for x in D:
    print(x) # Prints the keys
    print(D[x]) # Prints the values
'''
''' Restrictions on using Dictionaries
- Keys must be an immutable type (int, str, namedtuples, - not
lists for example).
- Values can be anything (mutable or immutable objects)
- For our purposes, KEYS are UNIQUE. Don't define something like
{'Joe':17, 'Joe':18}.
- Python is actually OK with duplicate keys and it will return
the last key/value in the dictionary.
- Again, for our purposes, we should never use duplicate key
values (kinda defeats the purpose of dictionaries).
'''

''' dictionary methods
    D.pop(key) # remove and return the value
    D.update(D2) # combine values in D and D2
    D.get(key) # returns item if it exists. If not, returns None or a default value
    D.keys() # dict_keys([ LIST OF KEYS ])
    D.values() # dict_values([ LIST OF VALUES ])
    D.items() # dict_items([ LIST OF KEY,VALUE ])
'''
'''
value = D.pop('John')
print(D)
print(value)
D.update({'Jess':25,'Jerry':27})
print(D)

# What if something is not in the dictionary and we try to access it?
#print(D["CS8"]) #ERROR - "CS8" key doesn't exist.
print(D.get("CS8"))

# Can define the default return value if key doesn't exist
print(D.get("CS8", "not in dictionary!"))

print(D.keys())
print(D.values())
'''
'''
for item in D.keys():
    print(item)
'''
'''
keys = D.keys()
#print(keys[2]) # ERROR - Not a list!
print(list(keys)[2]) # OK
'''

# Example of adding to a dictionary
D = {}
print(D)
D['CS8'] = "UCSB"
print(D)
D['CS16'] = "UCSB"
print(D)
'''

```