def calculate(opr, n1, n2):
    if opr == "+":
        return n1 + n2
    elif opr == "-":
        return n1 - n2
    elif opr == "*":
        return n1 * n2
    elif opr == "/":
        return n1 / n2
    else:
        return "Invalid operation"


print("Simple Calculator")
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
opr = input("Enter operation(+,-,*,/): ")
result = calculate(opr, n1, n2)
print(result)
