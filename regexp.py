# Write a Program to match a string that has the letter ‘a’ followed by 4 to 8 'b’s

import re
#
# def match_pattern(text):
#
#     # pattern = "ab{4,8}$"
#     pattern = "ab{4} | ab{8}"
#
#     if re.search(pattern, text):
#         return "Match found"
#     else:
#         return "Not found"

def match_pattern(text):
    pattern = "ab{4}|ab{8}"  # updated pattern

    if re.search(pattern, text):
        return "Match found"
    else:
        return "Not found"


print(match_pattern("abbbbbbbb")) # Match found
print(match_pattern("abbbbb")) # Not found


