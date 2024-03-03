from hillel_lessons.lesson_15.Custom_exceptions import OverCountException
"""класс группа. Основа - коллекция.
переменная capacity - защищена"""

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()
        self.count = 0 #текущее кол-во студентов в группе
        self.__capacity = 10 #максимальная вместимость группы

    def add_student(self, student):
        if self.count < self.get_capacity():
            self.group.add(student)
            self.count += 1
        else:
            raise OverCountException('too many students', self.count)

    def delete_student(self, last_name):
        if self.group:
            for student in self.group:
                if last_name == student.last_name:
                    self.group.remove(student)
                    self.count -= 1
                    break
        else:
            print('the group is empty')

    def find_student(self, last_name):
        if self.group:
            for student in self.group:
                if last_name == student.last_name:
                    return student
        return None

    def get_capacity(self):
        return self.__capacity

    def __str__(self):
        all_students = ''
        count = len(self.group)
        for student in self.group:
            all_students += f'{student.first_name}'
            count -= 1
            if count > 0:
                all_students += ', '

        return f'Number:{self.number}\n{all_students} '
