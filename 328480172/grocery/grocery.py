import sys

def main():
    grocery_list = {}

    while True:
        try:
            item = input().strip().lower()

            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

        except EOFError:
                  print()
                  break

    for sorted_item in sorted(grocery_list.keys()):
       print(f"{grocery_list[sorted_item]} {sorted_item.upper()}")

if __name__ == "__main__":
    main()
