import sys
import re
from datetime import date
import inflect

def main():
    birth_date = input("Date of Birth: ")
    try:
        days = check_date(birth_date)
        minutes = days * 24 * 60
        print(convert_to_words(minutes))
    except ValueError:
        sys.exit("Invalid date")


def check_date(birth_date):
    if not re.search(r"^\d{4}-\d{2}-\d{2}$", birth_date):
        raise ValueError

    year, month, day = birth_date.split("-")
    born = date(int(year), int(month), int(day))
    today = date.today()
    diff = today - born
    return diff.days


def convert_to_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, wantlist=False)
    words = words.replace(" and ", " ")
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
