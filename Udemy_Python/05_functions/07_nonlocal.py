# ============================================================
# FILE   : 07_nonlocal.py
# TOPIC  : nonlocal keyword — enclosing function ka variable change karna
# FOLDER : 05_functions
# ============================================================
# 'nonlocal' tab use hota hai jab INNER function ko OUTER function ka
# variable badalna ho — bina global banaye.
# Matlab: ek level upar wale scope ka variable modify karo.

# Global variable — file level par
chai_type = "ginger"

def update_order():
    # Ye outer function ka LOCAL variable hai
    chai_type = "Elaichi"

    def kitchen():
        # 'nonlocal' bolta hai: ye chai_type outer (update_order) wala hai, apna naya nahi
        nonlocal chai_type
        chai_type = "Kesar"  # Ab outer function ka chai_type "Kesar" ho jayega

    kitchen()  # Inner function call — nonlocal se outer ka variable update hoga
    print("After kitchen update", chai_type)  # Output: Kesar (outer wala change ho gaya)

# Poora flow chalao
update_order()
