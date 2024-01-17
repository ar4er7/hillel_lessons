# чтобы работать с калькулятором - на 3 запроса программы введи по очереди: перве число, оператор, второе число.
# оператор может быть только один из 4ех: + - * /
# если оператор / и второе число 0, то программа выдаст сообщение об ошибке.1
# если число дробное, то разделение - точкой

first_symbol = float(input("enter the 1st symbol:  "))
operator = input("enter the operator:  ")
second_symbol = float(input("enter the 2nd symbol:  "))
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