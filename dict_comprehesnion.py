# i want a dict for these list as name : heroes
# normal way:

names = ["Bruce", "clarck", "Peter"]
heroes = ["Batman", 'Superman', "Spiderman"]





# dict = {}
# new_list = zip(names,heroes)
# for name,hero in new_list:
#     dict[n] = h
#
# print(dict)

# using dictionary comrehension

dict = {name : hero for name,hero in zip(names,heroes) if name != "Peter"}
print(dict)




