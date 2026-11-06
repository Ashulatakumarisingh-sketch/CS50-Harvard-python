def main():
    menu ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    total_cost = 0.0

    while True:
        try:
            item = input("Item: ")
            item_title = item.title()

            if item_title in menu:
                total_cost += menu[item_title]
                print(f"Total: ${total_cost:.2f}")

        except EOFError:
            print()
            break

if __name__=="__main__":
    main()

