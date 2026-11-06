import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):
    pattern = r"^(\d{1,2})(?::([0-5]\d))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::([0-5]\d))?\s+(AM|PM)$"

    if match := re.search(pattern, s, re.IGNORECASE):
        hr1, min1, period1, hr2, min2, period2 = match.groups()
        time1 = format_24_hr(int(hr1), min1, period1)
        time2 = format_24_hr(int(hr2), min2, period2)

        return f"{time1} to {time2}"
    else:
        raise ValueError


def format_24_hr(hour, minute, period):
    if hour < 1 or hour > 12:
        raise ValueError

    if minute is None:
        minute = "00"

    if period.upper() == "PM" and hour != 12:
        hour += 12
    elif period.upper() == "AM" and hour == 12:
        hour = 0

    return f"{hour:02d}:{minute}"


if __name__ == "__main__":
    main()
