"""Keywords"""
# try : Wrap the block of code that might cause an exception.

# except : Handle the exception if it occurs

# else : Run code only if no exception occurs

# finally : Run code no matter what whether there's an exception or not

# raise : Manually throw an exception

# a = int(input("Enter a number: "))

# try:
#     print(10/a)
# except Exception as err:
#     print(f"sorry there is an err as {err}")

# else:
#     print("good there is no exception")

# finally:
#     print("I will run no matter what")

# print("ok i have done the division")

age = int(input("tell your age : "))

try:
    if age < 10 or age > 18:
        raise valueError("Your age must be between 10 and 18")
    else:
        print("Welcome to the club")
        
except Exception as err:
    print(f"an error occured as {err}")


print("the club will start soon")