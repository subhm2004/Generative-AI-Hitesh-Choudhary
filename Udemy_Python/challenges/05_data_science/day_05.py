# =============================================================================
# FILE    : day_05.py
# TOPIC   : YouTube Comments Dataset Banana (Toxic vs Supportive labels)
# FOLDER  : challenges/05_data_science/
# CHALLENGE DAY : Day 05
# =============================================================================
#
# Text classification ke liye fake YouTube comments banate hain —
# kuch "toxic" (negative), kuch "supportive" (positive).
# Baad mein ML model inhe classify karega!

import pandas as pd
import numpy as np
import random  # random.choice() — list se random item pick karna

# Toxic comments ki list — negative / rude messages
toxic_comments = [
    "You're so dumb", "This is trash", "Worst video ever", "Stop making content", "You sound horrible",
    "Clickbait title", "Can't believe people like this", "Waste of time", "Cringe content", "You're such a loser"
]

# Supportive comments — positive / encouraging messages
supportive_comments = [
    "This helped me a lot!", "You're amazing!", "Best tutorial I've seen", "Thanks for the content!",
    "Keep up the great work", "So clear and helpful", "Awesome explanation", "I learned a lot!", "Much appreciated!", "Legend!"
]

# data = khali list — hum isme dictionaries add karenge
data = []

# 50 baar loop — har baar ek toxic + ek supportive comment add karo (total 100 rows)
for i in range(50):
    # random.choice() list se ek random comment uthata hai
    data.append({"comment": random.choice(toxic_comments), "label": "toxic"})
    data.append({"comment": random.choice(supportive_comments), "label": "support"})

# List of dictionaries ko DataFrame (table) mein convert karo
df = pd.DataFrame(data)

# CSV file mein save — baad wale days is file ko padhenge
df.to_csv("youtube_comments.csv", index=False)
print("✅ Data saved successfully")
