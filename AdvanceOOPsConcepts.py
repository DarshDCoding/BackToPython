# Topics Covered:
# @classmethod as Constructor

class Employee:
    user_data =[]
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.user_data.append({'Name': self.name, 'Salary': self.salary})

    @classmethod
    def add_new(cls, data:dict):
        return cls(data.get("Name", "DefaultEmployee"), data.get('Salary', 0))

    @classmethod
    def get_all_employees(cls):
        if cls.user_data:
            print (f"{'Name':<20} {'Salary':<10}")
            for user in cls.user_data:
                print(f"{str(user['Name']):<20} {str(user['Salary']):<10}")

        return Employee.user_data

    def __str__(self):
        return f'{self.name}, {self.salary}'

employee1 = Employee.add_new({"Name": "Darsh", "Salary": 55000})
employee2 = Employee.add_new({"Name": "Darsh", "Salary": 60000})
employee3= Employee.add_new({"Name": "Darsh", "Salary": 65000})
employee4 = Employee("Hema", 5000)
rekha = Employee("Rekha", 5000)
Jaya = Employee("Jaya", 5000)
Shushma = Employee("Shushma", 5000)
employee5 = Employee.add_new({"Salary":500})

print(Employee.get_all_employees())