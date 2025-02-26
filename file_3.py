import json
from datetime import datetime

# models/employee.py
class Employee:
    def __init__(self, full_name, position, phone, email):
        self.full_name = full_name
        self.position = position
        self.phone = phone
        self.email = email

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Employee(**data)

# models/book.py
class Book:
    def __init__(self, title, year, author, genre, cost_price, sale_price):
        self.title = title
        self.year = year
        self.author = author
        self.genre = genre
        self.cost_price = cost_price
        self.sale_price = sale_price

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Book(**data)

# models/sale.py
class Sale:
    def __init__(self, employee, book, sale_price, date=None):
        self.employee = employee.full_name
        self.book = book.title
        self.sale_price = sale_price
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Sale(Employee(data['employee'], '', '', ''), Book(data['book'], 0, '', '', 0, 0), data['sale_price'], data['date'])

# services/data_manager.py
class DataManager:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.data = {"employees": [], "books": [], "sales": []}
        self.load_data()

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {"employees": [], "books": [], "sales": []}

    def add_employee(self, employee):
        self.data["employees"].append(employee.to_dict())
        self.save_data()

    def add_book(self, book):
        self.data["books"].append(book.to_dict())
        self.save_data()

    def add_sale(self, sale):
        self.data["sales"].append(sale.to_dict())
        self.save_data()

# services/sales_manager.py
class SalesManager:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def total_revenue(self):
        return sum(sale["sale_price"] for sale in self.data_manager.data["sales"])

# main.py
if __name__ == "__main__":
    dm = DataManager()
    sales_manager = SalesManager(dm)

    emp1 = Employee("Ivan Ivanov", "Salesman", "123456789", "ivan@mail.com")
    book1 = Book("Python for everyone", 2022, "Guido van Rossum", "Programming", 500, 1000)

    dm.add_employee(emp1)
    dm.add_book(book1)
    dm.add_sale(Sale(emp1, book1, 950))

    print(f"Total revenue: {sales_manager.total_revenue()} UAH")