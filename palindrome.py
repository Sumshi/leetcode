#!/usr/bin/python3

"""write a function that checks if a number is palindrome or not"""

class Solution(object):
    def isPalindrome(self, x):
        """convert the number to string"""
        x_string = str(x)
        # reverse the string
        reversed_str = x_string[::-1]

        # check if reversed string is same as original string
        if x_string == reversed_str:
            return True # means it is palindrome
        else:
            return False # not palindrome

# Create an instance of the Solution class
sol = Solution()
#test cases
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(12345))
