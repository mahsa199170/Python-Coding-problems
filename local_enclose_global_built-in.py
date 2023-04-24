''' LOCAL
    ENCLOSED
    GLOBAL
    BUILT-IN
    '''

name = "this is a global string"

def greet():
    name = "Sammy"
    def hello():
        print("hello " + name)

    hello()
greet()

# priotity in python is first check for local, if there isnt any local, then check for enclosed, if there isnt any
# then checked for global, if there isnt any, then check for built-in

# *******************
x = 50

def func(x):
    print("x is:{}".format(x))

func(x)

# *******************
x = 50
def func(x):
    print("x is:{}".format(x))
    x = 200
    print("x is:{}".format(x))

func(x)

# ***********************
# if we are in a situation and want to grab the global x=50 and reassign it to be 200, how we can do that.
# in this case we want to accept x as a parameter adn instead of that inside our function declare the global keyword
# in the beginning of learning it is better not to do this, instead you can
# put the function inside a variable and print that variable

x = 50
def func():
    global x
    print(f"x is {x}")

    x = 200
    print(f"i just changed the gloabl x to {x}")

func()

print(f"in golabl x is {x}")
# safer way for now:
x = 50
def func(x):
    x = 200
    return(x)
y = func(x)

print(f"this is {y}")