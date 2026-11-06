def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()

    if not (2 <= len(s) <= 6):
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    has_number_started = False
    for char in s:
        if not char.isalnum():
            return False

        if char.isdigit():
            if not has_number_started and char == "0":
                return False
            has_number_started = True
        else:
            if has_number_started:
                return False

    return True


if __name__ == "__main__":
    main()


