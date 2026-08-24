
"""Decorator"""

# class Animal:
#     @property
#     def show(self):
#         print("hello how are you")

# obj = Animal()

# obj.show



# def decorate(func):
#     def wrapper():
#         print("I will print my self before the function")
#         func()
#         print("I will print after the function")
#     return wrapper


# @decorate
# def hello():
#     print("hello I am deepal yadav")

# hello()



# def decorate(func):
#     def wrapper(a,b):
#         print("the addition to your numbers are ")
#         func(a,b)
#         print("thankyou I hope you liked it ")
#     return wrapper



# @decorate
# def addition(a, b):
#     print(f"your total is {a+b}")

# addition(12, 67)


"""Args and Kwargs"""


#Args: it takes arguments in a tuple form.
# def addition(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i


#     print(sum)

# addition(12, 12, 23, 56)



#kwargs: it take keywords argument in dictionary form
# def information(**kwargs):
#     print(kwargs)

# information(name = "Deepal", age = 23, designation = "AI/ML")

# def information(**kwargs):
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

# information(name = "Deepal", age = 23, designation = "AI/ML")


# def decorate(func):
#     def wrapper(*args,**kwargs):
#         print("the addition to your numbers are ")
#         func(*args,**kwargs)
#         print("thankyou I hope you liked it ")
#     return wrapper



# @decorate
# def addition(a, b):
#     print(f"your total is {a+b}")

# addition(12, 6)


"""List, Dictionary and Set Comprehensions"""


# l = [i for i in range(1,21) if i % 2 == 0]

# print(l)

# #Dictionary

# l = {i : i**2 for i in range(1,10) if i % 2 == 0}

# print(l)


"""lambda function"""

# addition = lambda a,b : a+b

# print(addition(12,13))



# evenOdd = lambda a : "even" if a%2 == 0 else "odd"

# print(evenOdd(12)) 

"""Map, filter and zip"""

#map
a = [1,2,3,4,5]

# result = map(lambda x : x*2, a)

# OR

# def double(x):
#     return x*2 

# result = map(double, a)


# print(list(result))


#filter
a = [1,2,3,4,5,6,7,8,9]


# result = filter(lambda x: x%2 == 0, a)
# result = filter(lambda x: True if  x%2==0 else False, a)

# OR
# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# result = filter(even, a)

# print(list(result))

