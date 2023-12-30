import sys
import requests
import bs4
import re
import wikipedia


def print_help():
    print("This program helps you sort keywords by the number of Google search results.")
    print("Usage: project.py INPUT_FILE OUTPUT_FILE [-w]")
    print("-h  help")
    print("-w  output links for Wikipedia pages into the file")
    sys.exit(0)


def process_arguments():
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print_help()
    elif len(sys.argv) == 3:
        return False
    elif len(sys.argv) == 4 and sys.argv[-1] == '-w':
        return True
    else:
        print("Usage: project.py INPUT_FILE OUTPUT_FILE [-w]")
        print("Use -h for the help page")
        sys.exit(1)


def read_input_file(file_path):
    try:
        with open(file_path) as file:
            return file.readlines()
    except FileNotFoundError:
        print("Invalid input file")
        sys.exit(1)


def google_search(keywords):
    results = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }

    for keyword in keywords:
        response = requests.get("https://www.google.com/search?q=" + keyword.strip(), headers=headers)
        soup = bs4.BeautifulSoup(response.content, features="lxml")
        stats = soup.find(id="result-stats")

        if stats:
            matches = re.search(r"About ([0-9,]+) results", stats.text)
            if matches:
                n = matches.group(1)
            else:
                n = '0'
        else:
            n = '0'

        results[keyword.strip()] = int(n.replace(',', ''))

    return results



def get_wikipedia_links(keywords):
    wikipages = {}

    for keyword in keywords:
        try:
            word = wikipedia.search(keyword.strip())[0]
            page = wikipedia.page(word, auto_suggest=False)
            wikipages[keyword.strip()] = page.url
        except (IndexError, wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError):
            continue

    return wikipages


def output_to_file(results, wikipages, outfile="output.tsv"):
    sorted_results = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))

    with open(outfile, 'w') as output_file:
        for key, value in sorted_results.items():
            output_file.write(f"{key}\t{value:,}")
            if key in wikipages:
                output_file.write(f"\t{wikipages[key]}\n")
            else:
                output_file.write("\n")


def main():
    if len(sys.argv) < 3:
        print("Insufficient arguments.")
        print_help()

    wiki_flag = process_arguments()
    input_keywords = read_input_file(sys.argv[1])
    search_results = google_search(input_keywords)

    if wiki_flag:
        wikipedia_links = get_wikipedia_links(input_keywords)
    else:
        wikipedia_links = {}

    output_to_file(search_results, wikipedia_links, sys.argv[2])


if __name__ == "__main__":
    main()
