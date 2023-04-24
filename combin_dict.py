#Write a Program to combine two different dictionaries. While combining, if
#you find the same keys, you can add the values of these same keys. Output the new dictionary

d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}


def combine_dicts (d1, d2):


    for key, value in d1.items():
        if key in d2:
            d2[key] += value
        else:
            d2[key] = value

    return d2

print(combine_dicts(d1,d2))


