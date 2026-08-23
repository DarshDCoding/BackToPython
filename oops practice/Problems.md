# Python OOP Practice Projects Checklist

## Easy Projects
*Focus: Classes, `self`, `__init__`, Instance Methods*

- [x] **1. Digital Library Book Tracker**
  - **Key Concepts:** Basic Class definition, Constructor (`__init__`), Attributes, Instance Methods.
  - **Goal:** Create a `Book` class to track availability. Include methods like `borrow_book()` and `return_book()`, which modify internal state attributes (e.g., `is_available`).
  - **Solution:** [Click here](https://github.com/DarshDCoding/BackToPython/blob/main/oops%20practice/Solution1.py)

- [x] **2. Bank Account Simulator**
  - **Key Concepts:** Encapsulation basics, State Modification, Methods.
  - **Goal:** Build a `BankAccount` class with `deposit()`, `withdraw()`, and `get_balance()` methods. Ensure withdrawals fail gracefully if the requested amount exceeds the current balance.
  - **Solution:** [Click here](https://github.com/DarshDCoding/BackToPython/blob/main/oops%20practice/Solution2.py)

- [x] **3. Digital Student Gradebook**
  - **Key Concepts:** Attributes holding collections (lists/dictionaries), Instance Methods, Logic calculations inside classes.
  - **Goal:** Create a `Student` class that stores grades in a list. Write methods to `add_grade()`, calculate the average, and determine a pass/fail status based on threshold logic.
  - **Solution:** [Click here](https://github.com/DarshDCoding/BackToPython/blob/main/oops%20practice/Solution3.py)

---

## Medium Projects
*Focus: Inheritance, Encapsulation, Class/Static Methods*

- [x] **4. E-Commerce Product Catalog & Cart System**
  - **Key Concepts:** Class Inheritance (`Product` -> `ElectronicsProduct`, `ClothingProduct`), Private attributes (`__price`), Getters/Setters with `@property`.
  - **Goal:** Create a base class `Product` with encapsulated prices. Extend it into specific sub-classes that add unique attributes (e.g., warranty length or clothing size). Build a `ShoppingCart` class that accepts `Product` instances and calculates total tax.
  - **Solution:** [Click here](https://github.com/DarshDCoding/BackToPython/blob/main/oops%20practice/Solution4.py)

- [ ] **5. Fleet Vehicle Management System**
  - **Key Concepts:** Polymorphism, Class Variables (`total_vehicles`), Inheritance.
  - **Goal:** Build a base `Vehicle` class tracking a global count via a class variable. Subclass into `Car`, `ElectricCar`, and `Truck`. Implement a common `get_fuel_efficiency()` method in each class that computes range differently (Polymorphism).

- [ ] **6. Employee Payroll Manager**
  - **Key Concepts:** Polymorphism, `@staticmethod`, Method Overriding.
  - **Goal:** Implement `FullTimeEmployee` and `ContractEmployee` inheriting from a base `Employee` class. Override `calculate_salary()` for both. Add `@staticmethod` helpers to validate tax IDs or format payroll output.

---

## Hard Projects
*Focus: Multiple Inheritance, Decorators, Property Validation, Composition*

- [ ] **7. Smart Home Automation Engine**
  - **Key Concepts:** Multiple Inheritance, Mixins, Property Decorators.
  - **Goal:** Create standalone mixin classes like `WiFiConnectedMixin` and `BatteryPoweredMixin`. Combine these with base device classes (`Light`, `Thermostat`) to create hybrid devices (e.g., `SmartThermostat`). Use `@property` getters and setters with validation logic to restrict device settings (e.g., temperature limits).

- [ ] **8. Custom Plugin & Logger Framework**
  - **Key Concepts:** Decorators applied to methods, Class methods as constructors, Encapsulation.
  - **Goal:** Create an audit logging system that records function execution. Implement `@classmethod` factory constructors (e.g., `Logger.from_config_file()`). Create custom method decorators inside your class structure to auto-log performance or control permission access.

- [ ] **9. Role-Based Access Control (RBAC) & Authentication System**
  - **Key Concepts:** Composition, Encapsulation, Dynamic Properties, Inheritance.
  - **Goal:** Design a system with `User`, `Role`, and `Permission` classes. Use composition (a `User` *has a* `Role`, which *has* `Permissions`). Protect password attributes using private variables with secure hashing routines via property decorators, ensuring lower-tier roles cannot escalate permissions.