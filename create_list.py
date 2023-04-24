# create a list which is [0,0,0]

#  first approach:
l = [ i * 0 for i in range(3)]
print(l)

# second approach:
mylist = []
for i in range(3):
    mylist.append(0)
print(l)

# third approach:
print([0]*3)


# ---------------

#  we have one "z" , how can we have "zzzzzzzzzz"

x  = "z"
print(x * 10)