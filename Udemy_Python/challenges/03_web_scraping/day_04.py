# ============================================================
# FILE: day_04.py
# TOPIC: Image download, regex, os.makedirs
# FOLDER: challenges/03_web_scraping
# CHALLENGE DAY: Day 04
# ============================================================
# Yeh challenge sikhata hai:
# - Scrape karke image URLs nikalna
# - requests.get(stream=True) = bade files chunk mein download
# - iter_content(8192) = 8KB chunks mein file likho (memory efficient)
# - re.sub() = regex se invalid filename characters hatao
# - os.makedirs() = folder create karo agar nahi hai
# - os.path.join() = safe file path banana
# ============================================================

"""
 Challenge: Download Cover Images of First 10 Books

Goal:
- Visit https://books.toscrape.com/
- Scrape the first 10 books listed on the homepage
- For each book, extract:
  • Title
  • Image URL

Then:
- Download each image
- Save it to a local `images/` folder with the filename as the book title (sanitized)

Example:
 Title: "A Light in the Attic"
 Saved as: images/A_Light_in_the_Attic.jpg

Bonus:
- Handle invalid filename characters
- Show download progress
"""
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re  # regular expressions - pattern matching

BASE_URL = "https://books.toscrape.com/"
IMAGE_DIR = "images"

# Book title ko safe filename mein convert karo
def sanitize_filename(title):
    # [^\w\-_. ] = sirf letters, numbers, -, _, ., space rakho, baaki hatao
    return re.sub(r'[^\w\-_. ]', '', title).replace(" ", "_")

# Image URL se file download karo
def download_image(img_url, filename):
    try:
        # stream=True = poori file ek saath memory mein nahi, chunks mein aayegi
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
        # 'wb' = write binary mode (images binary data hain)
        with open(filename, 'wb') as f:
            # 8192 bytes = 8KB chunks mein download karo
            for chunk in response.iter_content(8192):
                f.write(chunk)
    except Exception as e:
        print(f"Failed to download {filename} - {e}")


def scrape_and_download_images():
    url = BASE_URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")[:10]  # pehle 10 books

    # images/ folder banao agar exist nahi karta
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    for book in books:
        title = book.h3.a['title']  # title attribute se book name
        relative_img = book.find("img")["src"]  # relative image path
        img_url = urljoin(BASE_URL, relative_img)  # full image URL
        print(f"url - {img_url}")

        filename = sanitize_filename(title) + ".jpg"
        filepath = os.path.join(IMAGE_DIR, filename)  # images/filename.jpg
        print(f"filepath - {filepath}")

        print(f"Downloading: {title}")
        download_image(img_url, filepath)
    print("All 10 books covers downloaded to images/")

if __name__ == "__main__":
    scrape_and_download_images()
