mylist = [1, 2, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1, 2, 3]

def sort_list(mylist):
    for i in range(len(mylist)):
        for j in range(i+1, len(mylist)):
            if mylist[i]>mylist[j]:
                mylist[i],mylist[j] = mylist[j],mylist[i]
    return mylist

print(sort_list(mylist))

# -----------------------------------------------
# using sort & sorted:

nums = [3,4,2,1,4,5,6,7,3,0]

nums.sort()
print(nums)

x = sorted(nums)
print(x)

