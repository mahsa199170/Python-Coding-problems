# 5! = 5 * 4 * 3 *2 *1

def factorial(num):
    if num == 1 or num ==0:
        return 1
    return num * factorial(num-1)

print(factorial(5))


# ------------------------------------------

# seond approach

def factorial1(num):
    result = 1
    if num < 0:
        return "please enter a number bigger than 0 "
    elif num == 0 or num == 1:
        return 1
    for i in range(1,num+1):
        result *= i
    return result

print(factorial1(3))


