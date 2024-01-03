#!/usr/bin/python3
# count the number of times characters appear in a string
def count_characters(s):
    char_count = {} # empty dictionary store the character counts.

    for char in s:
        # increment the count for each character
        char_count[char] = char_count.get(char, 0) + 1

    return char_count

# Example usage
input_str = "hello"
char_count_result = count_characters(input_str)
print(char_count_result)
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}