# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

number = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
digits = []
zeros = []

print(number)

for index in range(len(number)):
    if number[index] == 0:
        zeros.append(number[index])
    else:
        digits.append(number[index])

digits.extend(zeros)
print(digits)