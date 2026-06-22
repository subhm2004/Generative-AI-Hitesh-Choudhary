# ============================================================
# FILE: day_03.py
# TOPIC: Multi-page web crawling, urljoin, JSON export
# FOLDER: challenges/03_web_scraping
# CHALLENGE DAY: Day 03
# ============================================================
# Yeh challenge sikhata hai:
# - Web crawling = multiple pages par jaake data collect karna
# - "Next" button follow karke pages traverse karna
# - urljoin() = relative URL ko absolute URL mein convert karo
# - while loop se tab tak scrape karo jab tak target count na mile
# - Scraped data ko JSON file mein save karna
# ============================================================

"""
 Challenge: Scrape Books To Scrape (70 Books)

Goal:
- Visit https://books.toscrape.com/
- Scrape each book's:
  • Title 
  • Price 

You must:
- Crawl through multiple pages using the "next" button until you collect 70 books.
- Save the data to a JSON file: books_data.json
- Handle network errors gracefully.

Bonus:
- Track how many books scraped
- Print progress as you collect pages
"""


import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin  # relative URLs ko absolute banane ke liye

BASE_URL = "https://books.toscrape.com/"
START_PAGE = "catalogue/page-1.html"
OUTPUT_PAGE = "books_data.json"
TARGET_COUNT = 70

# Ek page scrape karo aur next page URL return karo
def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Failed to fetch url")
        return [], None
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    # CSS selector: har book article tag
    for article in soup.select("article.product_pod"):
        title_tag = article.select_one("h3 > a")  # select_one = pehla match
        title = title_tag.get("title")  # title attribute mein full book name
        price = article.select_one("p.price_color").text.strip()
        # print(f"{title} - {price}")
        books.append({"title":title, "price":price})

    # "Next" button dhundho - agar hai to next page URL banao
    next_link = soup.select_one("li.next > a")
    next_url = urljoin(url, next_link.get("href")) if next_link else None

    return books, next_url


def main():
    collected = []  # saari books yahan collect hongi
    # urljoin = BASE_URL + START_PAGE = full first page URL
    current_url = urljoin(BASE_URL, START_PAGE)

    # Tab tak crawl karo jab tak 70 books na mil jayein ya pages khatam
    while len(collected) < TARGET_COUNT and current_url:
        print(f"Scrapping: {current_url}")
        books, next_url = scrape_page(current_url)
        collected.extend(books)  # is page ki books main list mein jod do
        current_url = next_url  # agle page par jao

    # Sirf pehle 70 books rakho (zyada scrape ho gayi to trim)
    collected = collected[:TARGET_COUNT]
    print(f"scrapped {len(collected)} books")

    with open(OUTPUT_PAGE, "w", encoding="utf-8") as f:
        json.dump(collected, f, indent=2)

    print(f"Data save to {OUTPUT_PAGE}")


if __name__ == "__main__":
    main()
