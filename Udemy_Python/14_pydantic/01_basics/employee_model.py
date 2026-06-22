# ============================================================
# FILE: employee_model.py
# TOPIC: Pydantic Field() - constraints, Optional, regex
# FOLDER: 14_pydantic/01_basics
# ============================================================
# Field() = field par extra rules lagao (min_length, max_length, ge, le)
# ... = required field (Ellipsis) - dena ZAROORI hai
# Optional[str] = ya to string ya None - default 'General' diya hai
# ge = greater than or equal, le = less than or equal
# regex = pattern match karna (email, phone format)
# ============================================================

from typing import Optional  # Optional = value ya None ho sakti hai
from pydantic import BaseModel, Field  # Field = extra validation rules
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,  # required - dena zaroori hai
        min_length=3,   # kam se kam 3 characters
        max_length=50,  # zyada se zyada 50 characters
        description="Employee Name",  # documentation ke liye
        examples="Hitesh Choudhary"   # example value
    )
    department: Optional[str] = 'General'  # optional - default 'General'
    salary: float = Field(
        ...,
        ge=10000  # salary kam se kam 10000 honi chahiye
    )


class User(BaseModel):
    email: str = Field(...,regex=r'')  # regex pattern - email format check
    phone: str = Field(..., regex=r'')  # phone number format check
    age: int = Field(
        ...,
        ge=0,    # age 0 se kam nahi
        le=150,  # age 150 se zyada nahi
        description="Age in years",
    )
    discount: float = Field(
        ...,
        ge=0,   # 0% se kam discount nahi
        le=100, # 100% se zyada discount nahi
        description="Discount percentage"
    )
