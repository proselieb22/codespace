def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:  # Checks length
        return False
    if not s[:2].isalpha():  # Checks if first two characters are letters
        return False
    if not s.isalnum():  # Checks if all characters are alphanumeric
        return False
    if not s[2:].isdigit():  # Checks if characters after the first two are numbers
        return False
    if s[2] == '0':  # Checks if the first number is not '0'
        return False
    return True

main()