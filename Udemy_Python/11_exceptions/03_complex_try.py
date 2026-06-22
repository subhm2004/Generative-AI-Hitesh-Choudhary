# ============================================================
# FILE: 03_complex_try.py
# TOPIC: try, except, else, finally aur raise
# FOLDER: 11_exceptions
# ============================================================
# try = risky code
# except = error aayi to
# else = koi error NA aayi to (try success)
# finally = hamesha chalega - error ho ya na ho (cleanup ke liye)
# raise = khud se exception throw karo
# ============================================================

def serve_chai(flavor):
    try:
        # pehle flavor print karo
        print(f"Preparing {flavor} chai...")
        # agar flavor "unknown" hai to khud ValueError raise karo
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")  # raise = error throw
    except ValueError as e:
        # ValueError pakdi - e mein error message hai
        print("Error: ", e)
    else:
        # try mein koi error nahi aayi to ye block chalega
        print(f"{flavor} chai is served")
    finally:
        # hamesha chalega - success ho ya fail, cleanup/next step
        print("Next customer please")

# Valid flavor - try success, else chalega, finally bhi
serve_chai("masala")
# Unknown flavor - raise se ValueError, except pakdega, finally phir bhi chalega
serve_chai("unknown")
