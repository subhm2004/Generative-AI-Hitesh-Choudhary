# ============================================================
# FILE   : 02_complex.py
# TOPIC  : Bade kaam ko chhote functions mein todna (decomposition)
# FOLDER : 05_functions
# ============================================================
# Jab koi kaam bahut bada ho, use chhote-chhote functions mein todo.
# Har function ek chhota kaam kare — phir ek main function sabko call kare.

# Pehla chhota function — sirf sales data fetch karta hai
def fetch_sales():
    print("Fetching the sales data")


# Doosra function — valid sales ko filter karta hai
def filter_valid_sales():
    print("Filtering valid sales data")

# Teesra function — data ko summarize (short summary) karta hai
def summarize_data():
    print("Summarizing sales data")


# Ye MAIN function hai — ye teeno functions ko ek saath call karta hai
# Matlab: bada kaam = chhote functions ka sequence
def generate_report():
    fetch_sales()           # pehle data lao
    filter_valid_sales()    # phir filter karo
    summarize_data()        # phir summarize karo
    print("Report is ready")  # sab ho gaya toh message dikhao


# Ab poora report generate karo — ek hi line se sab functions chal jayenge
generate_report()
