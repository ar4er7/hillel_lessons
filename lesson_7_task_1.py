# я не понял, надо было ли програмно ограничить ввод возраста позитивными числами.
# поэтому на всякий случай добавил простую проверку.
def say_hi(name: str, age: int) -> str:
    if age >= 0:
        result = f"Hi. My name is {name} and I'm {age} years old"
        return result

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')



