is_retry = "y"
result = 0

while is_retry == "y":

    is_retry = "n"
    first_symbol = float(input("enter the 1st symbol:  "))
    operator = input("enter the operator:  ")

    if operator not in ["+", "-", "/", "*"]:
        print("it's not an operator symbol ")
        is_continue = "n"
    else:
        second_symbol = float(input("enter the 2nd symbol:  "))

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


    is_retry = input("type y to retry: ")