# ============================================================
# FILE: nested_model.py
# TOPIC: Nested Pydantic models - model ke andar model
# FOLDER: 14_pydantic/01_basics
# ============================================================
# Nested Model = ek model ke andar doosra model as field
# User.address = Address type ka object hona chahiye
# Dictionary se bhi bana sakte ho - Pydantic automatically nested dict parse karega
# **user_data = nested dictionary ko User object mein convert karta hai
# ============================================================

from typing import List, Optional
from pydantic import BaseModel


# Address model - street, city, postal_code
class Address(BaseModel):
    street: str
    city: str
    postal_code: str

# User model - address field Address TYPE ka hai (nested!)
class User(BaseModel):
    id: int
    name: str
    address: Address  # Address object chahiye - sirf string nahi!


# Pehle Address object banao
address = Address(
    street="123 something",
    city="Jaipur",
    postal_code="100001"
)

# Phir User object mein Address pass karo
user = User(
    id=1,
    name="Hitesh",
    address=address,
)


# Dictionary se bhi bana sakte ho - nested dict automatically parse hoga!
user_data = {
    "id": 1,
    "name": "Hitesh",
    "address": {  # nested dictionary - Pydantic Address model banayega
        "street": "321 something",
        "city": "Paris",
        "postal_code": "20002"
    }
}

user = User(**user_data)  # dict se User object - address auto-parse
print(user)
