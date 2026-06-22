# ============================================================
# FILE: mini_story_1.py
# TOPIC: String processing + boolean condition
# FOLDER: 03_conditionals
# ============================================================
# .strip() = string ke start/end se extra spaces hatao
# .lower() = sab chhote letters mein
# == "true" compare karke boolean True/False banao
# ============================================================

# User "true" ya "false" type karega
# .strip() spaces hataega, .lower() chhota karega, == "true" se boolean banega
kettle_boiled = input("Enter true or false: ").strip().lower() == "true"

# kettle_boiled ab True ya False hai
if (kettle_boiled):
    print("Kettle done! Time to make chai ☕")
else:
    print("Kettle not ready yet.")


# ----- .strip() DEMO -----
# NOTE: .strip() string ke start aur end se extra spaces hata deta hai
name = "   Shubham   "
print(name.strip())  # sirf "Shubham" - bina spaces ke
