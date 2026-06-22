# ============================================================
# FILE: smart_thermostat.py
# TOPIC: NESTED if - if ke andar aur if (andhera andar andhera)
# FOLDER: 03_conditionals
# ============================================================
# Nested if = ek condition ke andar doosri condition
# Pehle device active hai check karo, phir temperature check karo
# ============================================================

device_status = "active"  # device on hai ya off
temperature = 38          # current temperature Celsius mein

# Pehla check: device chal raha hai?
if (device_status == "active"):
    # Device active hai - ab temperature check karo (nested if)
    if temperature > 35:
        print("High temperature alert!")  # 38 > 35 = True
    else:
        print("Temperature is normal")
else:
    print("Device is offline")  # device active nahi toh ye message
