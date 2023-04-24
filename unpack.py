work_hours = [("Adby", 100), ("joe", 200), ("Rose", 300)]


def best_employee(work_hours):
    max_hours = 0
    best_employee = ""

    for name,hours in work_hours:
        if hours > max_hours:
            max_hours = hours
            best_employee = name
    return (max_hours, best_employee)

    # if we return like this:
    # return (f"the best employee is {best_employee} with {max_hours} of working")
    # and then do: name,hours = best_employee(work_hours) we will get
    # valueError:too many values to unpack (expected 2) and thats because function is returning a
    # formatted string, which cannot be unpacked into two separate variables




print(best_employee(work_hours))

name,hours = best_employee(work_hours)

print(name)
print(hours)



# ----------------------------------

l = [(2, 5, 5), (1, 3, 3), (4, 6, 1)]

for x, y, z in l :
    print(x, end = " ")
    print(y, end = " ")
    print(z, end = " ")

# ----------------------------------

# dictionary unpacking

dict = {"name" : "luna", "age":5, "breed": "german"}
for key,value in dict.items():
    print(key,value)

for item in dict.items():
    print(item)


# ----------------------------------
# tuple unpacking:

word = "abcd"
for index,letter in enumerate(word):
    print(index)
    print(letter)

# ----------------------------------
# zipping
# zipp function return tuple
l1 = [1, 2, 3]
l2 = ["a", "b", "c"]

print(list(zip(l1,l2)))
for i in zip(l1,l2):
    print(i)

# ----------------------------------

# list comprehension

x = [ x if x%2 == 0 else "odd" for x in range(10) ]
print(x)
x = [ (i,j) for i in "abc" for j in range(3)]
print(x)