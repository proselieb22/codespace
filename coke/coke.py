def calculate_change(total_inserted):
    return total_inserted - 50  # Calculate the change

def main():
    total_inserted = 0
    while total_inserted < 50:
        coin = int(input("Insert Coin: "))
        if coin in [25, 10, 5]:
            total_inserted += coin
            print(f"Amount Due: {50 - total_inserted}")
        else:
            print(f"Amount Due: {50 - total_inserted}")
            print("Machine does not accept that denomination.")

    change = calculate_change(total_inserted)
    if change == 0:
        print("Change Owed: 0")
    else:
        print(f"Change Owed: {change if change > 0 else 0}")

if __name__ == "__main__":
    main()




