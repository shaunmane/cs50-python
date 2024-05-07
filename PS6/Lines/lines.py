import sys


if len(sys.argv) == 2:
    try:
        if sys.argv[1].endswith(".py"):
            with open(sys.argv[1], "r") as file:
                count = 0
                for line in file:
                    e_line = line.strip()
                    if e_line.strip():
                        if not e_line.startswith("#"):
                            count += 1
                    else:
                        pass
            print(count)
        else:
            sys.exit("Not a Python file")
    except FileNotFoundError:
        sys.exit("File does not exist")
elif len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")