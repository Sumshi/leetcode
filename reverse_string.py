#!/usr/bin/python3
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None
        """
        left = 0  # represents left of list
        right = len(s) - 1 # represents right of list

        while left < right:
            s[left], s[right] = s[right], s[left] # swaps left and right
            left += 1 # left element goes to next
            right -= 1 # decrements backwords

solution = Solution()
s = ["h", "e", "l", "l", "o"]
solution.reverseString(s)
print(s)  # Output: ["o", "l", "l", "e", "h"]
