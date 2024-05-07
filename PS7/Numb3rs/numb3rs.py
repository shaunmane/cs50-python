import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        if re.search(
            r"^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-1]?[0-9]?[0-9]?|2[0-4][0-9]|25[0-5]){1}$",
            ip,
        ):
            return True
        else:
            return False
    except ValueError:
        return False


if __name__ == "__main__":
    main()
