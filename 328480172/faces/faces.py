def main():
    user_input = input("enter your text:")
    output = convert(user_input)
    print(output)

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

main()
