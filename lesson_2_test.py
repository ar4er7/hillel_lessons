value = int(input())

# digit_1 = value // 1000
# digit_2 = value % 1000 // 100
# digit_3 = value % 100 // 10
# digit_4 = value % 10 // 1
#
#
# # print(digit_1,"\n")
# # print( digit_2,"\n")
# # print(digit_3,"\n")
# # print(digit_4,"\n")


digit_1 = value // 1000
digit_2 = value % 1000
digit_3 = value % 100
digit_4 = value % 10


print(digit_1, "\n")
print(digit_2 // 100, "\n")
print(digit_3 // 10, "\n")
print(digit_4 // 1)



