a = input("Enter an expression: \n")
x, y, z = a.split(" ")

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*" or y == "x":
    print(float(x) * float(z))
elif y == "/":
    print(float(x) / float(z))
else:
    print("Incorrect Operator")