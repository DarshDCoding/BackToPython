# 8. Custom Plugin & Logger Framework
# Key Concepts: Decorators applied to methods, Class methods as constructors, Encapsulation.
# Goal: Create an audit logging system that records function execution.
#       Implement `@classmethod` factory constructors (e.g., `Logger.from_config_file()`).
#       Create custom method decorators inside your class structure to auto-log performance or control permission access.
import datetime as dt
from functools import wraps

class Logger:

    __logs ={}
    __present_employees =set()
    __employee_shit = {}

    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_logged_in(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.name not in Logger.__present_employees:
                print(f"{self.name} is not logged in. Access denied.")
                return None
            return func(self, *args, **kwargs)

        return wrapper

    @staticmethod
    def audit_log(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            start_time = dt.datetime.now()
            result = func(self, *args, **kwargs)
            time_duration = (dt.datetime.now() - start_time).total_seconds()
            Logger.__logs[dt.datetime.now()] = (self.name, f"{func.__name__}(args={args},**kwargs={kwargs})" ,f"{time_duration:.6f}s")
            return result
        return wrapper

    @audit_log
    @is_logged_in
    def log(self, message):
        Logger.__employee_shit.setdefault(self.name, {})
        Logger.__employee_shit[self.name][dt.datetime.now()] = message

    @classmethod
    def employee_log_data(cls):
        print(f"{'Name':<10} {'Date':<10} {'Time':<20} Logs")
        for user, data in cls.__employee_shit.items():
            for time, log in data.items():
                print(f"{str(user):<10} {str(time):<30} {log}")

    @classmethod
    def get_log_info(cls):
        if cls.__logs:
            print(f"{'Date':<10} {'Time':<20} {'Person':<10} {'Action':<50} Duration")
            for time, log in cls.__logs.items():
                print(f"{str(time):<31} {str(log[0]):<10} {str(log[1]):<50} {str(log[2])}")
            return
        print("No logs present.")

    @classmethod
    def from_config_file(cls, config:dict):
        config = config or {}

        return cls(config.get("name", "DefaultEmployee"))

    @audit_log
    def login(self):
        if self.name in Logger.__present_employees:
            print(f"{self.name} is already logged in.")
            return
        print(f"{self.name} logged in.")
        Logger.__present_employees.add(self.name)

    @audit_log
    @is_logged_in
    def logout(self):
        print(f"{self.name} logged out.")
        Logger.__present_employees.remove(self.name)



#tests
darsh = Logger("Darsh")
sima = Logger("Sima")
sima.login()
darsh.login()
darsh.log("Hello")
sima.log("Hello This is Sima")

reshma = Logger.from_config_file({"name":"Reshma"})
reshma.login()
reshma.log("Hello This is Reshma")
Logger.get_log_info()
Logger.employee_log_data()