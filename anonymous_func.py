# LAMBDA

# first example

mylist = [2,4,5,6,8,9,10,20]

new_list = sorted(mylist, key = lambda x : -x)

print(new_list)
'''key here  does not apply the operation and return that.
 forexample does not apply - operator  on the numbers and return -200 or -400 or -1, in fact,
  for each element of list it make them negative just to compare them when they are negative,
   it doe snot make them negative and return negative
'''

# second example:

result = lambda x : x ** 2
print(result(2))


# third examp

# we have list of authors who have name and middle name family name,
# so we want to sort them based on just tehir family name

authors = ["Issac Assiomve", "Ray Bradny", " Robert heniki",
           " Arthur C. clarck", "fRank Harbert", "orson scott Card"]

new_sort = sorted(authors, key = lambda author: author.split(" ")[-1].lower() )

print(new_sort)


# --------------------------------------------------------------------

# MAP


list_1 = [3,4,5,6]

new_l1 = map(lambda x : x ** 2, list_1)

for i in new_l1:
    print(i)

# --------------------------------------------------------------------

# FILTER

# it uses to select certain peices of data from a list,tuple or other collection of data, it filters out the data we dont need
# when we have condition we can use filter

mylistc = [2,3,4,5,7,6]

new_mylistc = filter(lambda x : x%2 == 0, mylistc)

for i in new_mylistc:
    print(i)
# --------------------------------------------------------------------