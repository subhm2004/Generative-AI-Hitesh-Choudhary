# ============================================================
# FILE   : 08_global_scope.py
# TOPIC  : global keyword — file-level variable ko function se change karna
# FOLDER : 05_functions
# ============================================================
# 'global' keyword batata hai: ye variable file ke TOP level ka hai,
# function ke andar isko modify kar sakte ho.
# Bina 'global' likhe, andar assignment = naya LOCAL variable ban jata hai.

# Global variable — poori file mein accessible
chai_type = "Plain"

def front_desk():
    # Nested function — function ke andar doosra function
    def kitchen():
        global chai_type  # Ab chai_type global wala hai — LOCAL nahi banega
        chai_type = "Irnai"  # Global variable ko "Irnai" se replace kar do

    kitchen()  # Inner function call — global chai_type change ho jayega


front_desk()  # front_desk chalega → kitchen chalega → global update hoga
# Ab global chai_type "Irnai" ho chuka hai — "Plain" nahi raha
print("Final global chai: ", chai_type)
