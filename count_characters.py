#!/usr/bin/python3
# count the number of times characters appear in a string
def count_characters(s):
    l = list(s) # convert the string to a list
    # count the number of times each character appears in the list
    frequency = [l.count(element) for element in l]
    return dict(zip(l, frequency))# zip to combine the two lists into a dictionary

# Example usage
input_str = "hello"
char_count_result = count_characters(input_str)
print(char_count_result)
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}