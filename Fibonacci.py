# fib series = 0 1 1 2 3 5 8 13 21 ....

def fib(num):
    a = 0
    b = 1

    for i in range(num):
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp

fib(10)


# ---------------------------------------------------
# secpnd approach

def fib1(num):
    mylist = [0,1]
    for i in range(1,num):
        result = mylist[i] + mylist[i-1]
        mylist.append(result)
    new_list = map(str,mylist)

    return " ".join(new_list)

print(fib1(10))


# ---------------------------------------------------
# Third approach/ recursion

def fib3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib3(n-1) + fib3(n-2)


print(fib3(10))