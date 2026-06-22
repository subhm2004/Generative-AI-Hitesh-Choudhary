# ============================================================
# FILE: day_11.py
# TOPIC: Sets, set operations, min(), functions
# FOLDER: challenges/01_utilities
# CHALLENGE DAY: Day 11
# ============================================================
# Yeh challenge sikhata hai:
# - Set = unique items ka collection (duplicate nahi hote)
# - set(name) = string ke unique characters
# - & operator = set INTERSECTION (dono mein common items)
# - min(score, 100) = score 100 se zyada nahi ho sakta (cap)
# - Function ko call karna aur result print karna
# ============================================================

"""
 Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themed message like:
   "You're like chai and samosa — made for each other!" or 
   "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""

# Compatibility score calculate karne wala function
def friendship_score(name1, name2):
    # Dono names ko lowercase karo (case-insensitive comparison)
    name1, name2 = name1.lower(), name2.lower()
    score = 0
    # set(name) = naam ke UNIQUE letters ka set banao
    # & = intersection = dono names mein COMMON letters
    shared_letters = set(name1) & set(name2)
    vowels = set('aeiou')  # vowels ka set

    # Har shared letter ke liye 5 points
    score += len(shared_letters) * 5
    # Shared vowels ke liye extra 10 points
    score += len(vowels & shared_letters) * 10
    
    # min(score, 100) = maximum 100 tak hi score (cap lagao)
    return min(score, 100)

def run_friendship_calculator():
    print("❤️ Friendship Compatibility calculator ❤️")
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")

    score = friendship_score(name1, name2)

    print(f"\n {score}")


run_friendship_calculator()
