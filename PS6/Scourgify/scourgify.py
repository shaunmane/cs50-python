import sys
import csv


def main():
    greeting = len(sys.argv)
    length(greeting)

# conditional for the number of terminal commands
def length(greeting):
    greeting = len(sys.argv)
    if greeting == 3:
        try:
            first_file(sys.argv[1], sys.argv[2])
        except FileNotFoundError as a:
            sys.exit(f"Could not read {a}")
    elif greeting < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def first_file(f_file, s_file):
    f_file = sys.argv[1]
    s_file = sys.argv[2]

    students = []

    names = []

    with open(f_file) as file:
        reader = csv.reader(file)
        for line in reader:
            students.append({"name": line[0], "house": line[1]})

    for student in students:
        f_name = student["name"].split(",")[-1]
        s_name = student["name"].split(",")[0]
        names.append({"First name": f_name, "Last name": s_name, "House": student["house"]})

    #return names
    with open(s_file, "w", newline="") as csvfile:
        fieldnames = ["First name", "Last name", "House"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in names:
            writer.writerow({"First name": i["First name"], "Last name": i["Last name"], "House": i["House"]})


if __name__ == "__main__":
    main()

