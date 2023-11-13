def has_at_least_two_letters(s):
    letter_count = sum(1 for char in s if char.isalpha())
    return letter_count >= 2

def has_valid_length(s):
    return 2 <= len(s) <= 6

def has_valid_number_placement(s):
    if any(char.isdigit() for char in s):
        last_num_index = s.rfind([char for char in s if char.isdigit()][-1])
        if last_num_index != -1:
            return s[last_num_index] == s[-1] and s[last_num_index] != '0'
    return True

def has_no_punctuation(s):
    return all(char.isalnum() for char in s)

def is_valid(s):
    return (
        has_at_least_two_letters(s) and
        has_valid_length(s) and
        has_valid_number_placement(s) and
        has_no_punctuation(s)
    )

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
