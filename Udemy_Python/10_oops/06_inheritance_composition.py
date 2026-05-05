# Base class (Parent class) jo ek normal chai ke liye basic functionality provide karta hai.
# Ye ek blueprint hai baaki sabhi types ki chai ke liye.
class BaseChai:
    # Constructor (__init__) method jo object create hote hi call hota hai.
    # Yahan hum chai ka type (jaise 'Regular', 'Masala') initialize karte hain.
    def __init__(self, type_):
        self.type = type_

    # Chai prepare karne ka ek simple method
    def prepare(self):
        print(f"Preparing {self.type} chai....")

# MasalaChai class jo BaseChai se INHERIT karta hai (Inheritance).
# Iska matlab MasalaChai ke paas BaseChai ke saare methods (jaise prepare) automatically aa jayenge.
class MasalaChai(BaseChai):
    # Ye method sirf MasalaChai ke paas hai, BaseChai ke paas nahi.
    # Ye parent class ki functionality ko extend kar raha hai.
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")


# ChaiShop class jo ek shop ka representation hai.
# Yahan hum COMPOSITION ka use kar rahe hain - ek class (ChaiShop) ke andar dusre class (BaseChai/MasalaChai) ka object use karna.
class ChaiShop:
    # Class level attribute: Default chai class BaseChai set karte hain.
    chai_cls = BaseChai

    # Jab bhi ChaiShop ka object banega, ye constructor chalega.
    def __init__(self):
        # Yahan Composition ho raha hai: ChaiShop ke paas ek 'chai' object hai.
        # self.chai_cls("Regular") basically default case mein BaseChai("Regular") ko call kar raha hai.
        self.chai = self.chai_cls("Regular")

    # Chai serve karne ka method jo internal chai object ka prepare method call karta hai.
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

# FancyChaiShop class jo ChaiShop se inherit karta hai.
class FancyChaiShop(ChaiShop):
    # Yahan humne chai_cls attribute ko MasalaChai se override kar diya hai.
    # Ab jab FancyChaiShop ka object banega, toh parent constructor self.chai mein MasalaChai("Regular") banayega.
    chai_cls = MasalaChai


# ---------------- TESTING THE CODE ----------------

# Ek regular shop banate hain
shop = ChaiShop()
# Ek fancy shop banate hain
fancy = FancyChaiShop()

# Regular shop se chai serve karte hain (Ye BaseChai ka prepare call karega)
shop.serve()
# Fancy shop se chai serve karte hain (Ye MasalaChai ka prepare call karega)
fancy.serve()

# Fancy shop ki chai MasalaChai ka object hai, toh hum usme masale add kar sakte hain
# (Agar hum shop.chai.add_spices() karte toh error aata kyunki wo ek BaseChai object hai)
fancy.chai.add_spices()