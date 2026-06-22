# ============================================================
# FILE: 02_multiprocessing.py
# TOPIC: Multiprocessing - alag-alag CPU cores use karna
# FOLDER: 12_threads_concurrency
# ============================================================
# Multiprocessing = har kaam ke liye ALAG process (alag Python interpreter)
# Threads se farq: processes ko alag memory milti hai, GIL se affect nahi hote
# CPU-heavy kaam (calculations) ke liye multiprocessing threads se better hai
# if __name__ == "__main__": ZAROORI hai Windows/Mac par - warna error aayega
# ============================================================

from multiprocessing import Process  # Process class - alag process banane ke liye
import time

# Har process ye function alag se chalayega
# name parameter se har chai maker ka naam alag hoga
def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)  # 3 second simulate - chai ban rahi hai
    print(f"End of {name} chai brewing")

# __name__ == "__main__" check ZAROORI hai multiprocessing mein!
# Iske bina child processes infinite loop mein phas sakte hain
if __name__ == "__main__":
    # List comprehension se 3 processes banao
    # args=(f"Chai Maker #{i+1}",) - comma ZAROORI hai tuple ke liye!
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
        for i in range(3)  # 3 alag processes - 3 alag chai makers
    ]

    # Sab processes start karo - teeno EK SAATH chalenge (alag CPU cores par)
    for p in chai_makers:
        p.start()

    # Har process khatam hone ka wait karo
    for p in chai_makers:
        p.join()

    print("All chai served")
