# Student(s): (insert name here)
# Make sure to read the comments for each function.

import pytest
'''
  You will write your own test cases (3 - 5 tests per function). 
  There's an example for each function to test: 
'''
####################
from lab08 import recursiveDigitSum

def test_recursiveDigitSum_0():
    assert recursiveDigitSum(1234) == 10

# Your tests for recursiveDigitSum...

####################
from lab08 import recursiveFactorial

def test_recursiveFactorial_0():
    assert recursiveFactorial(4) == 24

# Your tests for recursiveFactorial...

####################
from lab08 import recursiveAccumulateVowels

def test_recursiveAccumulateVowels_0():
    assert recursiveAccumulateVowels("apple") == "ae"

# Your tests for recursiveAccumulateVowels...
