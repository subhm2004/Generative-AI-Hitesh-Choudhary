# ============================================================
# FILE: day_9.py
# TOPIC: Countdown timer, time.sleep(), divmod(), range()
# FOLDER: challenges/01_utilities
# CHALLENGE DAY: Day 9
# ============================================================
# Yeh challenge sikhata hai:
# - time module = delays aur timers ke liye
# - time.sleep(1) = 1 second ruko (countdown effect)
# - range(seconds, 0, -1) = reverse countdown (seconds se 1 tak)
# - divmod(remaining, 60) = minutes aur seconds alag karo
# - f"{mins:02}:{secs:02}" = MM:SS format (02 = 2 digits with leading zero)
# - end="\r" = same line par overwrite (live countdown effect)
# ============================================================

"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time  # sleep() aur timing ke liye

# Input validation loop - tab tak poocho jab tak valid seconds na milein
while True:
    try:
        seconds = int(input("⏰ Enter the time in seconds: "))
        if seconds < 1:
            print("Please enter a number greater than 0")
            continue  # loop ke start par wapas jao, dobara input lo
        break  # valid input mil gaya, loop se bahar niklo
    except ValueError:
        print("Invalid input, please enter a whole number")

print("\n 🔔 Timer started...")
# range(start, stop, step) = seconds se 1 tak, -1 step (countdown)
for remaining in range(seconds, 0, -1):
    # divmod = division + remainder ek saath (e.g. 125 -> 2 mins, 5 secs)
    mins, secs = divmod(remaining, 60)
    # :02 = 2 digit format with leading zero (05, not 5)
    time_format = f"{mins:02}:{secs:02}"
    # end="\r" = carriage return - same line par update (timer effect)
    print(f"🕰️ Time left: {time_format} ", end="\r")
    time.sleep(1)  # 1 second wait karo phir next iteration

print("\n Time's up! Take a break or move on to next task.")
#print("\a") # optional; makes a beep sound (\a = ASCII bell character)
