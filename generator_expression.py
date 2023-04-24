'''generators allow us to generate a sequence of values over time, instead of to craete an
entire sequence and hold it in memory.
generator functions will automatically suspend and resume their execution and state around the
last point of value generation
the advantage is that instead of having to compute an entire seris of values up front,
the generator computes one value, waits until the next value is called for
'''

# because generators do not hold the entire result in memory,they yield results one by one
# thats why we need to loop through it to get amounts one by one

nums = [1,2,3,4,5,6,7,8,9,10]
# for printing generators we have three way: 1- convert to list 2- loop through it 3-using next

def gen_func(num):
    for n in num:
        yield n*n
my_gen = gen_func(nums)

# printing using for loop
for n in gen_func(nums):
    print(n)
# **********************
# printing using list
# print(list(my_gen))

# ***********************
# printing using next
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))


# generator expression
my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)
#-------------------------------------------------------------------------

# write a code and define two lists one for names and one for majors,
# i want randomly put an id and name and major for each person add them to a list

import random
names = ["john", " corey", "amy","steve","rick", "thomas"]
majors = ["math", "engineering", "compsci", "arts", "business"]

def p (num_peopel):
    result = []


    for i in range(num_peopel):
        person = {}
        person["name"] = random.choice(names)
        person["major"] = random.choice(majors)
        person["id"] = i

        # person = {
        #     "id": i,
        #     "name": random.choice(names),
        #     "major": random.choice(majors)
        # }
        result.append(person)

    return result

print(p(4))

# ***********************************

# solving this question using generator expression

