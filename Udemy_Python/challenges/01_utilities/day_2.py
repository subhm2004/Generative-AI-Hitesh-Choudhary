# ============================================================
# FILE: day_2.py
# TOPIC: Functions, if-elif, File Writing, textwrap
# FOLDER: challenges/01_utilities
# CHALLENGE DAY: Day 2
# ============================================================
# Yeh challenge sikhata hai:
# - User se multiple inputs lena
# - Function define karna aur return value use karna
# - if-elif chain se different styles handle karna
# - File mein data save karna (with open ... "w")
# - textwrap.dedent() se formatted text print karna
# ============================================================

"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""

# textwrap module = text formatting ke liye (dedent extra spaces hata deta hai)
import textwrap

# User se saari details ek ek karke lo
name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
passion = input("Enter your passion in one line: ").strip()
emoji = input("Enter your favourite emoji: ").strip()
website = input("Enter your website: ").strip()

# User ko style options dikhao
print("\nChoose your style: ")
print("1. Simple lines ")
print("2. Vertical flair ")
print("3. Emoji sandwich ")

style = input("Enter 1, 2 or 3: ").strip()

# Function = reusable code block jo ek kaam karta hai
# style parameter ke basis par alag-alag bio format return karta hai
def generate_bio(style):
    if style == "1":
        # Style 1: Simple horizontal layout with pipe separator
        return f"{emoji} {name} | {profession} \n💡 {passion}\n {website}" 
    elif style == "2":
        # Style 2: Vertical layout with fire emoji flair
        return f"{emoji} {name}\n {profession}🔥\n {passion} \n {website}🔥"
    elif style == "3":
        # Style 3: Emoji sandwich - emoji*3 = emoji ko 3 baar repeat karo
        return f"{emoji*3}\n {name} - {profession}\n {passion}\n {website} \n {emoji*3}"
    
# Function call - user ke chosen style ke hisaab se bio generate karo
bio = generate_bio(style)

print("\nYour stylish bio:\n")
print("*" * 50)
# dedent() = string ke common leading whitespace hata deta hai (clean print)
print(textwrap.dedent(bio))
print("*" * 50)

# User se poocho ki file mein save karna hai ya nahi
save = input("Do you want to save this bio to a text file? (y/n): ").lower()

if save == 'y':
    # name ko lowercase karo, spaces ko underscore se replace karo (safe filename)
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    # with open = file automatically close ho jati hai block ke baad
    # "w" mode = write (naya file banao ya purana overwrite karo)
    # encoding="utf-8" = emoji aur special characters sahi save honge
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print("file saved")
