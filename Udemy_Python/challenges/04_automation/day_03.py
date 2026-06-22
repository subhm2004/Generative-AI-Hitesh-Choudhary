# =============================================================================
# FILE    : day_03.py
# TOPIC   : Auto File Organizer with Watchdog (Folder ko live monitor karna)
# FOLDER  : challenges/04_automation/
# CHALLENGE DAY : Day 03
# =============================================================================
#
# Yeh script Downloads folder ko "watch" karti hai — jaise hi nayi file aati hai,
# automatically sahi subfolder mein move ho jati hai.
# Real-time automation = program background mein chalta rehta hai!

"""
 Challenge: Auto File Organizer with Watchdog

Goal:
- Monitor a folder (e.g., Downloads/Desktop)
- When a new file is added:
    - Move PDFs to /PDFs
    - Move Images to /Images
    - Move ZIP files to /Archives
    - Everything else goes to /Others

Teaches: Folder monitoring, real-time automation, event-driven design
Tools: watchdog, shutil, os
"""

import os
import shutil

# watchdog library — folder mein changes (nayi file, delete, etc.) detect karti hai
from watchdog.events import FileSystemEventHandler  # Events handle karne ke liye class
from watchdog.observers import Observer              # Folder ko observe karne wala

# WATCH_FOLDER = hum kaunsa folder monitor karenge
# expanduser("~/Downloads") = user ke home folder ka Downloads path (Mac/Linux)
WATCH_FOLDER = os.path.expanduser("~/Downloads")

# FILE_DESTS = extension → folder name ka map (dictionary)
# .pdf wali file PDFs folder mein, .jpg/.png Images mein jayegi
FILE_DESTS = {
    '.pdf': 'PDFs',
    '.jpg': 'Images',
    '.png': 'Images',
}


# FileSystemEventHandler se inherit karte hain — matlab hum apna custom handler banate hain
# "Event-driven" = kuch hua tabhi code chalega (nayi file aayi → on_created chalega)
class FileMoverHandler(FileSystemEventHandler):
    def on_created(self, event):
        """
        Jab bhi koi nayi cheez create hoti hai folder mein, yeh function automatically chalta hai.
        event = details about kya create hua (file ya folder?)
        """
        # Agar naya folder bana hai, ignore karo — sirf files move karni hain
        if event.is_directory:
            return

        # event.src_path = nayi file ka poora path
        filepath = event.src_path
        # File ka extension nikalo (.pdf, .jpg, etc.)
        ext = os.path.splitext(filepath)[1].lower()

        # Dictionary se destination folder dhundho; nahi mila toh 'Others'
        dest_folder = FILE_DESTS.get(ext, 'Others')
        # Poora destination path banao
        full_dest = os.path.join(WATCH_FOLDER, dest_folder)
        # Destination folder create karo agar nahi hai
        os.makedirs(full_dest, exist_ok=True)
        # File kahan move hogi — destination + file ka naam
        move_to = os.path.join(full_dest, os.path.basename(filepath))

        try:
            # File ko move karo
            shutil.move(filepath, move_to)
            # print message
        except:
            # Koi error aayi (file locked ho, permission na ho) toh message dikhao
            print("Failed to move")


# Main program — script run hone par yeh chalega
if __name__ == "__main__":
    print(f"Watching folder: {WATCH_FOLDER}")

    # Apna custom event handler banayo
    event_handler = FileMoverHandler()
    # Observer object — yeh actually folder ko watch karta hai
    observer = Observer()
    # Handler ko folder par schedule karo; recursive=False matlab sirf top level, subfolders nahi
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    # Observer start — ab monitoring shuru!
    observer.start()

    try:
        # Infinite loop — program chalta rehta hai jab tak Ctrl+C na dabao
        while True:
            pass  # pass = kuch mat karo, bas wait karo
    except KeyboardInterrupt:
        # User ne Ctrl+C dabaya — monitoring band karo
        observer.stop()

    # Observer thread ko properly khatam hone do
    observer.join()
