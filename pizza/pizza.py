import sys
import csv
from tabulate import tabulate

def create_ascii_table(file_name):
    # Check if the file name ends with '.csv'
    if not file_name.endswith('.csv'):
        sys.exit("Not a CSV file")

    try:
        with open(file_name, 'r') as file:
            csv_reader = csv.DictReader(file)
            table = list(csv_reader)
            if not table:
                sys.exit("Empty CSV file")
            headers = table[0].keys()
            print(tabulate(table, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    file_to_read = sys.argv[1]
    create_ascii_table(file_to_read)
