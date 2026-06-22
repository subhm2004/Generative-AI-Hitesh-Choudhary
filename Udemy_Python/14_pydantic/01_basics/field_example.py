# ============================================================
# FILE: field_example.py
# TOPIC: Complex field types - List, Dict, Optional
# FOLDER: 14_pydantic/01_basics
# ============================================================
# List[str] = string ki list chahiye
# Dict[str, int] = string keys, integer values wala dictionary
# Optional[str] = string ya None - default None
# Pydantic nested structures (list, dict) bhi validate karta hai
# **cart_data = dictionary se Cart object banana
# ============================================================

from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]              # list of strings - ["Laptop", "Mouse"]
    quantities: Dict[str, int]     # dict - {"laptop": 1, "mouse": 2}

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None  # optional - default None


# Shopping cart ka data - list aur dict dono hain
cart_data = {
    "user_id": 123,
    "items": ["Laptop", "Mouse", "Keyboard"],
    "quantities": {"laptop": 1, "mouse": 2, "keyboard": 3}
}

# Dictionary se Cart object banao - Pydantic sab validate karega
cart = Cart(**cart_data)
