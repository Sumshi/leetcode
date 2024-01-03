#!/usr/bin/python3
# count the number of times characters appear in a string
def count_characters(s):
    l = list(s)
    frequency = [l.count(element) for element in l]
    return dict(zip(l, frequency))

# Example usage
input_str = "hello"
char_count_result = count_characters(input_str)
print(char_count_result)
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}