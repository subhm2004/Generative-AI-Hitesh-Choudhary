#NOTE: Loop me [Start , End) tak chalta hai 

n = int(input("Enter a number:"))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

print("\n")

# inverse table 
m = int(input("Enter a number:"))
for i in range(10, 0, -1): # Ulti loop chal rhi hai 10 se 1  taki 
    print(f"{m} x {i} = {m*i}")

print("\n")

# count numbers from reverse 
num = int(input("Enter a number:")) 
for i in range(num, 0, -1):
    print(i)

print("\n")

# skip krke bhi chalti h loops 
for i in range(1, 10, 2):
    print(i)