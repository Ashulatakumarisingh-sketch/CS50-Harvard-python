import random


def main():
    game_level = get_level()
    final_score = 0

    for _ in range(10):
        first_num = generate_integer(game_level)
        second_num = generate_integer(game_level)
        answer = first_num + second_num
        wrong_attempts = 0

        while wrong_attempts < 3:
            try:
                guess = int(input(f"{first_num} + {second_num} = "))
                if guess == answer:
                    final_score += 1
                    break
                else:
                     print("EEE")
                     wrong_attempts += 1
            except ValueError:
                print("EEE")
                wrong_attempts += 1

        if wrong_attempts == 3:
            print(f"{first_num} + {second_num} = {answer}")

    print(f"Score: {final_score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3] :
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()

