# [0, 1, 7, 2, 4, 8] -> (0 + 7 + 4) * 8 = 88
# [1, 3, 5] -> 30
# [6] -> 36
# [] -> 0


numbers = [0, 1, 7, 2, 4, 8]
index = 0
result = 0

while index < len(numbers):
    result += numbers[index]
    index += 2

result *= numbers[-1]
print(result)