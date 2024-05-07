def main():
    word = input("Input: ")
    print("Output: " + shorten(word))

def shorten(word):
    b = ""
    for i in word:
        if (
        i == "i"
        or i == "I"
        or i == "a"
        or i == "A"
        or i == "e"
        or i == "E"
        or i == "u"
        or i == "U"
        or i == "o"
        or i == "O"
            ):
            continue
        else:
            b = b + i
    return b

if __name__ == "__main__":
    main()