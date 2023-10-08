def main():
    input = input("What time is it? ")
    time = convert(input)
    print(time)
def convert(time):
    hours, minutes = time.split(":")
    new_minute = float(minutes) / 60
    return float(hours) = float(minutes) / 60

if __name__ == "__main__":
    main()