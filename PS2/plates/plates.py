def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    while len(s) <= 6:
        if len(s) < 2:
            return False
        elif s[-2].isnumeric() and s[-1].isalpha():
            return False
        elif s[-3].isnumeric() and s[-2].isalpha():
            return False
        elif s[1:2].isnumeric() or s[0:1].isnumeric():
            return False
        elif s[2] == "0":
            return False
        elif s[2].isalpha() and s[3] == "0":
            return False
        elif s[3].isalpha() and s[4] == "0":
            return False
        elif s.isspace():
            return False
        elif is_punct(s):
            return False
        return True

def is_punct(n):
    b = ".?!,:;-_[]{}()\'\"..."
    for i in b:
        if i in n:
            return True
        else:
            return False


main()