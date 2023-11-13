def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:  # Check length
        return False
    if not s[:2].isalpha():  # Check if first two characters are letters
        return False
    if s[2:-1].isdigit() and s[-1].isnumeric() and s[2] != '0':  # Check number placement
        return True
    return False

main()
