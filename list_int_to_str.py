# convert list of integers to list of strings
mylist = [3,4,5,6,7]

def int_to_str(mylist):

    result = map(str,mylist)

    return list(result)


print(int_to_str(mylist))


# second approach

def  int_to_str2(mylist):
    new_list = []
    for i in mylist:
        new_list.append(str(i))
    return new_list

print( int_to_str2(mylist))


# third approach

def  int_to_str3(mylist):

    new_list = [ str(i) for i in mylist]
    return new_list


print( int_to_str3(mylist))


# Converting integer list to string list
# and joining the list using join()

def int_to_str4(mylist):

    result = "".join(map(str, mylist))

    return result




print(int_to_str4(mylist))


