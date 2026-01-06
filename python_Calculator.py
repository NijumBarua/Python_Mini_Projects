Num1 = int(input("Enter a number: "))
Num2 = int(input("Enter a number: "))
operator= input ('Enter an operator (+, -, *, /): ')
if operator == "+":
    print(Num1 + Num2)
elif operator == "-":
    print(Num1 - Num2)
elif operator == "*":
    print(Num1 * Num2)
elif operator == "/":
    print(Num1 / Num2)
else:
    print("Invalid operator")