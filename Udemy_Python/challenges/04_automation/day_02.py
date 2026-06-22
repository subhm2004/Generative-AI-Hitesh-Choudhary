# =============================================================================
# FILE    : day_02.py
# TOPIC   : Batch Rename Files (Ek saath bahut saari files rename karna)
# FOLDER  : challenges/04_automation/
# CHALLENGE DAY : Day 02
# =============================================================================
#
# Yeh script ek folder ki files ko ek pattern mein rename karti hai,
# jaise: photo_1.jpg, photo_2.jpg, photo_3.jpg ...
# Pehle preview dikhati hai, phir user confirm karta hai.

"""
Challenge: Batch Rename Files in a Folder

Goal:
- Scan all files in a selected folder
- Rename them with a consistent pattern:
    e.g., "image_1.jpg", "image_2.jpg", ...
- Ask the user for:
    - A base name (e.g., "image")
    - A file extension to filter (e.g., ".jpg")
- Preview before renaming
- Optional: allow undo (save original names in a file)

Teaches: File iteration, string formatting, renaming, user input
"""

# os module — files aur folders ke saath kaam karne ke liye
import os


def batch_rename(folder, base_name, extension):
    """
    Folder ki files ko naye naam deti hai.
    folder     = kaunsa folder
    base_name  = naye naam ka prefix, jaise "image"
    extension  = sirf is extension wali files, jaise ".jpg"
    """
    # List comprehension — ek line mein filter + list banana
    # f.lower().endswith() se check karte hain ki file ki extension match karti hai ya nahi
    files = [f for f in os.listdir(folder) if f.lower().endswith(extension.lower())]

    # files.sort() — files ko alphabetical order mein rakhta hai (rename order consistent rahe)
    files.sort() # this will not do much

    # Agar koi file nahi mili toh yahan se return (function khatam)
    if not files:
        print("NO files found in dir")
        return

    # enumerate(files, start=1) — har file ke saath number bhi deta hai: 1, 2, 3...
    # Pehle PREVIEW dikhate hain — abhi rename nahi hua!
    for i, file in enumerate(files, start=1):
        # f-string se naya naam banate hain: base_name_1.jpg, base_name_2.jpg ...
        new_name = f"{base_name}_{i}{extension}"
        print(f"{file} => {new_name}")

    # User se confirmation lo — 'y' dabao toh rename hoga
    confirm = input("Press (y) to confirm or (n) to reject").strip().lower()

    # Agar user ne 'y' nahi dabaya, cancel karo
    if confirm != 'y':
        print("Cancel")
        return

    # Ab actually rename karo — dobara loop chalao
    for i, file in enumerate(files, start=1):
        # Purani file ka poora path
        src = os.path.join(folder, file)
        new_name = f"{base_name}_{i}{extension}"
        # Nayi file ka poora path (same folder mein, sirf naam badlega)
        dest = os.path.join(folder, new_name)
        # os.rename() file ka naam badal deta hai
        os.rename(src, dest)

    # Kitni files rename hui — len(files) se count milta hai
    print(f"Renamed {len(files)} files successfully")


# Script directly run hone par yeh block chalega
if __name__ == "__main__":
    # Folder path lo — blank chhodo toh current folder use hoga
    folder = input("Enter folder path or learn blank for current folder: ").strip() or os.getcwd()

    if not os.path.isdir(folder):
        print("Invalid folder")
    else:
        # User se base name aur extension poocho
        base_name = input("Enter base name for files: ").strip()
        extension = input("Enter extension name for files: ").strip()

        # Ab batch rename function call karo
        batch_rename(folder, base_name, extension)
