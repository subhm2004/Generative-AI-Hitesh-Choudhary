# ============================================================
# FILE: day_5.py
# TOPIC: Dictionary, string methods, for loop, list
# FOLDER: challenges/01_utilities
# CHALLENGE DAY: Day 5
# ============================================================
# Yeh challenge sikhata hai:
# - Dictionary = key-value pairs (word -> emoji mapping)
# - .split() se message ko words mein todo
# - .lower() aur .strip() se word clean karna
# - .get() method = safe dictionary lookup (key nahi mili to default return)
# - List mein words collect karke " ".join() se wapas string banana
# ============================================================

"""
 Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
  I love to code and drink tea when I'm happy.

Output:
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

"""

# Dictionary = key-value store (jaise real dictionary: word -> meaning)
# Yahan word -> emoji map hai
emoji_map_fun = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "tea": "🍵",
    "music": "🎵",
    "food": "🍕",
}

# User ka original message lo
message = input("Enter your message: ")

updated_words = []  # processed words yahan store honge

# message.split() = string ko spaces par todo, list of words milega
for word in message.split():
    # .lower() = lowercase karo (case-insensitive matching ke liye)
    # .strip(".,!?") = word ke start/end se punctuation hata do
    cleaned = word.lower().strip(".,!?")
    # .get(key, default) = dictionary se value lo; nahi mili to "" (empty string)
    emoji = emoji_map_fun.get(cleaned, "")
    if emoji:
        # Agar emoji mila to original word + emoji add karo
        updated_words.append(f"{word} {emoji}")
    else:
        # Emoji nahi mila to word as-is rakho
        updated_words.append(word)

# " ".join(list) = list ke items ko space se jod kar ek string banao
updated_message = " ".join(updated_words)
print("\n Enhanced message:\n")
print(updated_message)
