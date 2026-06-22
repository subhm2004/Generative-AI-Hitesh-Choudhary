# ============================================================
# FILE: 04_thread_async.py
# TOPIC: run_in_executor - blocking code ko async mein run karna
# FOLDER: 13_async_python
# ============================================================
# Kabhi-kabhi purana BLOCKING code hota hai (jaise time.sleep, database)
# run_in_executor() = blocking function ko alag THREAD mein chalao
# Async event loop block NAHI hoga - thread background mein kaam karega
# ThreadPoolExecutor = thread pool manage karta hai
# Pattern: async code + blocking library = executor use karo
# ============================================================

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

# Ye BLOCKING function hai - time.sleep poora thread rok deta hai
def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(3) # Blocking operation - 3 second wait
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_running_loop()  # current event loop lo
    # ThreadPoolExecutor = threads ka pool - blocking kaam yahan daalo
    with ThreadPoolExecutor() as pool:
        # run_in_executor = check_stock ko THREAD mein chalao, result await karo
        # Async loop FREE rehta hai jab thread kaam kar raha hai
        result = await loop.run_in_executor(pool, check_stock, "Masala chai")
        print(result)

asyncio.run(main())
