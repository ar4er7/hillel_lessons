children = []
long_names = []

dudes = [{"name": "John", "age": 41},
         {"name": "Batman", "age": 15},
         {"name": "Bob", "age": 49},
         {"name": "Billy", "age": 15},
         {"name": "Timmy", "age": 99},
         {"name": "Volodymyr", "age": 41}
         ]
min_age = dudes[0].get("age")
max_name_length = len(dudes[0].get("name"))

for man in dudes:
    if man.get("age") < min_age:
        min_age = man.get("age")

    if len(man.get("name")) > max_name_length:
        max_name_length = len(man.get("name"))
    print(max_name_length)

for man in dudes:
    if man.get("age") == min_age:
        children.append(man.get("name"))

    if man.get("name") == max_name_length:
        long_names.append(man.get("name"))

print(children)
print(long_names)

