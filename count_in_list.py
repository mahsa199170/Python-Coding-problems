# we have a list, and we want to count each number in the list
# create a for loop and have dictionary keeping track if we've already seen the number or not
# and if you've already seen it go ahead and add plus one to the count a dif you haven't seen it
# create a new key and then add one again etc...# [Python program to count the frequency of elements
#  in a list using a dictionary]

mylist = [1,1,2,3,4,4,5,5,5,6,7]


def count_each_number(mylist):
    dict = {}

    for i in mylist:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for key,value in dict.items():
        print(f"{key} : {value}")


# Driver function
if __name__ == "__main__":
    my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]


count_each_number(mylist)

