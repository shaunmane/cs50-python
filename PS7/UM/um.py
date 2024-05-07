import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = len(re.findall(r"\bum\b", s, re.IGNORECASE))
    return matches


if __name__ == "__main__":
    main()
