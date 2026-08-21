# 2. Bank Account Simulator
# Key Concepts: Encapsulation basics, State Modification, Methods.
# Goal: Build a `BankAccount` class with `deposit()`, `withdraw()`, and `get_balance()` methods.Ensure withdrawals fail gracefully if the requested amount exceeds the current balance.

class BankAccount:
    def __init__(self, name:str, amount:float) -> None:
        self._name = name
        self._amount = amount

    def deposit(self, amount:float) -> int:
        if amount <0:
            print("Kindly enter right amount")
            return 0
        else:
            self._amount += amount
            print(f"{amount} rupees is credited to your account. Your total balance is {self._amount:.2f}")
            return 1

    def withdraw(self, amount:float) -> int:
        if amount <0:
            print("Kindly enter right amount")
            return 0
        elif amount <= self._amount:
            self._amount -= amount
            print(f"{amount} rupees is debited from your account. Your total balance is {self._amount:.2f}")
            return 1
        else:
            print(f"Entered amount exceeds current balance. Your total balance is {self._amount:.2f}")
            return 0

    def get_balance(self) -> float:
        print(f"Account Balance: {self._amount:.2f}")
        return self._amount

#Examples:
darsh_account = BankAccount("Darsh", 100000)
darsh_account.get_balance()
darsh_account.deposit(100000)
darsh_account.get_balance()
darsh_account.withdraw(50)
darsh_account.get_balance()
darsh_account.withdraw(5.26)
darsh_account.get_balance()

shiva_account = BankAccount("Shiva", 100)
shiva_account.withdraw(101)
shiva_account.deposit(101)
shiva_account.get_balance()
shiva_account.withdraw(101)
shiva_account.get_balance()