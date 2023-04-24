dict = {}

dict[2] = 56
dict[1] = 2
dict[5] = 12
dict[4] = 24
dict[6] = 18
dict[3] = 323

print(dict)

#  Displaying the Keys in sorted order

# for i in sorted(dict.keys()):
#     print(i, end = " ")

# *******************************************************************


# Displaying the values in sorted order

# for i in sorted(dict.values()):
#     print(i, end = " ")
#

# *******************************************************************

# Sort the dictionary by key

# from collections import OrderedDict
#
# dict1 = OrderedDict(sorted(dict.items()))
# print(dict1)


# *******************************************************************


# Sorting the Keys and Values in Alphabetical Order using the Key

# for i in sorted(dict.keys()):
#     print((i, dict[i]), end = " ")

# *******************************************************************

# Sorting the Keys and Values alphabetically using the value


print(sorted(dict.items(), key = lambda kv : (kv[1], kv[0])))
# *******************************************************************
# sorting dict using value

# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
# {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
#
# # To sort it in descending order just add reverse=True:
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse = True)}
# {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}



# dictionaries are unordered but if we want teh capabilties of a dictionary
# but would like ordering as well, we can use "orderdict" objt.items())))