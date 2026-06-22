# ============================================================
# FILE: 02_async_two.py
# TOPIC: asyncio.gather() - multiple async tasks parallel
# FOLDER: 13_async_python
# ============================================================
# asyncio.gather() = multiple coroutines EK SAATH chalao
# Jab sab I/O wait kar rahe hon, ek hi thread sab handle kar leta hai
# time.sleep() BLOCKING hai - async mein KABHI mat use karo!
# asyncio.sleep() NON-BLOCKING hai - doosre tasks chal sakte hain
# 3 chai parallel = total ~3 seconds, 9 seconds NAHI!
# ============================================================

import asyncio
import time

async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(3)  # non-blocking wait - thread free rehta hai
    # time.sleep(3)  # YE MAT USE KARO! Poora program block ho jayega
    print(f" {name} is ready...")

# main() bhi async function hai - andar await use kar sakte ho
async def main():
    # gather() = teeno brew() EK SAATH start karo
    # Sab parallel chalenge - total time = max(3,3,3) = 3 seconds
    await asyncio.gather(
        brew("Masala chai"),
        brew("Green chai"),
        brew("Ginger chai"),
    )

asyncio.run(main())
