# Write a program which takes a sequence of numbers and check if all numbers are unique.

def unique(arr):
    myset = set()

    for i in arr:
        if i in myset:
            return "not unique"
        else:
            myset.add(i)
    return "unique"


print(unique([3, 4, 5, 6]))


# second approach:

# You can do this by converting the list to set by using set() method and comparing the length of
# this set with the length of the original list. If found equal, return True.

def unique1(arr):
    if len(arr) == len(set(arr)):
        return True
    else:
        return False


print(unique1([5, 4, 6, 3, 2, 3]))
