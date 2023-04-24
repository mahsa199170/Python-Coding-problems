a = 4
b = 6

def swap(a,b) :
    a,b = b, a

    return (a,b)

print(swap(a,b))


# -------------------------------

# second approach

def swap_1(a,b):
    temp = a
    a = b
    b = temp

    return(a,b)


print(swap_1(a,b))