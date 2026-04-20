names = ["Shubham", "Meera", "Sandeep", "Alina"]
bills = [5_000, 70, 100, 55]

# it is used to combine the lists 

for name, amount in zip(names, bills) :
    print(f"{name} paid {amount} rupees")