import csv
import sys

def clean_names(input_file, output_file):
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = ['first', 'last', 'house']

            with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:
                    name = row['name'].split(', ')
                    first_name = name[1]
                    last_name = name[0].replace('"', '')  # Remove quotes from last name
                    writer.writerow({'first': first_name, 'last': last_name, 'house': row['house']})
    except FileNotFoundError:
        sys.exit("Could not read {}".format(input_file))
    except IndexError:
        sys.exit("Invalid format in the input file")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Too few or too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    clean_names(input_file, output_file)
