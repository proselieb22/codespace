import emoji

def emojize_text(text):
    emojized_text = emoji.emojize(text, use_aliases=True)
    return emojized_text

def main():
    user_input = input("Enter a text in English: ")
    emojized = emojize_text(user_input)
    print("Emojized text:", emojized)

if __name__ == "__main__":
    main()

