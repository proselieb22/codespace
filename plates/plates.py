def is_valid(s):
    if len(s) < 2 or not s[:2].isalpha():
        return False

    if len(s) > 6:
        return False

    if not s.isalnum():
        return False

    if '0' in s[:-1] or not s[-1].isdigit():
        return False

    return True


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


main()