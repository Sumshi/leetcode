#!/bin/python3
import unittest
from palindrome import Solution

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(121), True)
        self.assertEqual(sol.isPalindrome(12321), True)
        self.assertEqual(sol.isPalindrome(12345), False)
        self.assertEqual(sol.isPalindrome(-121), False)
        self.assertEqual(sol.isPalindrome(10), False)

if __name__ == '__main__':
    unittest.main()

