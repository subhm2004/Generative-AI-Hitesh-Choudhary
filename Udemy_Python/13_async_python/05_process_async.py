# ============================================================
# FILE: 05_process_async.py
# TOPIC: ProcessPoolExecutor - CPU work ko async mein run karna
# FOLDER: 13_async_python
# ============================================================
# ThreadPoolExecutor = I/O blocking ke liye (threads)
# ProcessPoolExecutor = CPU-heavy kaam ke liye (processes, GIL bypass)
# run_in_executor(process_pool, func, arg) = function alag PROCESS mein chalega
# if __name__ == "__main__" ZAROORI hai processes ke liye
# Example: encryption, image processing - CPU intensive tasks
# ============================================================

import asyncio
from concurrent.futures import ProcessPoolExecutor

# CPU kaam - string reverse karna (example ke liye)
def encrypt(data):
    return f"🔒 {data[::-1]}"  # [::-1] = string ulta kar do

async def main():
    loop = asyncio.get_running_loop()
    # ProcessPoolExecutor = alag processes - GIL se free!
    with ProcessPoolExecutor() as pool:
        # encrypt function alag PROCESS mein chalega
        result = await loop.run_in_executor(pool, encrypt, "credit_card_1234")
        print(f"{result}")

if __name__ == "__main__":
    asyncio.run(main())
