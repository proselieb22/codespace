import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Split the address into its components
    parts = ip.split('.')

    # Check if the IP address has four components
    if len(parts) != 4:
        return False

    # Check if each part is a valid integer between 0 and 255
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False

    return True


if __name__ == "__main__":
    main()
