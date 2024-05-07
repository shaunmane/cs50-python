import string

def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    while len(s) <= 6:
        try:
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
        except IndexError:
            return False
    else:
        return False

def is_punct(n):
    return any(i in string.punctuation for i in n)

if __name__ == "__main__":
    main()
