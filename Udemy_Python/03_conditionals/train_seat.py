# ============================================================
# FILE: train_seat.py
# TOPIC: match-case (Python 3.10+) - switch statement jaisa
# FOLDER: 03_conditionals
# ============================================================
# match-case = ek value ko multiple options se match karo
# case _ = default case (kuch match nahi hua)
# if-elif chain se zyada clean dikhta hai jab bahut options hon
# ============================================================

seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()

# match = seat_type ki value ko cases se compare karo
match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:  # underscore = default, koi match nahi hua
        print("Invalid seat type")
