a = float(input("a: "))
b = float(input("b: "))
op = input("Enter + - * / : ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")
