from hillel_lessons.lesson_14.Human import Human
"""класс студента. Метод __eq__ переопределен"""

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return f'Student: {super().__str__()}, record book: {self.record_book}'
