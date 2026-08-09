# def hello():
#     print("this is a hello function so i am doing hello")

# hello()

"""Function for sum"""
# def sum(a,b):
#     print(f"The sum of you number is {a+b}")

# sum(12,12)


"""Positional, Default and Keyword argument"""

# Positional Argument
# def hello(name, age):
#     print(f"your name is {name} and your age is {age}")

# hello("Deepal", 22)


# # Keyword Argument
# def sum(a, b = 45):
#     print(f"sum is {a+b}")

# sum(5)


# # Default Argument
# def hello(name, age):
#     print(f"your name is {name} and your age is {age}")

# hello(age = 22, name = "Deepal")

# question

# def palindrome(st):
#     rev = ""
#     for i in range (len(st)-1,-1,-1):
#         rev = rev +st[i]

#     if rev == st:
#         print("Palindrome")
#     else:
#         print(f"{st} is not a palindrome")

# palindrome("NAMAN")
# palindrome("deepal")


"""Return function"""

def hello():
    return "hello, how are you"

print(hello())