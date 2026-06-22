# ============================================================
# FILE: 06_custom_except_two.py
# TOPIC: Custom Exception class - apni khud ki error type
# FOLDER: 11_exceptions
# ============================================================
# Custom exception = Exception class se inherit karke apna error type
# class OutOfIngredientsError(Exception) - apna meaningful error naam
# raise OutOfIngredientsError(...) - specific error throw karo
# except OutOfIngredientsError se sirf ye error pakdo
# ============================================================

# Apni custom exception class - Exception parent se inherit
class OutOfIngredientsError(Exception):
    pass  # body khali - bas naya error TYPE banaya

def make_chai(milk, sugar):
    # milk ya sugar 0 hai to ingredients khatam
    if milk == 0 or sugar == 0:
        # custom exception raise - generic Error se zyada clear message
        raise OutOfIngredientsError("Missing milk or sugar")
    print("chai is ready...")


# milk = 0 hai - OutOfIngredientsError raise hoga
make_chai(0, 1)
