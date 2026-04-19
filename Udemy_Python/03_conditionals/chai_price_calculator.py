cup = input("Choose your cup size (small/medium/large): ").lower() #chaining ki hai yha pr

if cup == "small":
    print("Price is 10 rupees")
elif cup == "medium":
    print("Price is 15 rupees")
elif cup == "large":
    print("price is 20 rupees")
else:
    print("Unknown cup size")