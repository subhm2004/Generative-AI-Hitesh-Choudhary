# ============================================================
# FILE: field_validation.py
# TOPIC: field_validator + model_validator - custom validation
# FOLDER: 14_pydantic/01_basics
# ============================================================
# @field_validator = EK field par custom rule lagao
# @model_validator = POORE model par rule - multiple fields compare karo
# mode='after' = sab fields set hone ke BAAD validation chale
# ValueError raise karo agar validation fail ho
# Use case: password match, username length, date range check
# ============================================================

from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    username: str

    # @field_validator = username field par custom check
    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v  # validated value return karo
    

class SignupData(BaseModel):
    password: str
    confirm_password: str

    # @model_validator = POORE model par check - do fields compare karo
    @model_validator(mode='after')
    def password_match(cls, values):
        # values.password aur values.confirm_password compare karo
        if values.password != values.confirm_password:
            raise ValueError("Password do not match")
        return values  # poora model return karo
