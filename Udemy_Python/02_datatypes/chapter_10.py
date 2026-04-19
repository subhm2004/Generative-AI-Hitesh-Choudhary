# Dictionary in python (mutable hai dictionary bhi)
chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

customer_note = chai_order.get("size", "NO Note")
print(f"customer_note is: {customer_note}")


my_dictionary = {
    "name " : "Shubham",
    "age" : 22,
    "height" : "5'9"
}
print(my_dictionary)
for i in my_dictionary.keys(): # my_dictionary.values() ya fir my_dictionary.items()
    # print(i, my_dictionary[i])
    # print(f"{i} : {my_dictionary[i]}")
    # print(f"{i} : {my_dictionary.get(i)}")
    print(i)

del my_dictionary["age"]
print(my_dictionary)

# my_dictionary.clear() # sab saaf kr dega 
print(my_dictionary)

my_dictionary_2 = {
    "name_2 " : "hardik",
    "age" : 22,
    "height_2" : "5'8"    
}
my_dictionary.update(my_dictionary_2)
print(my_dictionary)
print("\n")
