# 6. Employee Payroll Manager
# Key Concepts: Polymorphism, `@staticmethod`, Method Overriding.
# Goal: Implement `FullTimeEmployee` and `ContractEmployee` inheriting from a base `Employee` class. Override `calculate_salary()` for both.
#       Add `@staticmethod` helpers to validate tax IDs or format payroll output.
from typing import override

class Employee:
    def __init__(self,name:str, employee_id:int, salary:float):
        self.name = name
        self.id = employee_id
        self.salary = salary

    @staticmethod
    def format_salary(employee_id:int, salary:float) -> str:
        """formatting salary"""
        return f"Employee Id:{employee_id} Salary: {salary}"

    def calculate_salary(self, total_working_days:int):
        return total_working_days * self.salary



class FullTimeEmployee(Employee):
    def __init__(self, name:str, employee_id:int, salary:float):
        super().__init__(name, employee_id, salary)

    @override
    def calculate_salary(self, total_working_days):
        salary = total_working_days * self.salary
        print(Employee.format_salary(self.id, salary))
        return salary

class ContractEmployee(Employee):
    def __init__(self, name:str, employee_id:int, salary:float, contract_period_in_month:int):
        super().__init__(name, employee_id, salary)
        self._contract_period = contract_period_in_month

    @override
    def calculate_salary(self, total_working_days) -> float:

        if self._contract_period >0:
            salary = total_working_days * self.salary
            print(f"{Employee.format_salary(self.id, salary)}, Contract Ends in {self._contract_period} months")
            self._contract_period -= 1
            return salary
        else:
            print("Your Contract Period has ended.")
            return 0

#Testing....
#Yes I could have added a filter like days couldn't be more than 31 for salary days. or overtime kind of things...but ehh I don't have mood to do it right now...

employ1 = ContractEmployee("Employee 1", 1, 10, 5)
employ2 = FullTimeEmployee("Employee 2", 2, 10)

employ1.calculate_salary(100)
employ2.calculate_salary(100)