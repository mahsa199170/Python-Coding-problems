# ** if we access to a dict key which does not exist, we will get key error, in order to not getting error when
#     we want to get a key which is not exist, we can use .get(key) method this will return None,
#     we can also put a default message .get(key, "Not found")

# when we want to update multiple items in a dictionary we can use .update() method
# if we want to delet a key we can use del : del person["name"] or using pop() method. person.pop("name")

dog = {"name" : "luna", "age" : 5, "breed" : "german"}

# dog["breed"] = "german shephred"
# print(dog)

# update multiple items
# dog.update({"name" : "lunzza", "breed" : "german sheherd"})
# print(dog)

# del dog["age"]
# print(dog)
#
# dog.pop("breed")
# print(dog)

# loop through dict :

# how many key we have in dict:
# print(len(dog))

#
for key in dog:
    print(key)

for key in dog.keys():
    print(key)

for value  in dog.values():
    print(value)

for key,value in dog.items():
    print("{} : {}".format(key,value))

print(reversed(dog))