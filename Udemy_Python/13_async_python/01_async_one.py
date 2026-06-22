# ============================================================
# FILE: 01_async_one.py
# TOPIC: Async/Await basics - pehla async function
# FOLDER: 13_async_python
# ============================================================
# Async/Await = ek hi thread mein multiple I/O tasks efficiently handle karna
# async def = ye function asynchronous hai (coroutine banata hai)
# await = yahan RUKO jab tak ye kaam complete na ho, lekin thread FREE rehta hai
# asyncio.sleep() = time.sleep() jaisa but NON-BLOCKING (thread ko free karta hai)
# asyncio.run() = async program start karne ka entry point
# ============================================================

import asyncio  # Python ka built-in async module

# async def = coroutine function - andar await use kar sakte ho
async def brew_chai():
    print("Brwing chai...")
    await asyncio.sleep(2)  # 2 second wait BUT thread block NAHI hoga
    # Dusre async tasks is time mein chal sakte hain!
    print("Chai is ready")

# asyncio.run() = event loop start karo aur coroutine chalao
# Ye program ka entry point hai async code ke liye
asyncio.run(brew_chai())
