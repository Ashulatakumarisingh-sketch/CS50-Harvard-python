def main():
    user_input = input("Input: ")
    print(f"Output: {shorten(user_input)}")

def shorten(word):
    output = ""
    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            output += char
    return output


if __name__ == "__main__":
    main()

