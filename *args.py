# Write python function which takes a variable number of arguments

def func(*args):
    for i in args:
        print(i, end = " ")

func(4,5,6,7,8)


# ------------------------------------------

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
student_info("math", "art", name = "john", age = 22)


# ------------------------------------------

# if we want to unpack a sequence or dictionary and pass those values into the function individually

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ["math", "art"]
info = {"name": "joe", "age":15}

student_info(*courses, **info)


# ------------------------------------------------

# Write python function which takes a variable number of arguments
def func(*args):
    for i in args:
        print(i)


func(1, 2, 3)


# ------------------------------------------------
# Write a program which takes a sequence of numbers and check if all numbers are unique.
# You can do this by converting the list to set by using set() method and comparing the length of
# this set with the length of the original list. If found equal, return True.

def func_var(data_list):
    if len(data_list) == len(set(data_list)):
        return True
    else:
        return False


print(func_var([3, 4, 3, 2]))
print(func_var([3, 4, 5, 6, 7]))


# ------------------------------------------------
# Write a Program to add two integers >0 without using the plus operator.

def calculate_add(n1, n2):
    if n1 > 0 and n2 > 0:
        x = sum((n1, n2))
    else:
        print("please provide numbers bigger than 0 ")
    return x


print(calculate_add(3, 4))


def add_nums(num1, num2):
    while num2 != 0:
        data = num1 & num2
        num1 = num1 ^ num2
        num2 = data << 1
    return num1


print(add_nums(2, 10))

# ------------------------------------------------

# Write a Program to solve the given equation assuming that a,b,c,m,n,o are constants:

# ax + by = c
# mx + ny = o


a, b, c, m, n, o = 5, 9, 4, 7, 9, 4
temp = a * n - b * m
if n != 0:
    x = (c * n - b * o) / temp
    y = (a * o - m * c) / temp
    print(str(x), str(y))

# ------------------------------------------------
# Write a Program to match a string that has the letter ‘a’ followed by 4 to 8 'b’s

import re


def match_text(txt_data):
    pattern = 'ab{4,8}'
    if re.search(pattern, txt_data):  # search for pattern in txt_data
        return 'Match found'
    else:
        return ('Match not found')


print(match_text("abc"))  # prints Match not found
print(match_text("aabbbbbc"))  # prints Match found

# ------------------------------------------------

#  Write a Program to combine two different dictionaries. While combining, if
#     you find the same keys, you can add the values of these same keys. Output the new dictionary
#
from collections import Counter

d1 = {'key1': 50, 'key2': 100, 'key3': 200}
d2 = {'key1': 200, 'key2': 100, 'key4': 300}
new_dict = Counter(d1) + Counter(d2)
print(new_dict)
