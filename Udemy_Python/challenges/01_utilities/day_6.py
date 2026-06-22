# ============================================================
# FILE: day_6.py
# TOPIC: File Append Mode, datetime formatting, with open
# FOLDER: challenges/01_utilities
# CHALLENGE DAY: Day 6
# ============================================================
# Yeh challenge sikhata hai:
# - File mein data APPEND karna ("a" mode) - purana data safe rehta hai
# - datetime.datetime.now() se current date-time lena
# - strftime() se date ko readable format mein dikhana
# - Optional input handle karna (rating agar diya to add karo)
# - with open = file automatically close ho jati hai
# ============================================================

"""
 Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:
1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.txt`.
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.

Bonus:
- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.

Example:
📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5
"""

import datetime

# User se aaj kya seekha woh poocho
entry = input("What did you learn today ? ").strip()
# Optional rating - user skip bhi kar sakta hai
rating = input("⭐️ rate your productivity today (1-5, optional)").strip()

# datetime.now() = abhi ka exact date aur time (hours, minutes, seconds)
now = datetime.datetime.now()
# strftime = date/time ko custom format mein string banao
# %Y = year, %m = month, %d = day, %I = 12-hour, %M = minutes, %p = AM/PM
date_str = now.strftime("%Y-%m-%d - %I:%M %p")

# Journal entry ka formatted text banao
journal_entry = f"\n 🗓️ {date_str}\n{entry}"
# Agar rating diya hai (empty nahi hai) to entry mein add karo
if rating:
    journal_entry += f"\n Productivity Rating: {rating}\n"
# Separator line add karo taaki entries alag dikhein
journal_entry += "\n" + "-" * 50

# "a" mode = APPEND - file ke end mein naya data likho, purana data safe
# "w" mode hota to purani file delete ho jati!
with open("learning_journal.txt", "a", encoding="utf-8") as f:
    f.write(journal_entry)

print(f"\n your journal entry has been saved to 'learning_journal.txt' file. ")
