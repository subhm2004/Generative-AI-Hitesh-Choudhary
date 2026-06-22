# ============================================================
# FILE: day_06.py
# TOPIC: PIL/Pillow image creation, textwrap
# FOLDER: challenges/03_web_scraping
# CHALLENGE DAY: Day 06
# ============================================================
# Yeh challenge sikhata hai:
# - Scrape + Image generation combine karna
# - PIL (Pillow) = Python mein images create/edit karne ke liye
# - Image.new() = nayi blank image banao
# - ImageDraw.Draw() = image par text/shapes draw karo
# - textwrap.fill() = lambi text ko multiple lines mein wrap karo
# - image.save() = PNG file mein save karo
# ============================================================

"""
 Challenge: Quote of the Day Image Maker

Goal:
- Scrape random quotes from https://quotes.toscrape.com/
- Extract quote text and author for the first 5 quotes
- Create an image for each quote using PIL
- Save images in 'quotes/' directory using filenames like quote_1.png, quote_2.png, etc.


"""
import os
import requests
import textwrap  # long text ko lines mein wrap karne ke liye
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont  # pip install Pillow

BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_DIR = "quotes"

def fetch_quotes():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select("div.quote")  # har quote ek div.quote mein hai

    quote_data = []

    for q in quotes[:5]:  # pehle 5 quotes
        # strip("""") = opening/closing quote marks hata do
        text = q.find("span", class_="text").text.strip(""")
        author = q.find("small", class_="author").text

        quote_data.append((text, author))  # tuple store karo

    return quote_data

def create_image(text, author, index):
    width, height = 800, 400
    backgroud_color = "#f8d77f"  # warm yellow background
    text_color = "#262626"       # dark gray text

    # RGB mode mein nayi image banao with background color
    image = Image.new("RGB", (width, height), backgroud_color)
    draw = ImageDraw.Draw(image)  # drawing object banao

    font = ImageFont.load_default()  # default system font
    author_font = ImageFont.load_default()

    # width=60 = har line mein max 60 characters
    wrapped = textwrap.fill(text, width=60)
    author_text = f"- {author}"

    y_text = 60  # text ki starting y position
    draw.text((40, y_text), wrapped, font=font, fill=text_color)
    # wrapped.count('\n') = kitni lines hain, spacing adjust karo
    y_text += wrapped.count('\n') * 15 + 40
    draw.text((500, y_text), author_text, font=font, fill=text_color)

    # save image
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    filename = os.path.join(OUTPUT_DIR, f"quote_{index+1}.png")
    image.save(filename)
    print(f"✅ saved: {filename}")


def main():
    quotes = fetch_quotes()
    # enumerate = index + (text, author) tuple
    for idx, (text, author) in enumerate(quotes):
        create_image(text, author, idx)

if __name__ == "__main__":
    main()
