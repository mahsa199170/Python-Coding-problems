# the key function is a parameter that can be used with certain built-in functions and methods
# to specify a custom sorting order for a collection of objects.
# For example, when sorting a list of dictionaries based on a specific key,
# you can use the key function to tell Python which value to use as the sorting criterion

my_list = [
    {"name": "John", "age": 35},
    {"name": "Alex", "age": 25},
    {"name": "Anna", "age": 30},
]

# sort the list of dictionaries by age
sorted_list = sorted(my_list, key=lambda x: x["age"])
print(sorted_list)

# ----------------------------------------

# key function  can be used with many built-in functions some are  min(), max(), filter(), and map(), as well as with methods like list.sort() and sorted().

my_list = ["apple", "banana", "cherry", "durian", "elderberry"]
longest_fruit = max(my_list, key=len)
print(longest_fruit)  # Output: "elderberry"

# In this example, the max() function is used to find the longest fruit in the my_list list. The key parameter is used to specify that the length of each string should be used to determine the maximum value. The len function is passed as the key function to compute the length of each string, and then the max() function returns the element with the maximum length.

# ----------------------------------------

'''
create an employee class with name,age and salary, then create some objects,after that sort the object
1-based on salary
2-based on name
3-based on age '''


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return ("{},{},{}".format(self.name,self.age, self.salary))

e1 = Employee("luna",6,200000)

e2 = Employee("ellie", 1, 100000)

e3 = Employee("tango", 4, 70000)

e4 = Employee("maverick", 9, 60000)

employees = [e1, e2, e3, e4]

sort_based_salary = sorted(employees, key = lambda x: x.salary, reverse=True)
sort_based_name = sorted(employees, key = lambda x: x.name)
sort_based_age = sorted(employees, key = lambda x: x.age)

print(sort_based_salary)
print(sort_based_name)
print(sort_based_age)


# ---------------------------------------------------------------

# example 2

# we have a list with negative and positive numbers, sort them irrespective of the negative mark

li = [-1,-2,-5,0,1,4,3,-6]
s_li = sorted(li, key = abs)
print(s_li)


