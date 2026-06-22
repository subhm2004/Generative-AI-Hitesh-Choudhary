# ============================================================
# FILE: day_02.py
# TOPIC: CSS selectors, CSV export from scraped data
# FOLDER: challenges/03_web_scraping
# CHALLENGE DAY: Day 02
# ============================================================
# Yeh challenge sikhata hai:
# - CSS selectors = HTML elements dhundhne ka powerful tarika
# - soup.select("span.titleline > a") = specific elements target karo
# - Scraped data ko CSV file mein save karna
# - csv.DictWriter = dictionary list ko CSV mein likho
# - List slicing [:20] = sirf pehle 20 items lo
# ============================================================

"""
 Challenge: Hacker News Top Posts Scraper

Build a Python script that:
1. Fetches the HN homepage (news.ycombinator.com).
2. Extracts the top 20 post titles and URLs.
3. Saves the results into a CSV file (`hn_top20.csv`) with columns:
   - Title
   - URL
4. Handles network errors and uses a clean CSV structure.
"""
import csv
import requests
from bs4 import BeautifulSoup

HN_URL = "https://news.ycombinator.com/"
CSV_FILE = "hn_top20.csv"


def fetch_top_post():
    try:
        response = requests.get(HN_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Network error \n {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    # CSS selector: span.titleline ke andar direct child <a> tags
    post_links = soup.select("span.titleline > a")
    # print(post_links)

    posts = []
    # [:20] = sirf pehle 20 posts lo (top 20)
    for link in post_links[:20]:
        title = link.text.strip()  # link ka visible text = title
        url = link.get("href").strip()  # href attribute = URL
        # print(f"{title} \n {url} \n\n")
        posts.append({"title": title, "url": url})

    return posts


def save_to_csv(posts):
    if not posts:
        print("Noting to save")
        return
    
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        # DictWriter = har dict ek CSV row ban jata hai
        writer = csv.DictWriter(f, fieldnames=["title", "url"])
        writer.writeheader()
        writer.writerows(posts)  # saari rows ek saath likho

    print(f"✅ Saved Hacker News to {CSV_FILE}")



def main():
    print("Scrapping the HN portal....")
    posts = fetch_top_post()      
    print("Collected all data...")
    save_to_csv(posts)

if __name__ == "__main__":
    main()

