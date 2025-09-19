import task

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


# print(operations["*"](4,8))

def calculator():
    print(task.art)
    should_accumulate = True
    num1 = float(input("What is the first number? : "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation : ")
        num2 = float(input("What is the next number? : "))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")

        choice = input(f"Type 'y' to continue with the {answer} or type 'n' to start a new calculation : ")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n " * 30)
            calculator()


calculator()
