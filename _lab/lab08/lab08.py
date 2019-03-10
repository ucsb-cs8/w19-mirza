# Student(s): (insert name here)
# Make sure to read the comments for each function.

# Do not delete this method, this is to help grade your subsmissions
def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__
    return helper

# Make sure @call_counter is present above every method (Do not delete it)
@call_counter
def recursiveDigitSum(n):
    '''
    Computes the sum of digits of a positive integer n
    Your solution must use recursion in order to receive credit.
    '''
    return "stub"

@call_counter
def recursiveFactorial(n):
    '''
    Computes the factorial of positive integer n
    Your solution must use recursion in order to receive credit.
    '''
    return "stub"

@call_counter
def recursiveAccumulateVowels(s):
    '''
    The parameter s is a string. This function returns a string that
    contains only the vowels in the string.
    - The returned string contains the vowels in order of appearance
    (for example, "apple" -> "ae").
    - Your solution must use recursion in order to receive credit.
    '''
    return "stub"
