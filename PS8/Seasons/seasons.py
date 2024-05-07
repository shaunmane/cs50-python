from datetime import date
import inflect
import re
import sys


def main():
    n = input("Date of Birth: ").strip()
    p = inflect.engine()
    words = p.number_to_words(get_date(n), andword="")
    print(f"{words.capitalize()} minutes")


def get_date(n):
    today = date.today()
    if matches := re.search(r"^(1[0-9][0-9][0-9]|2[0][0-2][0-3])+-(0[0-9]|1[0-2])+-([0-9]|[0-1][0-9]|[0-2][0-9]|[0-3][0-1])$", n):
        # stores the match as a variable
        dob = f"{matches.group(1)}-{matches.group(2)}-{matches.group(3)}"

        # converts string to date object
        dob = date.fromisoformat(dob)

        # gets the difference betwen today's date and the date of birth (dob) and converts it to minutes
        delta = abs(today - dob).total_seconds() / 60
        return int(delta)

    else:
        sys.exit("Invalid  Jardate")


if __name__ == "__main__":
    main()
