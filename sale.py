from datetime import datetime

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