def calculate_change(total_inserted):
    return total_inserted - 50  # Calculate the change

def main():
    while True:
        total_inserted = 0
        while total_inserted < 50:
            print(f"Amount Due: {50 - total_inserted}")
            coin = int(input("Insert Coin: "))
            if coin in [25, 10, 5]:
                total_inserted += coin
            else:
                print("coke rejects invalid amount of cents")

        change = calculate_change(total_inserted)
        if change == 0:
            print("No change owed.")
        else:
            print(f"Change Owed: {abs(change)} cents")

        choice = input("Would you like to buy another Coke? (yes/no): ")
        if choice.lower() != 'yes':
            break

if __name__ == "__main__":
    main()


