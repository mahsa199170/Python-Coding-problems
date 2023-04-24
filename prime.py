# Write a program in Python to check if a number is prime.

# if a number is not divisible by numbers other than 1 or itself, it is  a prime number
# infact if the number has only 2 factors between numbers from 1 to the number itslef it is a prime


#first assproach

def is_prime(num):

    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                return ("Not Prime!")
        return ("Prime!")
    else:
        return ("The number must be bigger than 1")


print(is_prime(2))


# ------------------------------------------


# second approach

def prime(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        return "prime"
    else:
        return "not prime"

print(prime(7))


# ------------------------------------------