number = [1, 0, 13, 0, 0, 0, 5]
new_number = number
index = 0

while index < len(number):
   if number[index] == 0:
      zero = new_number.pop(index)
      new_number.insert(zero,-1)
