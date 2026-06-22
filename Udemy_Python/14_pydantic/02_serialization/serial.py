# ============================================================
# FILE: serial.py
# TOPIC: Serialization - model_dump() and model_dump_json()
# FOLDER: 14_pydantic/02_serialization
# ============================================================
# Serialization = Pydantic model ko dict ya JSON mein convert karna
# model_dump() = Python dictionary return karta hai
# model_dump_json() = JSON string return karta hai
# ConfigDict json_encoders = custom format (jaise datetime ko string)
# API responses, database storage ke liye bahut useful
# ============================================================

from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime  # datetime object
    address: Address     # nested model
    tags: List[str] = []

    # ConfigDict = model ki settings
    model_config = ConfigDict(
        # datetime ko custom format mein convert karo JSON mein
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )


user = User(
    id=1,
    name="Hitesh",
    email="h@hitesh.ai",
    createdAt=datetime(2024, 3, 15, 14, 30,),
    address=Address(
        street="Something",
        city="Jaipur",
        zip_code="009988"
    ),
    is_active=False,
    tags=["premium", "subscriber"]
)

# model_dump() = Pydantic model ko Python dict mein convert karo
python_dict = user.model_dump()
print(user)
print("="*30)
print(python_dict)

# model_dump_json() = Pydantic model ko JSON string mein convert karo
json_str = user.model_dump_json()
print("="*30)
print(json_str)
