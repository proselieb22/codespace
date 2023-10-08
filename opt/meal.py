def main():
    input = input("What time is it? ")
    time = convert(input)

def convert(time):
    hours, minutes = time.split(":")
    new_minute = float(minutes) / 60 


if __name__ == "__main__":
    main()