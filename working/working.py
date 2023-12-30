import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r'^(\d{1,2})(?::(\d{2}))?\s(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s(AM|PM)$'

    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    start_hour, start_minute, start_meridiem, end_hour, end_minute, end_meridiem = match.groups()

    start_hour = int(start_hour)
    start_minute = int(start_minute or 0)
    end_hour = int(end_hour)
    end_minute = int(end_minute or 0)

    if (start_hour > 12 or start_minute >= 60 or end_hour > 12 or end_minute >= 60 or
            (start_hour == 12 and start_meridiem == 'AM') or (end_hour == 12 and end_meridiem == 'AM')):
        raise ValueError("Invalid time")

    if start_meridiem == 'PM' and start_hour != 12:
        start_hour += 12

    if end_meridiem == 'PM' and end_hour != 12:
        end_hour += 12

    return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"


if __name__ == "__main__":
    main()
