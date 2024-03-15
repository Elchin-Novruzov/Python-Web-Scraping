# Web Scraping with Python and Beautiful Soup 4

This Python project utilizes the Beautiful Soup 4 library for web scraping. It extracts data from the busaat.az website, specifically scraping 24 news articles at a time. Additionally, it provides functionality to export the scraped data to an Excel document.

## Prerequisites

Before running the script, make sure you have Python 3.x installed on your system. You'll also need to install the Beautiful Soup 4 library. You can do this via pip:

```
pip install beautifulsoup4
```


## How to Run

To run the web scraper, follow these steps:

1. Install the Beautiful Soup 4 library if you haven't already (see Prerequisites above).
2. Clone or download this repository to your local machine.
3. Navigate to the directory containing the `scraping_script.py` file.
4. Open a terminal or command prompt in that directory.
5. Run the script using the following command:

```
python main.py
```


## Features

- Scrapes 24 news articles from the busaat.az website.
- Extracts data such as date, name, and link for each news article.
- Saves the extracted data to an Excel document for further analysis.

## Output Format

The scraped data is exported to an Excel document with the following format:

<table>
  <tr>
    <th>Date</th>
    <th>Title</th>
    <th>Link</th>
  </tr>
  <tr>
    <td>DD-MM-YYYY</td>
    <td>Article title</td>
    <td>example.com/news/link</td>
  </tr>
  <tr>
    <td>DD-MM-YYYY</td>
    <td>Article title</td>
    <td>example.com/news/link</td>
  </tr>
  <tr>
    <td>...</td>
    <td>...</td>
    <td>...</td>
  </tr>
</table>
