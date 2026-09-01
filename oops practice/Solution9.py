# 9. Role-Based Access Control (RBAC) & Authentication System**
# Key Concepts: Composition, Encapsulation, Dynamic Properties, Inheritance.
# Goal: Design a system with `User`, `Role`, and `Permission` classes.
#       Use composition (a `User` *has a* `Role`, which *has* `Permissions`).
#       Protect password attributes using private variables with secure hashing routines via property decorators, ensuring lower-tier roles cannot escalate permissions.
from functools import wraps
import bcrypt


class Permission:
    def __init__(self):
        pass

    @staticmethod
    def print_in_permission():
        print("We are in permission")

    @staticmethod
    def login_employee(data:dict):
        print(f"{data['name']} logged in.")
        return Employee(data=data)

    @staticmethod
    def has_password(password:str, rounds=12) -> bytes:
        pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds))
        return pwd

    @staticmethod
    def check_pwd(password:str, hash:bytes) -> bool:
        return bcrypt.checkpw(password.encode(), hash)

    @staticmethod
    def add_data(role:str, data:dict):
        current_employee_data = Employee.get_data(role=role, admin_password="DarshD.Admin")
        # current_employee_data.append(data)
        id = data["id"]
        name = data["name"]
        password = Permission.has_password(data["password"])
        salary = data["salary"]
        role = data["role"]
        manager_id = data["manager_id"]
        of = data["of"]

        current_employee_data.append({"id":id, "name":name, "password": password, "salary":salary, "role":role, "manager_id":manager_id, "of":of})

        Employee.set_data(data=current_employee_data, role=role, admin_password="DarshD.Admin")
        return Employee.get_data(role=role, admin_password="DarshD.Admin")

    @staticmethod
    def add_new_employee(data:dict):
        if data["role"] == "Hr":
            return Permission.add_data(role="Hr", data=data)
        elif data["role"] == "Manager":
            return Permission.add_data(role="Manager", data=data)
        elif data["role"] == "Worker":
            return Permission.add_data(role="Worker", data=data)
        else:
            return None


class Role:
    def __init__(self,role):
        self.__emp_role = role
        self.permission= Permission()

    @staticmethod
    def is_role(role:str):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.__emp_role == role:
                    return func(self, *args, **kwargs)
                else:
                    print(f"You are not {role}. Access Denied")
                return False
            return wrapper
        return decorator

    @staticmethod
    def is_admin(admin_password:str):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if admin_password == Employee.get_admin_password("DarshD.Admin"):
                    return func(self, *args, **kwargs)
                else:
                    print("You are not Admin. Access Denied")
                    return False
            return wrapper
        return decorator

    # @is_admin("DarshD.Admin")
    def login_emp(self, data:dict):
        return self.permission.login_employee(data=data)

    @is_admin("DarshD.Admin")
    @is_role("Hr")
    def add_employee(self,data):
        Permission.add_new_employee(data)

    def get_emp_role(self):
        return self.__emp_role


class Employee:
    __admin_password = "DarshD.Admin"
    __managers = [
        {
            "id": "Manager#01",
            "name": "Darsh",
            "password": "DarshKaPassword@54",
            "salary": 150000,
            "role": "Manager",
            "manager_id": None,
            "of": {"Hr#1"}
        }
    ]
    __hrs = [{
        "id":"Hr#1",
        "name":"Raju",
        "password":"Raju#01",
        "salary":50000,
        "role":"Hr",
        "manager_id":"Admin",
        "of":set()
    }]
    __workers = []

    def __init__(self, data:dict):
        self.__id = data["id"]
        self.__name = data["name"]
        self.__password = data["password"]
        self.__salary = data["salary"]
        self.__role = Role(data["role"])
        self.__manager_id = data["manager_id"]
        self.__of = data["of"]

    def get_my_data(self):
        return [self.__id, self.__name, self.__salary, self.__role, self.__manager_id, self.__of]

    @classmethod #Getter
    def get_data(cls, role:str, admin_password:str):
        if admin_password != cls.__admin_password:
            print("You are not admin. Access Denied")
            return []

        if role == "Hr":
            return cls.__hrs
        elif role == "Manager":
            return cls.__managers
        elif role == "Worker":
            return cls.__workers
        else:
            return []

    @property
    def password(self):
        return self.__password


    @classmethod #Setter
    def set_data(cls,data:list, role:str, admin_password:str):
        if admin_password != cls.__admin_password:
            print("You are not admin. Access Denied")
            return None
        if role == "Hr":
            cls.__hrs = data
            return 1
        elif role == "Manager":
            cls.__managers = data
            return 2
        elif role == "Worker":
            cls.__workers = data
            return 3
        else:
            return None

    @classmethod
    def set_admin_password(cls, old_password:str, new_password:str):
        if old_password != cls.__admin_password:
            print("Old Password mismatch")
            return None
        else:
            cls.__admin_password = new_password
            return f"Password changed successfully"

    @classmethod
    def get_admin_password(cls, admin_password:str):
        if admin_password != cls.__admin_password:
            return "Password mismatch"
        return cls.__admin_password

    def add_new_employee(self, data:dict):
        self.__role.add_employee(data=data)



class Hr(Employee):
    __role = Role("Hr")
    def __init__(self, data:dict):
        super().__init__(data)

    @classmethod
    def login(cls, emp_id:str, password:str):
        data = Employee.get_data("Hr", "DarshD.Admin")
        for hr in data:
            if emp_id == hr["id"]:
                if password == hr["password"]:
                    return cls.__role.login_emp(hr)
                else:
                    print("password mismatch")
                    continue
        print("Employee Not Found")
        return None

class Manager(Employee):
    __role = Role("Manager")
    def __init__(self, data:dict):
        super().__init__(data)

    @classmethod
    def login(cls, emp_id:str, password:str):
        data = Employee.get_data("Manager", "DarshD.Admin")
        for manager in data:
            if emp_id == manager["id"]:
                if password == manager["password"]:
                    return cls.__role.login_emp(manager)
                else:
                    print("password mismatch")
                    continue
        print("Employee Not Found")
        return None

class Worker(Employee):
    __role = Role("Worker")
    def __init__(self, data:dict):
        super().__init__(data)

    @classmethod
    def login(cls, emp_id:str, password:str):
        data = Employee.get_data("Worker", "DarshD.Admin")
        for worker in data:
            if emp_id == worker["id"]:
                if Permission.check_pwd(password, worker["password"]):
                    return cls.__role.login_emp(worker)
                else:
                    print("password mismatch")
                    continue
        print("Employee Not Found")
        return None

Darsh = Manager.login("Manager#01", "DarshKaPassword@54")
Raju = Hr.login("Hr#1", "Raju#01")

Raju.add_new_employee({"id":"worker#01", "name":"Raju", "password":"RajuKaKaju", "salary":25000, "role":"Worker", "manager_id":"Manager#01", "of":"Hr#01"})

Sumit = Worker.login("worker#01", "RajuKaKaju")
print(Employee.get_data("Worker", "DarshD.Admin"))
Sumit.add_new_employee({"id":"worker#01", "name":"Raju", "password":"RajuKaKaju", "salary":25000, "role":"Worker", "manager_id":"Manager#01", "of":"Hr#01"})
