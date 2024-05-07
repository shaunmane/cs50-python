x = input("camelCase: ")

b = ""
for i in x:
    if (i.isupper()):
        b = b + "_" + i.lower()
    else:
        b = b + i
print("snake_case: " + b)


