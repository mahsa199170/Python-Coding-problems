import datetime

person = {"name" : "Joe", "age":23}

sentence = "my name is {0[name]} and i am  {1[age]} years old".format(person,person)
print(sentence)


sentence1 = "my name is {0[name]} and i am  {0[age]} years old".format(person)
print(sentence1)

l = ["jose", 23]
# here because we have three placeholder and only give one value we have to write the 0
print("my name is {0[0]} and I am {0[1]} years old".format(l))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Jose",32)

print("my name is {0.name} and i am {0.age} years old".format(p1))
print("my name is {name} and i am {age} years old".format(name = "jose", age = 30))


# we can unpack our dictionary from before into format

person = {"name" : "Joe", "age":33}
print("my name is {name} and i am {age} years old".format(**person))


for i in range(1,11):
    print("the value is {}".format(i))

#     I want these numbers to have two digits and  0 pads
for i in range(1,11):
    print("the value is {:02}".format(i))

# if i want to format in 2 decimal

pi = 3.141592
print("pi is equal to {:.2f}".format(pi))

# i want to print out  a large number but i want comma between unmners

print("1 MB is equal to {:,} bytes".format(1000000*2))
print("1 MB is equal to {:,.2f} bytes".format(1000000*2))

# format date
mydate = datetime.datetime(2090,3,21,12,12,12)
print(mydate)
print("{:%B %d %Y}".format(mydate))

# here because we have three placeholder and only give one value we have to write the 0
print("{0:%B %d %Y} fell on {0:%A} and was the {0:%j} day of the year".format(mydate))

print("{q} {b} {f}".format(f = "fox", b = "brown", q = "quick"))

# float formating {value:width.percession}
result = 100/777
print("result is : {r:1.3f}".format(r = result))
