# range(start, stop, steps)

# a = range(1,21,2)
# for i in a:
#     print(i)

# for i in range(16, 0, -1):
#     print(i)

# for i in range(-5, -16, -1):
#     print(i)

# for i in range(5, 51, 5):   #table of 5
#     print(i).

# n = int(input("Which table you want ?"))

# for i in range(n, (n*10)+1, n):
#     print(i)


"""Loops for strings"""
# a= "SHERYIANS TEACHES INDUSTRY THINGS"
# print(len(a))
# # print(a[4])

# for i in range(len(a)):
#     print(a[i])

# a = "SHERYIANS IS COOL"
# for i in a:
#     print(i)



# """Break and Continue"""
# for i in range(1,21):
#     if i == 150:
#         print("Break statement executed")
#         break
#     else:
#         print(i)

# else:
#     print("Break statement is not executed")


# for i in range(1,21):
#     if i == 15:
#         continue
#     else:
#         print(i)5


"""Questions"""

# n = int(input("please tell your number"))
# for i in range(n):
#     print("hello world")

# n = int(input("Enter the number: "))
# for i in range(n , 0, -1):
#     print(i)


# n = int(input("Enter the number: "))

# for i in range(1, 11):
#     print(f"{n}*{i} = {n*i}")

# sum = 0
# for i in range(5):
#     sum = sum +i

# print(f"your sum is {sum}")

# n = int(input("Enter the number"))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i

# print(f"your factorial is {fact}")



# n = int(input("tell your number :- ")) 
# odd = 0
# even = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         even = even + i
#     else:
#         odd = odd + i

# print(f"Even: {even} and odd: {odd}")



# n = int(input("Enter number factors you want : "))

# count = 0

# for i in range (1, n+1):
#     if n%i == 0:
#         count = count + 1


# if count == 2:
#     print("your number is prime")
# else:
# #     print("your number is not prime")


# a = "NAMAN"
# b = "  "                
# # print(a+b)

# for i in range(len(a)-1, -1,-1):
#     b = b + a[i]

# print(b)

# if b == a:
#     print("your string is palindrome")
# else:
#     print("its nota a palindrome")


# a = "sdfsongn1234532!@#$^$#^$"

# char = 0
# dig = 0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         dig += 1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr += 1

# print(f"your digits are {dig}\nyour alphabets are {char}\nyour special characters are {spchr}")



# Directory for strings
# print(dir(int))

"""while Loop"""

# a = 1
# while a <= 30:
#     print(a)
#     a = a+1


# a = int(input("tell your number"))
# rev = 0

# original = a

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# # palindrome
# if original == rev :
#     print("number is palindromic")
# else:
#     print("number is not palindromic")


"""Guessing number Game"""

import random

num = random.randint(1,11)

tries = 0

while True:
    guess = int(input("Enter your number to guess"))

    if num == guess:
        tries += 1
        print("Congratulations!, you are right")
    
    elif num < guess:
        print("Too high! guess again")

    elif num > guess:
        print("Too low! guess again")

    else:
        tries += 1
        print("sorry you are wrong")

         