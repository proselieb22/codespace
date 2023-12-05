def main():
    pass

def shorten(word):
    vowels = "AEIOUaeiou"
    return ''.join(char for char in word if char not in vowels)

if __name__ == "__main__":
    main()
