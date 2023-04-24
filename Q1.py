'''define a function that takes a string, and returns a matching
 string where every even letter is uppercase and every odd letter is lower case'''


def func(name):
    result = []
    for index,letter in enumerate(name):
        if index % 2 == 0:
             result.append(name[index].upper())
        else:
            result.append(name[index].lower())
    return "".join(result)


print(func("John Doe"))
