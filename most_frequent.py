# we want to print the most common character in a string

letter = "aaaaaabbbbbbbqqqqqqbssssiiiqq"

def most_frequent(s):

    dict = {}
    for i in letter:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    mylist = []

    for key, value in dict.items():
        mylist.append((key, value))

    max_val = max(mylist, key=lambda x: x[1])
    # max_val = max(mylist, key = lambda x:x[1])[1]  if we want to get the second element

    return max_val

print(most_frequent(letter))

# ----------------------------------------------


# second approach


from collections import Counter

letter = "aaaaaabbbbbbbqqqqqqbssssiiiqq"
c = Counter(letter)
print(c)   #Counter({'b': 8, 'q': 8, 'a': 6, 's': 4, 'i': 3})
print(c.most_common()) #[('b', 8), ('q', 8), ('a', 6), ('s', 4), ('i', 3)]

# if we want to get forexample the three most commons
print(c.most_common(3)) #[('b', 8), ('q', 8), ('a', 6)]