#!/usr/bin/python3
# factorial of a number
def factorial(n):
    # print(n)
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(150)) # Output: 120