def main():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").casefold().strip()
    if is_deep(x):
        print("Yes")
    else:
        print("No")

def is_deep(n):
    if n == "42":
        return True
    elif n == "fourty-two" or n == "fourty two" or n == "forty two" or n == "forty-two":
        return True
    else:
        return False
"""
match x:
    case "Fourty-two" | "fourtytwo" | "fourty two" | "forty-two" | "forty two" :
        print("Yes")
    case _:
        print("No")
"""
main()