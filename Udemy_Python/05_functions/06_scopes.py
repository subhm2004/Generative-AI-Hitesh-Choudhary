# ============================================================
# FILE   : 06_scopes.py
# TOPIC  : Variable Scope — local, enclosing, aur global
# FOLDER : 05_functions
# ============================================================
# SCOPE matlab: variable kahan-kahan accessible (dikhayi deta) hai.
# Teen types: LOCAL (function ke andar), ENCLOSING (outer function), GLOBAL (poori file)

# --- Part 1: LOCAL SCOPE ---
# Function ke ANDAR banaya variable sirf us function ke andar dikhta hai
def serve_chai():
    chai_type = "Masala" # local scope — sirf serve_chai() ke andar valid hai
    print(f"Inside function: {chai_type}")  # Andar "Masala" print hoga


# Ye GLOBAL variable hai — poori file mein accessible
chai_type = "Lemon"
serve_chai()  # Function call — andar wala local "Masala" use hoga
# Bahar wala global "Lemon" change NAHI hua — local alag hai!
print(f"Outside function: {chai_type}")  # Output: Lemon (global wala)

print("\n")  # Khali line — output alag dikhane ke liye

# --- Part 2: ENCLOSING SCOPE (nested functions) ---
# Function ke andar doosra function — inner function outer ke variables dekh sakta hai
def chai_counter():
    chai_order = "lemon" # Enclosing scope — outer function ka variable
    def print_order():
        chai_order = "Ginger"  # Ye LOCAL hai inner function ke liye — outer ko change NAHI karega
        print("Inner_loop:", chai_order)  # Inner ka apna "Ginger"
    print_order()  # Inner function call
    print("Outer_loop: ", chai_order)  # Outer ka ab bhi "lemon" — inner ne change nahi kiya

chai_order = "Tulsi" # Global — poori file level par
chai_counter()
print("Global :", chai_order)  # Global ab bhi "Tulsi" — kisi ne change nahi kiya
