import sys
from validator_collection import checkers

def main():
    print(validate(input("What's your email address? ").strip()))


def validate(email):
    try:
        if checkers.is_email(email):
            return "Valid"
        else:
            return "Invalid"
    except ValueError:
        sys.exit("Enter email address!")


if __name__ == "__main__":
    main()