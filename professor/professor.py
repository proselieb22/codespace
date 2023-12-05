import random


def main():
    level = get_level()
    score = 0
    for q in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        for a in range(3):
            result = check(x, y)
            if result == True:
                score += 1
                break
            if result == False and a == 2:
                print(str(x) + " + " + str(y) + " = " + str(z))
            if result == False and a != 2:
                print("EEE")

    print("Score: "+ str(score))


def get_level():
    level = input("Level: ")
    if level.isnumeric() == False:
        return get_level()
    if int(level) in [1, 2, 3]:
        return int(level)
    else:
        return get_level()


def generate_integer(level):
    try:
        if level == 1:
            return random.randint(0, 9)
        if level == 2:
            return random.randint(10, 99)
        if level == 3:
            return random.randint(100, 999)
    except:
        raise ValueError


def check(x, y):
    answer = x + y
    response = int(input(str(x) + " + " + str(y) + " = "))
    if answer == response:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
