def main():
    camel_case = input("camelcase: ").strip()
    print("snake_case: ", end="")

    for char in camel_case:
        if char.isupper():
            print("_" + char.lower(), end="")
        else:
            print(char, end="")

    print()

if __name__ == "__main__":
    main()
