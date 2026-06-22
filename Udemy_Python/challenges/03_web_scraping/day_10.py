# ============================================================
# FILE: day_10.py
# TOPIC: PDF reading with PyMuPDF (fitz)
# FOLDER: challenges/03_web_scraping
# CHALLENGE DAY: Day 10
# ============================================================
# Yeh challenge sikhata hai:
# - PDF files se text extract karna
# - PyMuPDF (import fitz) = powerful PDF library (pip install pymupdf)
# - fitz.open() = PDF file kholo
# - page.get_text() = ek page ka saara text nikalo
# - Loop through all pages = poori PDF ka text collect karo
# - doc.close() = file resources free karo
# ============================================================

# fitz = PyMuPDF library ka module name (PDF handling)
import fitz

def read_pdf(file_path):
  # PDF document open karo
    doc = fitz.open(file_path)
    all_text = ""

    # Har page par loop chalao (0 se len(doc)-1 tak)
    for page_num in range(len(doc)):
        page = doc[page_num]  # page number se page object lo
        all_text += page.get_text()  # page ka text string mein add karo

    doc.close()  # PDF file band karo (memory leak se bachne ke liye)
    return all_text

if __name__ == "__main__":
    file_path = "test.pdf"
    try:
        content =read_pdf(file_path)
        print("-" * 30)
        print(content)
        print("-" * 30)
    except Exception as e:
        print("Failed to read pdf, change that method")
