# ============================================================
# FILE: advance_validators.py
# TOPIC: Advanced validators - before mode, normalize, date range
# FOLDER: 14_pydantic/01_basics
# ============================================================
# mode='before' = type conversion se PEHLE validator chale
# Multiple fields ek validator mein: @field_validator('first_name', 'last_name')
# Normalize = data clean karo (email lowercase, strip spaces)
# model_validator mode='after' = do dates compare karo
# istitle() = pehla letter capital hona chahiye
# ============================================================

from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    first_name: str
    last_name : str

    # Dono fields par same validator - capitalize check
    @field_validator('first_name', 'last_name')
    def names_must_be_capitalize(cls, v):
        if not v.istitle():  # istitle() = "Hitesh" OK, "hitesh" NOT OK
            raise ValueError('Names must be capitilized')
        return v
    


class User(BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls, v):
        # Email clean karo - lowercase + spaces hatao
        return v.lower().strip()
    


class Product(BaseModel):
    price: str # type hint str hai lekin validator float mein convert karega

    # mode='before' = Pydantic type check se PEHLE ye chalega
    @field_validator('price', mode='before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', ''))  # "$4.44" -> 4.44
        return v
    
class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime


    # Poora model banne ke baad dates compare karo
    @model_validator(mode="after")
    def validate_date_range(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError('end_date must be after start_date')
        return values
