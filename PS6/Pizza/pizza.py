import sys
import csv
from tabulate import tabulate


if len(sys.argv) == 2:
    try:
        if sys.argv[1].endswith(".csv"):
            pizzas = []
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                for row in reader:
                    pizzas.append({"Pizza": row[0], "Small": row[1], "Large": row[2]})
                print(tabulate(pizzas, headers="firstrow", tablefmt="grid"))
        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
            sys.exit("File does not exist")
elif len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

