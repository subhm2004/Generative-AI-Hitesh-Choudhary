# ============================================================
# FILE: 06_bgworker.py
# TOPIC: Daemon thread + async - background worker pattern
# FOLDER: 13_async_python
# ============================================================
# Daemon thread = background mein chalta hai, main program khatam = thread bhi band
# Non-daemon thread = main program uska wait karta hai
# Pattern: background logging/monitoring thread + async main work
# daemon=True = jab asyncio.run() khatam ho, background thread bhi band ho jayega
# ============================================================

import asyncio
import threading
import time

# Background worker - hamesha chalta rahega (daemon thread mein)
def background_worker():
    while True:  # infinite loop - tab tak jab tak program chale
        time.sleep(1)
        print(f"Logging the system health 🕰️")

# Async main kaam - orders fetch karna
async def fetch_orders():
    await asyncio.sleep(3)  # 3 second simulate - API call
    print("🎁 order fetched")

# Daemon thread start karo - background mein health log karega
# daemon=True = main program band = ye thread bhi automatically band
threading.Thread(target=background_worker, daemon=True).start()

# Async main chalao - 3 sec mein order fetch hoga
# Background thread is time mein 3 baar log print karega
asyncio.run(fetch_orders())
