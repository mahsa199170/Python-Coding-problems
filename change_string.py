# strings are immutable, how to change the string?


str1 = "samuel"

def change_string(str1):
    remain= str1[1:]
    new_str1 = "p" + remain


    return new_str1

print(change_string(str1))



