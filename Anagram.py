#!/usr/bin/python3
def are_anagrams(str1, str2):
    """
    check if two strings are anagrams, meaning they contain same characters
    Rules:
    i) Both strings should be of equal length
    ii) Both strings should contain same characters
    """
    if len(str1) != len(str2):
        return False # not anagrams
    else:
        if sorted(str1) == sorted(str2):
            return True

# Example usage
str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))
