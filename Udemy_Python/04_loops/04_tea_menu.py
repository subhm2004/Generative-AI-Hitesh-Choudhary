menu = ["Green", "Lemon", "Spiced", "Mint"]

# Jab tumhe list ke items ke saath unka index bhi chahiye hota hai tab hum use krte hai enumerate ko 
for idx, item in enumerate(menu): # indexing 0 se start hogi 
    print(f"{idx} : {item} chai")

print("\n")

for index , item in enumerate(menu, start = 1): # indexing 1 se start hogi
    print(f"{index} : {item} ")

print("\n")