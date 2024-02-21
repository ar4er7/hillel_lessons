# def my_func():
#     return 10
#
# if __name__ == "__main__":
#     print("form this file")
# else:
#     print(f'from file "{my_func.__module__}"')

# bigger_than_zero = lambda x: x > 0



numbers = [1, 0, 3, 4]

power_numbers = map(lambda x: x ** 2, numbers)
# long analogue:
#
# def power_numbers (sequence: list):
#     result = []
#     for i in sequence:
#         result.append(i**2)


filter_numbers = filter(lambda x: x > 2, numbers)
# long analogue:
#
# def filter_numbers(seq, predicate):
#     result = []
#
#     for element in seq:
#         if predicate(element):
#             result.append(element)
#
#     return result
#
#
# filter_numbers(numbers, lambda x: x > 2)

print(numbers)
print(list(power_numbers))
# print(list(filter_numbers))

list_1 = ['apple 1$', 'mango 20$', 'orange 3$']
ans = list(map(str.split, list_1))
print(ans)