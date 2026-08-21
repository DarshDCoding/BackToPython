# Digital Library Book Tracker
# Key Concepts: Basic Class definition, Constructor(`__init__`), Attributes, Instance Methods.
# Goal: Create a `Book` class to track availability. Include methods like `borrow_book()` and `return_book()`, which modify internal state attributes (e.g., `is_available`).

class Book:
    def __init__(self, title:str, quantity:int ,max_quantity:int):
        self.title = title
        self._quantity = quantity
        self._max_quantity = max_quantity

    @property
    def is_available(self) -> bool:
        return self._quantity > 0

    def borrow_book(self) -> int:
        if self._quantity > 0:
            self._quantity -= 1
            print("Book Borrowed.")
            return 1
        else:
            print("Book is not available.")
            return 0

    def return_book(self) -> int:
        if self._quantity < self._max_quantity:
            self._quantity += 1
            print("Book Returned.")
            return 1
        else:
            print("All Books are present.")
            return 0

    def status(self):
        print(f'Book Status: {f"{self._quantity} are Available" if self.is_available else "Not Available"}')



# Examples:
ikigai = Book("Ikigai", 5, 10)
atomic_habits = Book("Atomic Habits", 4, 10)

ikigai.status()
ikigai.return_book()
ikigai.return_book()
ikigai.return_book()
ikigai.return_book()
ikigai.return_book()
ikigai.return_book()
ikigai.status()
atomic_habits.status()
