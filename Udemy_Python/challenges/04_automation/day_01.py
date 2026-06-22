# =============================================================================
# FILE    : day_01.py
# TOPIC   : File Sorter by Type (Files ko type ke hisaab se sort karna)
# FOLDER  : challenges/04_automation/
# CHALLENGE DAY : Day 01
# =============================================================================
#
# Yeh script ek folder ke andar ki files ko unke extension (jaise .pdf, .jpg)
# ke basis par alag-alag subfolders mein move karti hai.
# Beginners ke liye: "automation" ka matlab hai computer ko khud kaam karwana!

"""
 Challenge: File Sorter by Type

Goal:
- Scan the current folder (or a user-provided folder)
- Move files into subfolders based on their type:
    - .pdf → PDFs/
    - .jpg, .jpeg, .png → Images/
    - .txt → TextFiles/
    - Others → Others/
- Create folders if they don't exist
- Ignore folders during the move

Teaches: File system operations, automation, file handling with `os` and `shutil`
"""

# os module = Operating System se baat karne ke liye (folders, files, paths)
import os

# shutil module = files ko move/copy/delete karne ke liye (shell utilities)
import shutil

# EXTENSION_MAP ek dictionary hai — har folder name ke saath uski file extensions list hai
# Dictionary = key-value pairs store karta hai, jaise phonebook mein naam → number
EXTENSION_MAP = {
    "PDFs": [".pdf"],                        # PDF files yahan jayengi
    "Images": [".png", ".jpeg", ".jpg"],     # Image files yahan jayengi
    "TextFiles": [".txt"]                    # Text files yahan jayengi
}


def get_destination_folder(filename):
    """
    Yeh function file ka naam leke batata hai ki woh kis folder mein jayegi.
    filename = file ka poora naam, jaise "report.pdf"
    """
    # os.path.splitext() file ko naam aur extension mein tod deta hai
    # [1] se hum extension lete hain (.pdf), .lower() se chhota letter banate hain
    ext = os.path.splitext(filename)[1].lower()

    # Har folder aur uski extensions list par loop chalao
    for folder, extensions in EXTENSION_MAP.items():
        # Agar file ki extension is list mein hai, toh yeh folder return karo
        if ext in extensions:
            return folder

    # Agar koi match nahi mila, toh "Others" folder mein daal do
    return "Others"


def sort_files(folder_path):
    """
    Yeh main function hai — diye gaye folder ki saari files ko sort karti hai.
    folder_path = woh folder jisko sort karna hai
  """
    # os.listdir() folder ke andar ki saari cheezon ke naam return karta hai
    for file in os.listdir(folder_path):
        # os.path.join() sahi path banata hai — Windows/Mac dono par kaam karta hai
        full_path = os.path.join(folder_path, file)

        # write a check if file name is "day_01.py" then ignore this file

        # os.path.isfile() check karta hai ki yeh ek file hai (folder nahi)
        if os.path.isfile(full_path):
            # Decide karo ki file kis destination folder mein jayegi
            dest_folder = get_destination_folder(file)
            # Destination folder ka poora path banao
            dest_path = os.path.join(folder_path, dest_folder)

            # os.makedirs() folder banata hai; exist_ok=True matlab pehle se hai toh error mat do
            os.makedirs(dest_path, exist_ok=True)

            #move the file
            # shutil.move() file ko purani jagah se nayi jagah shift karta hai
            shutil.move(full_path, os.path.join(dest_path, file))
            # f-string se message print karo — {file} aur {dest_folder} values insert hoti hain
            print(f"Moved : {file} -> {dest_folder}/")


# Yeh block tab chalta hai jab aap directly "python day_01.py" run karte ho
if __name__ == "__main__":
    # input() user se text leta hai; .strip() aage-peeche ki extra spaces hata deta hai
    folder = input("Enter the folder path or leave blank: ").strip()

    # Agar user ne kuch nahi likha (blank), toh current working directory use karo
    # or = agar left side khali hai toh right side use karo
    folder = folder or os.getcwd()

    # os.path.isdir() check karta hai ki yeh valid folder hai ya nahi
    if not os.path.isdir(folder):
        print("Invalid directory")
    else:
        # Sab theek hai — sorting shuru karo!
        sort_files(folder)
        print("✅ sorting completed")
