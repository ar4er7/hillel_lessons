set_keys_1 = set()
set_keys_2 = set()

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

set_keys_1.update(my_dict_1.keys())
set_keys_2.update(my_dict_2.keys())
print(set_keys_1)
common_keys = set_keys_1.copy()

common_keys.update(set_keys_2)
only_in_1st = set_keys_1.difference(set_keys_2)
print("common keys: ", common_keys)
print("difference 1 of 2 keys: ", only_in_1st)
print(set_keys_1)








