# ============================================================
# FILE: advance_nested_model.py
# TOPIC: Advanced nesting - Optional, Union, deep nesting
# FOLDER: 14_pydantic/01_basics
# ============================================================
# Optional[Address] = Address object YA None - dono valid
# Union[A, B] = ya to A type ya B type - multiple types allow
# List[Union[Text, Image]] = list mein text YA image sections ho sakte hain
# Deep nesting = Country -> State -> City -> Address -> Organization
# Default empty list: branches: List[Address]=[]
# ============================================================

from pydantic import BaseModel
from typing import Optional, List, Union


class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address] = None  # address optional hai - None bhi chalega

class Employee(BaseModel):
    name: str
    company: Optional[Company] = None  # company bhi optional


# Union example - article mein text YA image sections ho sakte hain
class TextConent(BaseModel):
    type: str = "text"  # default type
    content: str

class ImageContent(BaseModel):
    type: str = "Image"
    url: str
    alt_text: str

class Article(BaseModel):
    title: str
    # List mein ya to Text ya Image - Union se multiple types
    sections: List[Union[TextConent, ImageContent]]


# Deep nesting example - 4 levels deep!
class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country  # State ke andar Country

class City(BaseModel):
    name: str
    state: State  # City ke andar State (jo Country contain karta hai)

class Address(BaseModel):
    street: str
    city: City  # Address ke andar City (poora chain!)
    postal_code: str

class Organization(BaseModel):
    name: str
    head_quarter: Address  # headquarters = deeply nested Address
    branches: List[Address]=[]  # branches list - default empty list
