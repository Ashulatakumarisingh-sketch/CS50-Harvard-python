import csv
import sys


def main():
    check_arguments()

    try:
        with open(sys.argv[1], "r") as infile:
            reader = csv.DictReader(infile)
            with open(sys.argv[2], "w", newline="") as outfile:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(", ")
                    writer.writerow({
                        "first": first.strip(),
                        "last": last.strip(),
                        "house": row["house"]
                    })

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()

