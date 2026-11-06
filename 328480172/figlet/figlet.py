import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        selected_font = random.choice(available_fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        selected_font = sys.argv[2]
        if selected_font not in available_fonts:
            sys.exit("Error: Invalid font name.")
    else:
        sys.exit("Error: Invalid usage.")

    figlet.setFont(font=selected_font)

    user_input = input("Input: ")
    print("Output:")
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
