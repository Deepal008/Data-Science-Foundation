# class Factory:
#     a = 12

#     def hello(self):
#         print("hello, how are you")

#     print("hello, i am getting initialized")

# print(Factory().a)



# class Factory:
#     def __init__(self, material, zips, pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets

#     def show(self):
#         print(f"your object deatails are {self.material}, {self.pockets}, {self.zips}")
        

# reebok = Factory("leather", 3, 2)
# campus = Factory("nylon", 3, 3)

# reebok.show()


"""Attributes  And Methods"""
# class Animal:
#     name = "lion"  #class attribute

#     def __init__(self, age):
#         self.age = age  #instance attribute

#     def show(self):  #instance method
#         print(f"how are you, your age is {self.age}")

#     @classmethod     #class method
#     def hello(cls):
#         print("how are you brother")

#     @staticmethod    #static method
#     def static():
#         print("i am good")


# obj = Animal(12)

# obj.show()
# obj.hello() 
# obj.static()



"""Inheritance"""

# class Factory:    #parent class/ superclass
#     a = "I am an attribute mentioned inside Factory"
#     def hello(self):
#         print("hello I am a method mentioned inside Factory")

# class Factorypune(Factory):   #child class/ subclass
#     pass  


# obj = Factory()
# print(obj.a)

# obj2 = Factorypune()

# obj2.hello()


"""Constructor in Inheritance"""

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"hello your name is {self.name}")

# class Human(Animal):
#     pass

# animal1 = Animal("Lion")
# animal1.show()

# person1 = Human("akarsh")
# person1.show()




# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"hello your name is {self.name}")

# class Human(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def show(self):
#         print(f"hello your name is{self.name} and your age is {self.age}")
    

# animal1 = Animal("lion")


# person1 = Human("Deepal yadav", 22)

# person1.show()



"""Type of Inheritace"""
# 1 - Single Inheritance
# 2 - Multiple Inheritance
# 3 - Multilevel Inheritance

"""Multiple Inheritance"""

# class Animal:
#     def __init__(self, name):
#         pass

# class Human:
#     def __init__(self, name, age):
#         pass

# class Robots(Human, Animal):
#     name3 = "Charlie123"

# obj =  Robots("deepal yadav", 34)



"""Multilevel Inheritance"""

# class Factory:
#     def __init__(self, material, zips):
#         self.material = material
#         self.zips = zips

# class BhopalFactory(Factory):
#     def __init__(self, material, zips, color):
#         super().__init__(material, zips)
#         self.color = color

# class PuneFactory(BhopalFactory):
#     def __init__(self, material, zips, color, pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets


# obj = PuneFactory( )




"""Polymorphism"""

"""Method Overriding"""
# if you have one class and that is a parent class and you have another class 
# that is child class , Parent class and child class have a method that is
# same, if the object is calling, the method will be called our child class 

# class Animal:
#     def show(self):
#         print("hello I am akarsh")

# class Human(Animal):
#     def show(self):
#         print("how are you")

# obj = Human()

# obj.show()



"""Duck Typing"""

# class Animal:
#     def show(self):
#         print("I am showing")

# class Human:
#     def show(self):
#         print("Hello, I am also showing")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()

"""Encapsulation"""


"""public"""
# class Factory:
#     a = "pune"

#     def show(self):
#         print("hellow I am a pune Factory")

# class Bhopal(Factory):
#     def show2(self):
#         print(super().a)

# obj = Bhopal()
# obj.show2()

"""Protected"""

# class Factory:
#     _a = "pune"

#     def _show(self):
#         print("hellow I am a pune Factory")

# class Bhopal(Factory):
#     def show2(self):
#         print(super()._a)

# obj = Bhopal()
# obj.show2()

"""Private"""

# class Factory:
#     __a = "pune"

#     def show(self):
#         print(Factory.__a)


# obj = Factory()
# obj.show()

# class Demo:
#     def __init__(self):
#         self.name = "Public Member"
#         self._age = 21
#         self.__Salary = 50000

#     def show(self):
#         print("Inside the class:")
#         print("Public: ", self.name)           #public
#         print("Protected: ", self._age)        #protected
#         print("Private: ", self.__Salary)      #private

# obj = Demo()

# obj.show()



"""Abstraction"""

# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass

#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
#     def __init__(self, side):
#         self.side = side

#     def perimeter(self):
#             print("I have created")
    
#     def area(self):
#         print("I have created this")

    
# class Circle(abstract):
#     def __init__(self, radius):
#         self.radius = radius

#     def perimeter(self):
#         print("I have created")

#     def area(self):
#         print("I have created this")


# obj = Circle(9)
# obj2 = Square(4)


"""Dunder method"""

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"hello how are you and you name is {self.name}"

#     def __add__(self, other):
#         sum = 0
#         for i in other:
#             sum = sum + i.age

#         return f"your sum of ages are {self.age + sum}"


# obj = Animal("lion", 12)
# obj2 = Animal("dolphin", 14)
# obj3 = Animal("tiger", 34)

# print(obj + (obj2, obj3))

# print(obj)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"My name is {self.name}"


# p = Person("Deepal")
# # print(p.name)
# print(p)