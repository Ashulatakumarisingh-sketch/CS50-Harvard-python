def main():
    answer = input("what is the answer to the great question  of life, the universe, and Everything?").strip().lower()

    if answer =="42" or answer =="forty-two" or answer =="forty two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()


