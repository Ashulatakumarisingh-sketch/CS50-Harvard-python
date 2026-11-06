import os
import sys
from PIL import Image, ImageOps


def main():
    check_arguments()

    try:
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as input_img:
            size = shirt.size
            output_img = ImageOps.fit(input_img, size)
            output_img.paste(shirt, shirt)
            output_img.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file1_ext = os.path.splitext(sys.argv[1].lower())[1]
    file2_ext = os.path.splitext(sys.argv[2].lower())[1]

    valid_extensions = [".jpg", ".jpeg", ".png"]
    if file1_ext not in valid_extensions:
        sys.exit("Invalid input")
    if file2_ext not in valid_extensions:
        sys.exit("Invalid output")

    if file1_ext != file2_ext:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
