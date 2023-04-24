# given a list of ints, True if the array contains a 3 next to a 3 somewhere

# first appproach

def check_side(arr):
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1] and arr[i] == 3:
            return True

    return False

print(check_side([1,2,3,4]))


# ---------------------------------------------

# second approach

def check(arr):
    for i in range(len(arr)):
        if arr[i:i+2] == [3,3]:
            return True
    return False

print(check([1,2,3,4,53,3,3]))

