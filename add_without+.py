# Write a Program to add two integers >0 without using the plus operator.
def add_without_plus(n1,n2):
    if n1 > 0 and n2>0 :
        return sum((n1,n2))
    else:
        return ("Oops! please eneter an integer bigger than 0")

print(add_without_plus(4,0))



# second approach

def add_nums(num1, num2):
   while num2 != 0:
       data = num1 & num2
       num1 = num1 ^ num2
       num2 = data << 1
   return num1
print(add_nums(2, 10))



# the trace of the function add_nums(2, 10) step by step:
#
# num1 = 2, num2 = 10
# The while loop condition num2 != 0 is true
# data = num1 & num2 = 2 & 10 = 2 (bitwise AND of 0010 and 1010)
# num1 = num1 ^ num2 = 2 ^ 10 = 8 (bitwise XOR of 0010 and 1010)
# num2 = data << 1 = 4 (bitwise left shift of 0010 by 1)
# The while loop condition num2 != 0 is true
# data = num1 & num2 = 8 & 4 = 0 (bitwise AND of 1000 and 0100)
# num1 = num1 ^ num2 = 8 ^ 4 = 12 (bitwise XOR of 1000 and 0100)
# num2 = data << 1 = 0 (bitwise left shift of 0000 by 1)
# The while loop condition num2 != 0 is false, so the loop terminates
# The final result is num1 = 12