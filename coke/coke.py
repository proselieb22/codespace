def calculate_change(total_inserted):
    return total_inserted - 50  

def main():
    while True:
        total_inserted = 0
        while total_inserted < 50:
            print(f"Amount Due: {50 - total_inserted}")
            coin = int(input("Insert Coin: "))
            if coin in [25, 10, 5]:
                total_inserted += coin
            else:
                print("Coke only accepts 25, 10, or 5 cents. Please insert a valid coin.")

        change = calculate_change(total_inserted)
        if change == 0:
            print("No change owed. Thank you!")
        else:
            print(f"Change Owed: {change if change > 0 else 0} cents")

        choice = input("Would you like to buy another Coke? (yes/no): ")
        if choice.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

