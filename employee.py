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