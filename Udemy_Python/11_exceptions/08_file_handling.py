# ============================================================
# FILE: 08_file_handling.py
# TOPIC: File handling - finally aur with statement (safe file close)
# FOLDER: 11_exceptions
# ============================================================
# File open karte waqt error ho sakti hai - finally se hamesha close karo
# with statement = context manager - file auto close ho jati hai
# try/finally = manual close ensure karna
# with open(...) as file = recommended tareeka - cleaner code
# ============================================================

# Purana tareeka (commented) - manually open, try, finally mein close
# file = open("order.txt", "w")
# try:
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close()  # finally mein close - error ho ya na ho file band


# Recommended: with statement - block ke baad file automatically close
with open("order.txt", "w") as file:
    # "w" = write mode - file create/overwrite
    file.write("ginger tea - 4 cups")  # file mein likha
# yahan se bahar aate hi file close ho chuki hai - finally jaisa behavior
