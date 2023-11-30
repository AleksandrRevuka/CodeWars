def check_number(number: str):
    try:
        if int(number):
            return True
    except ValueError:
        print(f"'{number}' is not a number. Try again.")
        return False


def check_operator(operator: str):
    if operator in "+-/*":
        return True
    else:
        print(f"'{operator}' is not '+' or '-' or '/' or '*'. Try again.")
        return False


def calc(operand: str, operator: str, operand_2: str):
    if operator == "+" and operand_2 is not None:
        return int(operand_2) + int(operand)

    elif operator == "-" and operand_2 is not None:
        return int(operand_2) - int(operand)

    elif operator == "*" and operand_2 is not None:
        return int(operand_2) * int(operand)

    elif operator == "/" and operand_2 is not None:
        print(operand_2, operator, operand)
        try:
            int(operand_2) / int(operand)
        except ZeroDivisionError:
            exit('ZeroDivisionError')
        return int(operand_2) / int(operand)
    return operand


def main():
    result = None
    operand = None
    operator = None
    wait_for_number = True

    while True:
        operand = input("Enter a number ('q' exit): ")
        if operand == "q":
            break
        wait_for_number = check_number(operand)
        result = calc(operand, operator, result)
        print(result)

        while True:
            if wait_for_number:
                operator = input("Enter an operator ('q' exit): ")
                if operator == "q":
                    exit("EXIT")
                elif operator == "=":
                    print(result)
                    exit("EXIT")
                else:
                    wait_for_number = check_operator(operator)
                    if wait_for_number:
                        break
                    else:
                        wait_for_number = True
            else:
                break


if __name__ == '__main__':
    main()
