# ============================================================
# FILE: 07_daemon.py
# TOPIC: Daemon Thread - background thread jo auto-stop hota hai
# FOLDER: 13_async_python
# ============================================================
# Daemon thread = "background servant" - main program khatam = ye bhi band
# daemon=True set karo thread banate time
# Use case: monitoring, logging - jo main program ke saath band hona chahiye
# Yahan "Main program done" print hoga aur program EXIT - thread bhi band!
# Monitor thread sirf 1-2 baar print karega, phir program khatam
# ============================================================

import threading
import time

def monitor_tea_temp():
    while True:  # infinite loop - lekin daemon hai to program exit par band
        print(f"Monitoring tea temperature...")
        time.sleep(2)

# daemon=True = ye thread background servant hai
# Main program khatam = daemon thread automatically kill ho jayega
t = threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()

# Ye turant print hoga - daemon thread ka wait NAHI karenge
print("Main program done")
# Program yahan EXIT - daemon thread bhi band ho jayega
