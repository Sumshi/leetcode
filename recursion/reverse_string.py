#!/usr/bin/python3
# prints a string in reverse
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
s = "Python"
print(reverse(s)) # Output: nohtyP