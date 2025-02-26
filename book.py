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