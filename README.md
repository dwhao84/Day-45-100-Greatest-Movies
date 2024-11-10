# Movie Scraper

A Python script that scrapes Empire Online's Top 100 Movies list and saves it to a text file.

## Description

This script scrapes a archived version of Empire Online's "100 Greatest Movies" list using BeautifulSoup4. It extracts movie titles from the webpage and saves them in chronological order to a text file.

## Prerequisites

The following Python packages are required:
- `beautifulsoup4`
- `requests`

You can install them using pip:
```bash
pip install beautifulsoup4 requests
```

## How It Works

1. The script sends a GET request to the archived Empire Online webpage
2. BeautifulSoup4 parses the HTML content
3. Movie titles are extracted from `<h3>` elements with the class "title"
4. The list is reversed to display movies in ascending order (1 to 100)
5. Results are saved to 'items.txt', with each movie on a new line

## Code Breakdown

- `requests.get()`: Fetches the webpage content
- `BeautifulSoup()`: Parses the HTML
- `find_all()`: Locates all movie title elements
- `get_text()`: Extracts text from HTML elements
- List comprehension creates the movie list
- `reverse()`: Reorders the list (alternatively `[::-1]` can be used)
- File operations write the results to 'items.txt'

## Output

The script creates a file named 'items.txt' containing the movie titles in ascending order, one per line.

## Usage

Simply run the script:
```bash
python main.py
```

## Note

The script uses an archived version of the webpage from Web Archive (May 18, 2020) to ensure consistent results, as the original page may have changed or been removed.

## Limitations

- Depends on the Web Archive's availability
- HTML structure must match the 2020 version of the page
- No error handling for network or parsing issues