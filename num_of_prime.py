# write a python program to provide the number of prime numbers between 1 to a specific number

# notice:
# 1 can only be divided by one number, 1 itself, so with this definition 1 is not a prime number.


# question 1 :

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def num_of_prime(num):
    count = 0
    for i in range(1, num):
        if is_prime(i):
            count += 1

    return count


print(num_of_prime(10))


# ------------------------------------------------------

# question 2

# sum of the prime numbers between a number:


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def num_of_prime(num):
    count = 0
    for i in range(1, num):
        if is_prime(i):
            count += i

    return count


print(num_of_prime(10))

