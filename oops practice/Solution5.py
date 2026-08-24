# 5. Fleet Vehicle Management System
# Key Concepts: Polymorphism, Class Variables (`total_vehicles`), Inheritance.
# Goal: Build a base `Vehicle` class tracking a global count via a class variable. Subclass into `Car`, `ElectricCar`, and `Truck`.
#       Implement a common `get_fuel_efficiency()` method in each class that computes range differently (Polymorphism).
from operator import truediv


class Vehicle:
    __total_vehicles = 0

    def __init__(self, make:str, model:str):
        self.make = make
        self.model = model
        Vehicle.__total_vehicles += 1

    @classmethod
    def total_vehicles(cls) -> int:
        print(f"Total vehicles : {Vehicle.__total_vehicles}")
        return cls.__total_vehicles

class Car(Vehicle):
    def __init__(self, make:str,model:str, distance_per_ltr:int, fuel_amount_in_ltr:float):
        super().__init__(make, model)
        self.distance_per_ltr = distance_per_ltr
        self.fuel_amount_in_ltr = fuel_amount_in_ltr

    def get_fuel_efficiency(self) -> float:
        full_efficiency = self.fuel_amount_in_ltr * self.distance_per_ltr
        print(f"Fuel efficiency : {full_efficiency:.2f}Km")
        return full_efficiency


class ElectricCar(Vehicle):
    def __init__(self, make:str, model:str, full_battery_distance:int,  battery_percentage:int=100):
        super().__init__(make, model)
        self.full_battery_distance = full_battery_distance
        self.battery_percentage = battery_percentage

    def get_fuel_efficiency(self) -> float:
        full_efficiency = self.battery_percentage/100 * self.full_battery_distance
        print(f"Fuel efficiency : {full_efficiency:.2f}Km")
        return full_efficiency


class Truck(Vehicle):
    def __init__(self, make:str, model:str, fuel_amount_in_ltr:float, load_capacity_in_percentage:float=0.0):
        super().__init__(make, model)
        self.load_capacity_in_percentage = load_capacity_in_percentage
        self.fuel_amount_in_ltr = fuel_amount_in_ltr

    def get_fuel_efficiency(self) -> float:
        base_range = self.fuel_amount_in_ltr * 10
        load_factor = self.load_capacity_in_percentage / 100
        efficiency_multiplier = 1.0 - (load_factor * 0.5)

        full_efficiency = base_range * efficiency_multiplier
        print(f"Fuel efficiency : {full_efficiency:.2f}Km")
        return full_efficiency



# Tests:
car1 = Car("Toyota", "City", 50, 8.025)
electric_car1 = ElectricCar("Tesla", "X200", 30, 70)
truck1 = Truck("BMW", "MK42",1,1)

Vehicle.total_vehicles()
car1.get_fuel_efficiency()
electric_car1.get_fuel_efficiency()
truck1.get_fuel_efficiency()