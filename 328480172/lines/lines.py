import sys


def main():
    check_arguments()

    try:
        with open(sys.argv[1], "r") as file:
            line_count = 0
            for line in file:
                stripped_line = line.strip()


                if not stripped_line or stripped_line.startswith("#"):
                    continue
                line_count += 1
            print(line_count)

    except FileNotFoundError:
        sys.exit("File does not exist")


def check_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()
