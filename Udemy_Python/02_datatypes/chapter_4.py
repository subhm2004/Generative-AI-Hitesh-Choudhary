# Boolean (true = 1 and false = 0)

is_boiling = True # 1
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
print(f"Total actions: {total_actions}")

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
tea_added = True

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")
print(f"Can serve chai? {int(can_server)}")


# AND operator
print("AND operator examples:")
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

print("\nOR operator examples:")
# OR operator
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

print("\nNOT operator examples:")
# NOT operator
print(not True)         # False
print(not False)        # True