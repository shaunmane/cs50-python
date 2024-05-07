import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    try:
        if matches := re.search(r"^([0-9]|1[0-2])?:?([0-5][0-9])? (AM|PM)+ to ([0-9]|1[0-2])?:?([0-5][0-9])? (AM|PM)+", s):

            # numbers grouped as strings
            a = int(matches.group(1))
            b = matches.group(2)
            c = int(matches.group(4))
            d = matches.group(5)

            if b == None or d == None:
                b = f"{0:02}"
                d = f"{0:02}"

            # time formats for AM
            ftd = f"{a:02}:{b}"
            std = f"{c:02}:{d}"

            # time formats for PM
            nf = (a + 12)
            ns = (c + 12)
            ft = f"{nf}:{b}"
            st = f"{ns}:{d}"

            # elif (a == 12 and matches.group(3) == "AM") or (c == 12 and matches.group(6) == "AM"):

            if matches.group(3) == "PM" and matches.group(6) == "PM":
                if a == 12 and c == 12:
                    return f"{ftd} to {std}"
                elif a == 12:
                    a = 12
                    return f"{a}:{b} to {st}"
                elif c == 12:
                    c = 12
                    return f"{ft} to {c}:{d}"
                else:
                    return f"{ft} to {st}"

            elif matches.group(3) == "AM" and matches.group(6) == "AM":
                if a == 12 and c == 12:
                    a = 0
                    c = 0
                    return f"{a:02}:{b} to {c:02}:{d}"
                elif a == 12:
                    a = 0
                    return f"{a:02}:{b} to {st}"
                elif c == 12:
                    c = 0
                    return f"{ft} to {c:02}:{d}"
                return f"{ftd} to {std}"

            elif matches.group(3) == "AM" and matches.group(6) == "PM":
                if a == 12 and c == 12:
                    a = 0
                    c = 12
                    return f"{a:02}:{b} to {c:02}:{d}"
                elif a == 12:
                    a = 0
                    return f"{a:02}:{b} to {st}"
                elif c == 12:
                    c = 12
                    return f"{ft} to {c}:{d}"
                else:
                    return f"{ftd} to {st}"

            elif matches.group(3) == "PM" and matches.group(6) == "AM":
                if a == 12 and c == 12:
                    a = 12
                    c = 0
                    return f"{a:02}:{b} to {c:02}:{d}"
                elif a == 12:
                    a = 12
                    return f"{a}:{b} to {st}"
                elif c == 12:
                    c = 0
                    return f"{ft} to {c:02}:{d}"
                else:
                    return f"{ft} to {std}"

        else:
            raise ValueError
    except ValueError:
        sys.exit(ValueError)


if __name__ == "__main__":
    main()
