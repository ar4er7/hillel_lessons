

def add_one(some_list):
    all_nums = ''
    for number in some_list:
        all_nums += str(number)  # made a sting with all nums
    added_1_int = int(all_nums) + 1  # wrapped str in int and added 1
    return [int(x) for x in str(added_1_int)]

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

