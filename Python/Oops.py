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
class Animal:
    name = "lion"  #class attribute

    def __init__(self, age):
        self.age = age  #instance attribute

    def show(self):  #instance method
        print(f"how are you, your age is {self.age}")

    @classmethod     #class method
    def hello(cls):
        print("how are you brother")

    @staticmethod    #static method
    def static():
        print("i am good")


obj = Animal(12)

obj.show()
obj.hello() 
obj.static()



"""Inheritance"""

class Factory:    #parent class/ superclass
    a = "I am an attribute mentioned inside Factory"
    def hello(self):
        print("hello I am a method mentioned inside Factory")

class Factorypune(Factory):   #child class/ subclass
    pass  