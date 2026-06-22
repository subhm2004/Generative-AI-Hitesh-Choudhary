# ============================================================
# FILE: chapter_6.py
# TOPIC: STRINGS - text data, slicing, encoding/decoding
# FOLDER: 02_datatypes
# ============================================================
# String = text/likha hua data, quotes mein likhte hain " " ya ' '
# Strings IMMUTABLE hain - change nahi ho sakti, nayi string banti hai
# Slicing = string ka koi hissa kaat ke lena [start:end:step]
# ============================================================

# Strings and its methods (strings are immutable)

chai_type = "Masala chai"      # double quotes mein text
customer_name = "Shubham"

# f-string = variables ko string ke andar embed karna
print(f"Order for {customer_name} : {chai_type} please !")

# ----- STRING SLICING -----
# Syntax: string[start:end:step]
# start = kahan se shuru, end = kahan tak (end include NAHI hota!)
# step = har kitne character skip karke lo

chai_description = "Aromatic and Bold"

# [:8] = index 0 se 7 tak (8 characters) - "Aromatic"
print(f"First word: {chai_description[:8]}")

# [:8:2] = 0 se 7 tak, har 2nd character - "Aao" jaisa pattern
print(f"First word: {chai_description[:8:2]}")

# [12:] = index 12 se end tak - "Bold"
print(f"Last word: {chai_description[12:]}")

# [::-1] = POORI string REVERSE kar do! step=-1 matlab peeche se aage
print(f"Last word: {chai_description[::-1]}")  # "dloB dna citamorA"

# ----- ENCODING / DECODING -----
# Encoding = text ko bytes mein convert (computer memory ke liye)
# UTF-8 = sabse common encoding (Hindi, emoji sab support)

label_text = "Chai Spécial"  # special character é hai
encoded_label = label_text.encode("utf-8")  # bytes mein convert

print("\n")
print(f"Non Encoded label: {label_text}")     # normal text
print("\n")
print(f"Encoded label: {encoded_label}")     # b'Chai Sp\xc3\xa9cial' jaisa
print("\n")

# Decoding = bytes wapas text mein
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")  # wapas "Chai Spécial"
