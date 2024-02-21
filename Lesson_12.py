# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#
#     def cat_sound (self):
#         return "meow"
#
#     def __str__(self):
#         # return f"Hi, my {self.name =}"
#         return f"Hi, my name in {self.name}, I'm {self.age} years old {self.color} cat"
#
#     def __repr__(self):
#         # return f"Hi, my {self.name =}"
#         return f"Cat: {self.name}, Age: {self.age} color: {self.color}"
#
#
# cat_1 = Cat("Barsik", 5, "black")
# cat_2 = Cat("Murzik", 3, "white")
#
# cat_list = [cat_1, cat_2]
# print(cat_list)


class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"Phone {self.brand}, {self.model}, {self.price}"


phone_1 = Phone('Samsung','A52', 7000)
phone_2 = Phone('Samsung','S11', 37000)
phone_3 = Phone('Samsung','A12', 4000)
phone_4 = Phone('Xiaomi','Redmi Note 11', 8700)
phone_5 = Phone('Xiaomi','Mi 12 Lite', 17000)

# print(hash(phone_1), hash(phone_2))


class Warehouse:
    def __init__(self, address):
        self.address = address
        self.storage = {}

    def add_to_storage(self, item, value):
        """adding item to the storage"""
        self.storage[item] = value

    def get_item_value(self, item):
        """Getting amount of the item in the storage"""
        return self.storage.get(item)

    def get_total_value(self):
        """Getting total value of the storage"""
        total = 0
        for key, cnt in self.storage.items():
            total += key.price * cnt
        return total

    def remove_form_storage(self, item):
        """adding item to the storage"""
        value = self.storage.pop(item, None)
        return value

    def __str__(self):
        """getting storage info"""
        tmp = ''
        for item, cnt in self.storage.items():
            tmp += f"{str(item)}: {cnt} pcs. \n"

        return f'Warehouse at {self.address} contains of \n{tmp}'


wh = Warehouse('Kyiv, Viskozna 135 str')
# print(wh.get_total_value())
wh.add_to_storage(phone_1, 40)
wh.add_to_storage(phone_2, 23)

# print(wh.get_item_value(phone_2))

wh.add_to_storage(phone_3, 4)
wh.add_to_storage(phone_4, 52)
wh.add_to_storage(phone_5, 22)

# print(wh.get_total_value())
# print(wh)

# print(wh.remove_form_storage(phone_2))
# print(wh.get_item_value(phone_2))
# print(wh)


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"Laptop {self.brand}, {self.model}, {self.price}"


laptop_1 = Laptop('HP', 'Pro book 450', 35000)
laptop_2 = Laptop('Lenovo', 'S340', 15000)

wh.add_to_storage(laptop_1, 40)
wh.add_to_storage(laptop_2, 10)

# print(wh.get_total_value())
# print(wh)


class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    @staticmethod
    def cat_sound(self):
        return "meow"

    def __str__(self):
        # return f"Hi, my {self.name =}"
        return f"Hi, my name in {self.name}, I'm {self.age} years old {self.color} cat"

    def __repr__(self):
        # return f"Hi, my {self.name =}"
        return f"Cat: {self.name}, Age: {self.age} color: {self.color}"


cat_1 = Cat("Barsik", 5, "black")

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_date(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def is_adult(age):
        return age > 18


person1 = Person("Michael", 21)
print(person1.age)
print(person1.is_adult(person1.age))

person2 = Person.from_birth_date("Slava", 1991)
print(person2.age)
