
x = input("Hello, How may I help? \n").casefold().strip()


if x.startswith("hello"):
    print("$0")
elif x[0] == "h":
    print("$20")
else:
    print("$100")
