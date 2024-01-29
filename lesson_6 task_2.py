
my_dict_1 = {
    "name": "Ivan",
    "sex": "male",
    "eye_color": "brown",
    "age": 30
    }

my_dict_2 = {
    "name": "Volksvagen",
    "type": "sedan",
    "color": "brown",
    "year": 2015
    }

set_keys_1 = set(my_dict_1.keys()) #сэт ключей первого словаря
set_keys_2 = set(my_dict_2.keys()) #сэт ключей второго словаря

common_keys = set_keys_1.copy() #копирую сет ключей №1, чтобы оригинальный сет испольовать потом еще раз
common_keys.update(set_keys_2)

only_in_1st = set_keys_1.difference(set_keys_2)

print("common keys: ", common_keys)
print("unic keys from 1st dict: ", only_in_1st)

my_dict_unic_1 = {}

for pairs in only_in_1st:
    my_dict_unic_1[pairs] = my_dict_1[pairs]

print("new dictionary with unic items from the 1st dict: ", my_dict_unic_1)







