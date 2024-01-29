children = []
long_names = []
ages_sum = 0

dudes = [{"name": "John", "age": 41},
         {"name": "Batman", "age": 15},
         {"name": "Bob", "age": 49},
         {"name": "Billy", "age": 15},
         {"name": "Timmy", "age": 99},
         {"name": "Volodymyr", "age": 41}
         ]
min_age = dudes[0].get("age") #возраст первого человека указываем как минимальный
max_name_length = len(dudes[0].get("name")) #длину первого имени указываем, как максимальную

for man in dudes: #находим самый маленький возраст и кладем его в min_age
    if man.get("age") < min_age:
        min_age = man.get("age")

    ages_sum += man.get("age") #суммируем все возрасты в переменную ages_sum

    if len(man.get("name")) > max_name_length: #находим длину самого длинного имени икладем его в max_name_lenth
        max_name_length = len(man.get("name"))

average_age = ages_sum / len(dudes)

for man in dudes: #все элементы массива с минимальным возрастом кладем в массив children
    if man.get("age") == min_age:
        children.append(man.get("name"))

    if len(man.get("name")) == max_name_length:
        long_names.append(man.get("name"))

print("youngest people are: ", children)
print("longest names: ", long_names)
print("average age: ", int(average_age))
