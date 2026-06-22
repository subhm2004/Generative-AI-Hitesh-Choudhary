# ============================================================
# FILE: 06_tea-temperature.py
# TOPIC: while loop - jab tak condition True, tab tak chalao
# FOLDER: 04_loops
# ============================================================
# while = condition True hai tab tak loop chalta rahega
# for se farq: for fixed times, while jab tak condition true
# Dhyan rakho: infinite loop na ban jaye! (condition kabhi False honi chahiye)
# ============================================================

temperature = 40  # shuruat mein 40 degree

# Jab tak temperature 100 se KAM hai, loop chalao
while (temperature < 100):
    print(f"Current temperature: {temperature}")
    temperature += 15  # har baar 15 degree badhao (shortcut: temp = temp + 15)

# Loop khatam jab temperature >= 100 ho gaya
print("Tea is ready to boil")
