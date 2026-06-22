# ============================================================
# FILE: 08_non_daemon.py
# TOPIC: Non-Daemon Thread - main program thread ka wait karta hai
# FOLDER: 13_async_python
# ============================================================
# Non-daemon (default) = main program thread KHATAM hone ka WAIT karega
# daemon=True nahi diya = default non-daemon thread
# Program tab tak chalega jab tak ye infinite loop wala thread chale
# Compare karo 07_daemon.py se - wahan program turant band, yahan nahi!
# Ctrl+C se manually band karna padega
# ============================================================

import threading
import time

def monitor_tea_temp():
    while True:  # infinite loop - program yahan ATKA rahega
        print(f"Monitoring tea temperature...")
        time.sleep(2)

# daemon=True NAHI diya = non-daemon thread (default behavior)
# Main program is thread ka wait karega - program band NAHI hoga!
t = threading.Thread(target=monitor_tea_temp)
t.start()

print("Main program done")
# Program yahan RUKEGA - non-daemon thread chal raha hai
# Ctrl+C dabao band karne ke liye
