from validator_collection import validators, checkers

def main():
    email = input("Email: ")
    if checkers.is_email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
