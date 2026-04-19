kettle_boiled = input("Enter true or false: ").strip().lower() == "true"

if kettle_boiled:
    print("Kettle done! Time to make chai ☕")
else:
    print("Kettle not ready yet.")


# NOTE : .strip() ka matlab hota hai string ke start aur end se extra spaces (ya unwanted characters) hata dena
name = "   Shubham   "
print(name.strip())
