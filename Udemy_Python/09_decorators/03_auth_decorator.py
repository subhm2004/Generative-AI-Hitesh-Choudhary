# ============================================================
# FILE: 03_auth_decorator.py
# TOPIC: AUTH DECORATOR - permission check before function runs
# FOLDER: 09_decorators
# ============================================================
# Authentication/Authorization decorator = access control lagata hai
# Function chalne se PEHLE check karo ki user allowed hai ya nahi
# Agar allowed nahi to function run mat karo, message do aur None return karo
# Real apps mein login/role check decorators se hota hai
# return None = kuch return nahi karna (function skip ho gaya)
# ============================================================

# build authentication with decorator
from functools import wraps

# require_admin = sirf "admin" role wale users ko allow karta hai
def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        # user_role != "admin" = agar role admin NAHI hai
        if user_role != "admin":
            print("Access denied: Admins only")
            return None  # function mat chalao, None wapas karo
        else:
            # admin hai to asli function chalao aur uska result return karo
            return func(user_role)
    return wrapper

# @require_admin = acess_tea_inventory ko admin check se wrap karo
@require_admin
def acess_tea_inventory(role):
    print("Access granted to tea inventory")

# "user" role = admin nahi -> Access denied print hoga, function nahi chalega
acess_tea_inventory("user")

# "admin" role = allowed -> asli function chalega, inventory access milega
acess_tea_inventory("admin")
