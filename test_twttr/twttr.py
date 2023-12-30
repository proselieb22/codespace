def main():
    nachricht = input("input: ")
    nachricht_without_vowels = shorten(input)
    print("Output: nachricht_without_vowels)

def shorten(word):
    word_without_vowels = ""
    for letter in word:
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
            word_without_voweös += letter
    return word_without_vowels

if _name_ == "__main__":
    main()


