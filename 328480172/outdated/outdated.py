def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        user_input = input("Date: ").strip()
        if "/" in user_input:
            try:
                month, day, year = user_input.split("/")
                if not (month.isdigit() and day.isdigit() and year.isdigit()):
                    continue

                month = int(month)
                day = int(day)
                year = int(year)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
            except ValueError:
                continue

        elif "," in user_input:
            try:
                parts, year = user_input.split(",")
                year = year.strip()
                month_name, day = parts.strip().split(" ")
                month_name = month_name.strip().capitalize()
                day = day.strip()

                if month_name in months and day.isdigit() and year.isdigit():
                    month = months.index(month_name) + 1
                    day = int(day)
                    year = int(year)


                    if 1 <= day <= 31:
                        print(f"{year:04d}-{month:02d}-{day:02d}")
                        break
            except ValueError:
                continue

if __name__ == "__main__":
    main()
