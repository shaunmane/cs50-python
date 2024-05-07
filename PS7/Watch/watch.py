import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    matches = re.search(r"https?://(www\.)?youtube?\.com/?embed/?(\w.{10})", s, re.IGNORECASE)
    if s.startswith("<iframe"):
        if matches:
            y, x = matches.groups()
            name = f"https://youtu.be/{x}"
            return name
    else:
        return None


if __name__ == "__main__":
    main()