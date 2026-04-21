def serve_chai():
    chai_type = "Masala" # local scope
    print(f"Inside function: {chai_type}")


chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}")

print("\n")

def chai_counter():
    chai_order = "lemon" # Enclosing scope
    def print_order():
        chai_order = "Ginger"
        print("Inner_loop:", chai_order)
    print_order()
    print("Outer_loop: ", chai_order)

chai_order = "Tulsi" # Global
chai_counter()
print("Global :", chai_order)