from car import Car
from developer import Developer
from manager import Manager
from book import Book

car = Car("Peugeot 308", "Silver", 130, 4)
print(car.model)

dev = Developer("Yasin", "Kucuker", 1, 450000, ["English", "Spanish"])
dev.add_language("French")
dev.raise_salary(150000)
dev.show_info()

mgr = Manager("Yasin", 550000, "Board Member", 250)
mgr.raise_salary(50000)
mgr.show_info()

book = Book("Istanbul Memories", "Author Name", 543, "Crime")
print(book)
print(len(book))
