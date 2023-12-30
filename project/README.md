# Google Search Analyzer

#### Video Demo: [YouTube Demo](https://youtu.be/7jk9Uzj8HM0)
#### Description:
This project serves as a final project for the CS50P course. It aids in sorting keywords based on the number of Google search results, particularly useful for handling extensive datasets such as thousands of microorganisms in a microbiome. This tool assists in identifying well-studied species, offering insights into potential research targets. By arranging keywords in order of their popularity on Google and providing Wikipedia links, it helps discern what is extensively studied versus what remains relatively obscure.

#### Components:
This project consists of four documents:
1. `project.py`: Contains the primary Python code for the program.
2. `test_project.py`: Includes test codes for pytest.
3. `requirements.txt`: Lists the Python modules required for `project.py`. Install using `pip install` followed by the module name.
4. `README.md`: A Markdown file containing instructions.

#### Design:
`project.py` comprises four main functions:
1. `main()`: Accepts input and output files via sys arguments. It calls `google()` and optionally `wiki()` (if "-w" is provided) to retrieve Google search result numbers and Wikipedia page links. Finally, it utilizes `output()` to list results in descending order into the output file.
2. `google()`: Takes an input file with a keyword on each line. It scrapes Google search results using the "requests" module and then extracts the div with the "result-stats" id from the HTML content using "BeautifulSoup". It utilizes regular expressions ("re") to extract the number of Google search results from the div and converts it into an integer. The numbers are then stored in a dictionary returned at the end of the function.
3. `wiki()`: Invoked when "-w" is provided. It accepts the same input file as `google()` and searches Wikipedia for the most relevant keywords. It retrieves the Wikipedia page and its associated URL (if available). Finally, it stores all links in a dictionary and returns it.
4. `output()`: Accepts dictionaries from `google()` and `wiki()`. It arranges keywords in descending order based on Google search results and writes them to the output file. If requested, Wikipedia links are also included in the same file.

#### User Instructions:
##### Usage: `python project.py INPUT_FILE OUTPUT_FILE [-w]`
`-h`: Show help page.\
`-w`: \[Optional\] Display Wikipedia links in the output file.

##### Example: `$ python project.py input.txt output.tsv -w`
##### `input.txt`:
##### `output.tsv`:

Ecoli
cats
New York
CS50

| Keyword  | Google Results | Wikipedia Link |
| -------- | -------------- | -------------- |
| New York | 8,360,000,000  | [New York City](https://en.wikipedia.org/wiki/New_York_City) |
| cats     | 4,270,000,000  | [Cat](https://en.wikipedia.org/wiki/Cat) |
| Ecoli    | 2,360,000,000  | [Escherichia coli](https://en.wikipedia.org/wiki/Escherichia_coli) |
| CS50     | 10,700,000     | [CS50](https://en.wikipedia.org/wiki/CS50) |

##### Observation: New York City appears to be the most searched item!
