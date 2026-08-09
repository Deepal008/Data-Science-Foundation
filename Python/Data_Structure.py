"""List"""
# Property of list:- Mutable, Duplicate, Ordered, Heterogenous

a = [12,13,14,15,16,12,15.2, True, print()]

# print(a[-2]) 


"""List Traversing"""

# 1st way using index
# for i in range(len(a)):
#     print(a[i])

# # 2nd way directly on value

# for i in a:
#     print(i)


"""Methods of List"""
# print(dir(list))
# help(list)

# l = [1,2,3,4,5]

# l.append(6)
# print(l)

# l.insert(1,0)
# print(l)


# l.remove(2)
# print(l)


# l[0] = 10
# print(l)


# Questions

# Find Positive and Negative numbers from the list
# l = [-45, 64,23,-68,34]
# print("Positive elements are")
# for i in l:
#     if i >= 0:
#         print(i)

# print("Negative elements are")

# for i in l:
#     if i <= 0:
#         print(i)


# mean in list elements

# l = [12,34,5,4,7,66,87]

# sum = 0
# for i in l:
#     sum = sum + i

# print(sum/len(l))


# Find the greatest element and print its index too
# l = [12,36,14,19,128,6,13]

# greatest = 0

# idx = 0
# for i in range(len(l)):
#     if l[i] >= greatest:
#         greatest = l[i]

#         idx = i


# print(f"Greatest element is {greatest} which is found at {idx} index")


# l = [12,36,14,19,128,6,13]

# greatest = l[0]
# sec_largest = l[0]

# idx = 0
# for i in l:
#     if i > greatest:
#         sec_largest = greatest
#         greatest = i
#     elif i > sec_largest:
#         sec_largest = i


# print(f"Greatest element is {greatest} and second greatest element is {sec_largest} ")


# check list is sorted or not
# a = [12, 13,4, 14, 15, 16]

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")

"""Tuple"""
# property of tuple :- immutable, duplicates, Ordered, Heterogenous

# a = (1,2,4,5)
 
# print(a[0])

"""Set"""
# property of set:- Mutable, Duplicates = you cant have any duplicate values in set, Unordered = you cant access them through index values, Heterogenous


# s = {1,2,3,4,5,5,4}

# print(s)


# b = hash("hello")
# print(b)


# c = hash((1,2,344))

# print(c)


# Set traversing
# for i in s:
#     print(i)

# set method
# a = {8,1,2,3,4}

# a.remove(2);
# a.pop()
# a.clear()



# a = {1,2,3,4,5,}
# b = {4,5,6,7,8}

# s = a.union(b)   #OR a|b
# s = a.intersection(b) # OR a&b
# s = a.difference(b)  #  OR a-b

# s = a^b (it removes the common element from both sets and print rest of elements)

# print(s)


"""Dictionary"""

# Property : mutable, Duplicates, ordered, Heterogenous

# d = {1:"hello", 2:56, "hello": "Deepal"}
# print(type(d))
# print(d)

# d = {10:100, 20:200, 30:300, 40:400}

# d[10] = 100  #updating
# d[50] = 500  # creating
# del d[30]    # deleting
# print(d[10])


# dictionary  traversing

# d = {10:100, 20:200, 30:300, 40:400}

# for i in d:
#     print(d[i])

    #  OR

# for i in d.values():
#     print(i)


# dectionary method

# help(dict)
# d.clear()


# a = [1,2,3,4,5]

# b = a

# b = a.copy()

# b[0] = 100

# print(b)

"""Questions"""
# Write a Python script to merge two Python dictionaries

# d1 = {10:100, 20:200, 30:300}
# d2 = {40:400, 50:500, 60:600}

# for i in d2:
#     d1[i] = d2[i]

# # print(d1)



# d1 = {10:100, 20:200, 30:300}
# sum = 0

# for i in d1:
#     sum = sum + d1[i]

# print(sum)



# Q: Count the frequency of each elements in List

# a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]

# d = {}

# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d)


# WAP to combine two dictionary by adding values for common keys.

d1 = {10:100, 20:200, 30:300, 40: 300}
d2 = {40:400, 50:500, 60:600}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print(d1)