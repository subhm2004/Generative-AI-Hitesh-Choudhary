# ============================================================
# FILE: 11_propert_decorators.py
# TOPIC: @property - getter, setter aur controlled attribute access
# FOLDER: 10_oops
# ============================================================
# @property = attribute jaisa access karo par andar method chale (getter)
# @age.setter = value set karte waqt validation/logic laga sakte ho
# _age = "private" convention (underscore) - direct access avoid karo
# raise ValueError = invalid value par error throw karo
# ============================================================

class TeaLeaf:
    # Constructor - internal _age store karte hain (underscore = internal use)
    def __init__(self, age):
        self._age = age  # asli value yahan store - direct access mat karo

    # @property = age ko read karte waqt ye method chalega (getter)
    @property
    def age(self):
        # bahar ko age + 2 dikhao (processing/validation example)
        return self._age + 2
    
    # @age.setter = leaf.age = 3 likhoge to ye method chalega (setter)
    @age.setter
    def age(self, age):
        # validation - sirf 1 se 5 ke beech allow
        if 1 <= age <= 5:
            self._age = age  # valid hai to store karo
        else:
            # invalid value par exception raise karo - program ruk jayega ya except pakdega
            raise ValueError("Tea leaf age must be between 1 and 5 years")
        
# Object banaya - _age = 2
leaf = TeaLeaf(2)
# leaf.age property getter call hoga - return 2+2 = 4
print(leaf.age)  # 4 print hoga (getter ne +2 kiya)
# Setter call - 6 invalid hai (1-5 ke bahar)
leaf.age = 6  # ValueError raise hoga - setter ne reject kiya
print(leaf.age)
