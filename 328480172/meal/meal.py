def main():
    time_input = input("what time is it? ").strip()
    hours = convert(time_input)

    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    converted_time = float(hours) + float(minutes) / 60.0
    return converted_time

if __name__ == "__main__":
    main()
