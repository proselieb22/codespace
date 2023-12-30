from datetime import date, datetime
import sys


def calculate_age_in_minutes(birthdate):
    try:
        birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
    except ValueError:
        sys.exit()

    today = date.today()
    age = today - birthdate
    total_minutes = age.total_seconds() // 60  # Convert total seconds to minutes

    return int(total_minutes)


def convert_to_words(n):
    def num_to_words(n):
        units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                 "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        if n < 20:
            return units[int(n)]
        else:
            return tens[int(n // 10)] + " " + units[int(n % 10)]

    if n == 0:
        return "Zero"

    result = ""
    if n >= 1000000:
        result += num_to_words(n // 1000000) + " Million, "
        n %= 1000000
    if n >= 1000:
        result += num_to_words(n // 1000) + " Thousand, "
        n %= 1000
    if n > 0:
        result += num_to_words(n)

    return result.capitalize()


def main():
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")

    total_minutes = calculate_age_in_minutes(birthdate)
    age_in_words = convert_to_words(total_minutes)

    print(age_in_words, "minutes")


if __name__ == "__main__":
    main()
