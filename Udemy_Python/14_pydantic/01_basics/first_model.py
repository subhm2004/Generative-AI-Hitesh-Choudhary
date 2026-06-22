# ============================================================
# FILE: first_model.py
# TOPIC: Pydantic BaseModel - pehla data validation model
# FOLDER: 14_pydantic/01_basics
# ============================================================
# Pydantic = data validation library - type checking + auto conversion
# BaseModel = sab models ka parent class - isse inherit karo
# Type hints (id: int) define karte hain - Pydantic validate karta hai
# Galat type aaye to automatically convert try karta hai (jaise '101a' -> error)
# **input_data = dictionary ko keyword arguments mein convert karta hai
# ============================================================

from pydantic import BaseModel  # BaseModel = Pydantic ka core class

# User model - teen fields with type hints
class User(BaseModel):
    id: int          # integer hona chahiye
    name: str        # string hona chahiye
    is_active: bool  # True/False hona chahiye

# Dictionary se data - id galat type hai ('101a' string hai, int nahi)
input_data = {'id': '101a', 'name': "Chaicode", 'is_active': True}

# **input_data = dict ko unpack karke User(id='101a', name=..., is_active=...) banata hai
# Pydantic validation chalega - '101a' int mein convert nahi ho sakta = ERROR!
user = User(**input_data)
print(user)
