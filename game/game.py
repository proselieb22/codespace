import random

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")

def play_game(level):
    secret_number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < secret_number:
                print("Too small!")
            elif guess > secret_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            print("Please enter a valid integer.")

def main():
    level = get_level()
    print("Guess a number between 1 and", level)
    play_game(level)

if __name__ == "__main__":
    main()
