# Dictionary containing fruits and their corresponding calories per portion
fruit_calories = {
    "apple": 130,
    "avocado": 50,
    "sweet cherries": 100,
    # Add other fruits and their calorie values here
}

def main():
    fruit = input("Enter a fruit: ").lower()  # Convert input to lowercase for case insensitivity
    if fruit in fruit_calories:
        print(f"Calories: {fruit_calories[fruit]}")
    # No output if the entered fruit is not in the dictionary

if __name__ == "__main__":
    main()
