a = "sher coder"
# a[start : stop : steps]
print(a[0:4:2])
# print(a[5::]) 



"""Type Conversion"""

# a = 12 
# a = str(a)
# print(type(a)) 

# a = "27"
# a = int(a)
# print(a)

# a = 0
# print(bool(a))


"""Formated String"""
# name = "Deepal"
# age = '22'

# print(name, age)

# print("hello my name is ", name, "and my age is", age)

# print(f"my name is {name} and my age is {age}")


"""Taking Input"""
# age = int(input("hellow what is you age"))
# print(type(age))


"""Arithmetic operation"""

# a = 12
# b = 20

# print(a+b)
# print(b-a)
# print(a*b)

# print(b/a)
# print(b//a)

# print(5**3)

# print(32%5)

# print(12+4/2)  BODOMAS


"""Assignment operator"""

# a = 20
# print()

"""Compound assignment operations/ """

# a = 20
# a=a+20
# a = a+40
# print(a)


"""Comparision operator"""
# a = 12
# b = 12
# print(a == b)
# print(a!=b)


# print(a > b)
# print(45<=79)


"""ord function for ASCII numbers"""
# print(ord("a"))
# print(ord("A"))
# print(ord("B"))
# print("A" > "B")

# print("ABC" > "ACD")

"""Logical operatior"""
# print(123 > 100 and 34 == 34 and 45 < 90)

# print(12 != 12 or 23== 45 or 67 == 57 or 10>5)

# print(not 12 == 12)

"""Conditional Statement"""
# a = 13

# if a > 10:
#     print("I will do task A")
# else:
#     print("I will do task B")


# money = int(input("please provide me the money :- "))

# if money == 10:
#     print("I will have a choco bar icecream")
# elif money == 20:
#     print("I will have a mangodolly")
# else:
#     print("I will have a cone")

# name = input("Enter your name:- ")
# age = int(input("Enter your age:- "))

# if age >= 18:
#     print("You are a valid voter")
# else:
#     print("You are not a valid voter")

year = int(input("Enter year"))

if year%100 == 0 and year%400 == 0:
   print("Its a leap year")
elif year%100 != 0 and year%4 == 0:
  print("Its a leap year")
else:
   print("its a normal year")
  