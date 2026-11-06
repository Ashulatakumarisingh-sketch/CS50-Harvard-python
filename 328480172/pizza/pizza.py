import csv
import sys
from tabulate import tabulate


def main():
    check_arguments()

    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            table = list(reader)

            if len(table) == 0:
                return

            headers = table[0]
            data = table[1:]
            print(tabulate(data, headers, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


def check_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
