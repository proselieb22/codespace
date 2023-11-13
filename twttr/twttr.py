def remove_vowels(text):
    vowels = "AEIOUaeiou"
    return "".join(char for char in text if char not in vowels)

def main():
    user_input = input("Enter a text: ")
    result = remove_vowels(user_input)
    print(result)

if __name__ == "__main__":
    main()
