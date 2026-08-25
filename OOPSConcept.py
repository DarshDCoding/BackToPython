# # Creating Class and Constructor also a method in it.
# class Car:
#     __noOfCars =0
#
#     def __init__(self, brand:str, model:str):
#         Car.__noOfCars += 1
#         self.__brand = brand
#         self.__model = model
#
#     def display_name(self):
#         return f"{self.__brand} {self.__model}"
#
#     # Using Encapsulation
#     # Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
#
#     def get_brand(self):
#         return self.__brand
#
#     def set_brand(self, brand:str):
#         self.__brand = brand
#
#     def fuel_type(self):
#         return "Petrol/Desil"
#
#     #Add a static method to the Car class that returns a general description of a car.
#     @staticmethod #so what does this mean is, you don't have to give self argument...hence can not be accessed by instances.
#     def get_total_cars():
#         return Car.__noOfCars
#
#     #Use a property decorator in the Car class to make the model attribute read-only.
#     @property
#     def model(self):
#         return self.__model
#
#
#
#
#
#
# # Using Inheritance to creat a new class with parent properties like atrributes and methods.
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size:int):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
#
#     def fuel_type(self):
#         return "Electric Charge"
#
#
#
# # #practice
# myCar = Car("Toyota", "Corolla")
# # print(myCar.display_name())
# # print(myCar.fuel_type())
#
# myTesla = ElectricCar("Tesla", "CyberTruck", 85)
# # print(myTesla.get_brand())
# # print(myTesla.fuel_type())
#
# # print(myCar._Car__noOfCars) #I don't know what the fuck is this...but IT WORKS...
#
# # print(myTesla.get_total_cars())
# # print(myCar.model())
# # myCar.model = "some"
# # print(myCar.model)
#
# # print(isinstance(myTesla, ElectricCar))
#
# # Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
# class Battery:
#     def battery_info(self):
#         return "This is battery"
#
# class Engine:
#     def engine_info(self):
#         return "This is engine"
#
# class FullyElectricCar(Battery, Engine, Car):
#     pass
#
# my_newTesla= FullyElectricCar("Tesla", "548")
#
# print(my_newTesla.battery_info())
# print(my_newTesla.engine_info())
#
# #chutiya video....jhaat kuch seekha hu ki nahi pata nahi...par kal questions karunga...tab dekhte hai...


#custome decorators

def decorate_something(func):
    def wrapper(*args, **kwargs):
        print("Hulla la la la")
        func()
    return wrapper

def decorate_something2(func):
    def wrapper(*args, **kwargs):
        print("Hoi Hoi")
        func()
    return wrapper


@decorate_something
@decorate_something2
def something():
    print("hoi")



something()