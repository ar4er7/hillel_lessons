# value_int = -11
#
# if value_int > 0 and value_int <= 10:
#     print(f"{value_int} is between 0 and 10")
# elif value_int > 10:
#     print(f"{value_int} is bigger than 10")
# else:
#     print(f"{value_int} is not less than 0")
#
# print("end")

# value_1 = 2000
# value_2 = 331
# result = "A" if value_1 > value_2 else "B"
# print(result)

base_list = [1,2,3,4]
print(f"base list original {base_list}")

new_list = base_list * 4
print(f"new list with original base list{new_list}")

print(f"new list's 0 index {new_list[0]}")

base_list[0] = 10
print(f"updated base list {base_list}")
print(f"new list after updating the base list {new_list}")
