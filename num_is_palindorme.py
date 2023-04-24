# check if a number is palindrome


def num_is_palindrome(num):
    n = num
    rev = 0

    while n > 0 :
        rev = rev * 10 + (n % 10 )
        n= n//10

    if num == rev:
        return ("Palindorme")
    else:
        return ("Not palindorme")



print(num_is_palindrome(12321)) # Palindrome
print(num_is_palindrome(12345)) # Not palindrome
print(num_is_palindrome(1001)) # Palindrome

