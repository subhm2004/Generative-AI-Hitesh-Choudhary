sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12 # ek naya reference bana hai 
print(f"Second Initial sugar: {sugar_amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")

# hum is code me refereance change kr rhe hai value change nhi kr rhe hai (Immutable)

# The numbers are immutable we cannot change them only the referece can be changes not the values