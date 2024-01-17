first_symbol = int(input("enter the 1st symbol:  "))
operator = input("enter the operator:  ")
second_symbol = int(input("enter the 2nd symbol:  "))
result = 0

if operator == "+":
    result = first_symbol + second_symbol

elif operator == "-":
    result = first_symbol - second_symbol

elif operator == "*":
    result = first_symbol * second_symbol

else:
    if second_symbol == 0:
        result = "ERROR - can't divide by zero"
    else:
        result = first_symbol / second_symbol

print(result)