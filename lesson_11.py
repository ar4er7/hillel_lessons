# filename = 'test.txt'
val_list = ["Hello, World!", "Apple", 'red', 'green']


# with open(filename, "w") as my_file:
#     my_file.write('Hello, World\n')
#     my_file.write('Hello, World\n')
#     my_file.write('Hello, World\n')
#
# filename = 'test.txt'
#
# with open(filename, "w") as my_file:
#     for i in val_list:
#         my_file.writelines(i + '\n')

filename = 'test.txt'

# my_file = open(filename,'r')
# data = my_file.read()
# print(data)
# my_file.close()

# with open(filename, 'r') as my_file:
#     data = my_file.readlines()
#     print(data, type(data))

# with open(filename, 'r') as my_file:
#     # data = my_file.readline()
#     print(my_file.readline())
#     print(my_file.readline())

# with open(filename, 'a') as my_file:
#     data = my_file.write('\nHello!')

# with open(filename, 'a+') as my_file:
#     # data = my_file.write('\nworld')
#     # print(data)
#     my_file.seek(17)
#     contex = my_file.read()
# print(contex)
#
# with open(filename, 'a+') as my_file:
#     data = my_file.read()
#     # print(data)
#     # my_file.seek(17)
# print(data)

# with open(filename, 'w', encoding='UTF-8') as my_file:
#     data = my_file.write("\nexample code")

class Car:
    color = 'red'
    engine = 2000



car_1 = Car()
car_1.color = 'gold'
car_1.body = "sedan"
