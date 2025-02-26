# save manger
import json  # Импортируем модуль json для работы с JSON-данными (сохранение и загрузка).

class DataManager:
    def __init__(self, filename="data.json"):
        # Конструктор класса DataManager. По умолчанию файл для данных называется "data.json".
        # Здесь мы создаём структуру данных, которая будет содержать 3 ключа: "employees", "books", "sales".
        self.filename = filename  # Имя файла, в котором будут храниться данные
        self.data = {"employees": [], "books": [], "sales": []}  # Структура данных с тремя пустыми списками
        self.load_data()  # Загружаем данные из файла при инициализации объекта

    def save_data(self):
        # Метод для сохранения данных в файл в формате JSON.
        # Данные из self.data записываются в файл, указанном в self.filename.
        with open(self.filename, "w") as f:
            # json.dump записывает данные в файл, indent=4 форматирует вывод с отступами.
            json.dump(self.data, f, indent=4)

    def load_data(self):
        # Метод для загрузки данных из JSON-файла.
        # Если файл не найден, создаётся пустая база данных с тремя списками.
        try:
            with open(self.filename, "r") as f:
                # Если файл существует, загружаем данные.
                self.data = json.load(f)
        except FileNotFoundError:
            # Если файл не найден, создаём пустую структуру данных.
            self.data = {"employees": [], "books": [], "sales": []}

    def add_employee(self, employee):
        # Метод для добавления нового сотрудника.
        # Добавляем сотрудника в список "employees" и сохраняем изменения в файл.
        self.data["employees"].append(employee.to_dict())  # employee.to_dict() конвертирует объект в словарь
        self.save_data()  # Сохраняем изменения в файл

    def add_book(self, book):
        # Метод для добавления новой книги.
        # Добавляем книгу в список "books" и сохраняем изменения в файл.
        self.data["books"].append(book.to_dict())  # book.to_dict() конвертирует объект книги в словарь
        self.save_data()  # Сохраняем изменения в файл

    def add_sale(self, sale):
        # Метод для добавления новой продажи.
        # Добавляем информацию о продаже в список "sales" и сохраняем изменения в файл.
        self.data["sales"].append(sale.to_dict())  # sale.to_dict() конвертирует объект продажи в словарь
        self.save_data()  # Сохраняем изменения в файл
