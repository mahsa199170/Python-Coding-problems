# Write python function which takes a variable number of arguments

def func(*args):
    for i in args:
        print(i, end = " ")

func(4,5,6,7,8)

