# ============================================================
# FILE: day_10.py
# TOPIC: Caesar Cipher, ord(), chr(), modulo arithmetic
# FOLDER: challenges/01_utilities
# CHALLENGE DAY: Day 10
# ============================================================
# Yeh challenge sikhata hai:
# - Caesar Cipher = har letter ko fixed positions shift karo
# - ord(char) = character ka ASCII/Unicode number
# - chr(number) = number se character banao
# - Modulo % 26 = alphabet wrap-around (z ke baad a aata hai)
# - char.isalpha() = kya yeh letter hai? (spaces/punctuation skip)
# - Encrypt aur decrypt = same function, bas key positive ya negative
# ============================================================

"""
Building a Caesar Cipher

Challenge: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
   - Ask for a message and a numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If decrypting:
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

Bonus:
- Allow uppercase and lowercase letter handling
- Show a clean interface
"""

# Caesar cipher encrypt function
def encrypt(message, key):
    result = ""
    for char in message:
        if char.isalpha():  # sirf letters shift karo, baaki as-is
            # Uppercase letters 'A' se start, lowercase 'a' se
            base = ord('A') if char.isupper() else ord('a')
            # Shift formula: (position + key) % 26 = wrap around alphabet
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)  # number wapas character mein
        else:
            result += char  # space, comma, etc. unchanged
    return result

# Decrypt = encrypt with NEGATIVE key (reverse shift)
def decrypt(message, key):
    return encrypt(message, -key)


print("Secret message program")
choice = input("Do you want to E or D").strip().lower()

if choice == "e":
    text = input("Enter your message: \n")
    try:
        key = int(input("Enter a number between 1 and 25: "))
        encrypted = encrypt(text, key)
        print("Encrypted message: ")
        print(encrypted)
    except ValueError:
        print("Invalid key")
elif choice == 'd':
    text = input("Enter your encrypted message: \n")
    try:
        key = int(input("Enter a number between 1 and 25: "))
        decrypted = decrypt(text, key)
        print("Decrypted message: ")
        print(decrypted)
    except ValueError:
        print("Invalid key")
else:
    print("Invalid choice")
