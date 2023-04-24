
# given an integer n, return True if n is within 10 of either 100 or 200


def func (num):
    return abs(num-100) <=10 or abs(num-200)<=10

print(func(110))

