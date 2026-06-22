# ============================================================
# FILE: product_model.py
# TOPIC: Pydantic default values + validation errors
# FOLDER: 14_pydantic/01_basics
# ============================================================
# Default value = field(= True) - agar value na do to ye use hogi
# Required fields = bina default ke - dena ZAROORI hai
# Pydantic ValidationError deta hai agar required field missing ho
# product_three mein id aur price missing hain - error aayega!
# ============================================================

from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True  # default value - agar na do to True hoga


# Sab fields diye - perfectly valid
product_one = Product(id=1, name="Laptop", price=999.99, in_stock=True)

# in_stock nahi diya - default True use hoga
product_two = Product(id=2, name="Mouse", price=24.33)

# id aur price MISSING hain - Pydantic ValidationError throw karega!
product_three = Product(name="keyboard")
