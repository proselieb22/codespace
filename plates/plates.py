def starts_with_letters(s):
    return s[:2].isalpha()

def valid_length(s):
    return 2 <= len(s) <= 6

def valid_number_placement(s):
    if any(char.isdigit() for char in s):
        last_num_index = s.rfind([char for char in s if char.isdigit()][-1])
        if last_num_index != -1:
            return last_num_index == len(s) - 1 and s[last_num_index] != '0'
    return True

def no_punctuation(s):
    return s.isalnum()

def is_valid(s):
    return (
        starts_with_letters(s) and
        valid_length(s) and
        valid_number_placement(s) and
        no_punctuation(s)
    )

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
