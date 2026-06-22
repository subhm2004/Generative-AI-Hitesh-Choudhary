# ============================================================
# FILE: day_01.py
# TOPIC: Web scraping basics, BeautifulSoup, requests
# FOLDER: challenges/03_web_scraping
# CHALLENGE DAY: Day 01
# ============================================================
# Yeh challenge sikhata hai:
# - Web scraping = website se data automatically nikalna
# - requests.get() = webpage ka HTML download karna
# - BeautifulSoup = HTML parse karke tags dhundhna
# - soup.find_all("h2") = saare h2 heading tags nikalo
# - .get_text(strip=True) = tag ka text content (HTML tags hata kar)
# - raise_for_status() = HTTP error check (404, 500 etc.)
# ============================================================

"""
 Challenge: Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming language).

Your task is to:
1. Download the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.
"""

import requests  # HTTP requests - webpage download karne ke liye
from bs4 import BeautifulSoup  # HTML parser (pip install beautifulsoup4)

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

def get_h2_headers(url):
    try:
        # timeout=10 = 10 seconds mein response nahi aaya to error
        response = requests.get(url, timeout=10)
        # 4xx/5xx status codes par exception raise karo
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page: \n {e}")
        return []
    
    # response.text = webpage ka poora HTML as string
    # "html.parser" = built-in HTML parser
    soup = BeautifulSoup(response.text, "html.parser")
    # find_all = saare matching tags ki list return karo
    h2_tags = soup.find_all("h2")
    print(h2_tags)
    headers = []
    for tag in h2_tags:
        # get_text(strip=True) = tag ke andar ka text, extra spaces hata kar
        header_text = tag.get_text(strip=True)
        # "Contents" heading skip karo (Wikipedia table of contents)
        if header_text and header_text.lower() != "contents":
            headers.append(header_text)
    print(headers)

get_h2_headers(URL)
