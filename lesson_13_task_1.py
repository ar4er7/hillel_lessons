class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, age: {self.age}, gender: {self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {super().__str__()}, record book: {self.record_book}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()
        self.count = 0
        self.__capacity = 10

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


class OverCountException(Exception):

    def __init__(self, message, x):
        super().__init__()
        self.message = message
        self.x = x

    def get_exception_message(self):
        return self.message


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 25, 'MonaLiza', 'Pupkin', 'AN140')
st4 = Student('Female', 25, 'Garry', 'Petrov', 'AN115')
st5 = Student('Female', 25, 'Andrew', 'Ivanov', 'AN141')
st6 = Student('Female', 25, 'Petr', 'Sharikov', 'AN148')
st7 = Student('Female', 25, 'Ignat', 'Bochkin', 'AN149')
st8 = Student('Female', 25, 'Egor', 'Kopytin', 'AN112')
st9 = Student('Female', 25, 'Lev', 'Sgrivoy', 'AN134')
st10 = Student('Female', 25, 'Galina', 'Blanka', 'AN167')
st11 = Student('Female', 25, 'Nikita', 'Perviu', 'AN190')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)

print(str(gr.find_student('Jobs')))

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку має повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student
#
gr.delete_student('Taylor')  # No error!

"""тут начинаю добавлять 10 студентов для 14го занятия"""

gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
print(gr.count)

try:
    gr.add_student(st11)
except OverCountException as err:
    print(err.get_exception_message())
    print(f"should be {gr.get_capacity()}, or less")



