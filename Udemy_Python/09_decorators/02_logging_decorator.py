# ============================================================
# FILE: 02_logging_decorator.py
# TOPIC: LOGGING DECORATOR - function calls track karna
# FOLDER: 09_decorators
# ============================================================
# *args = koi bhi POSITIONAL arguments (tuple ki tarah)
# **kwargs = koi bhi KEYWORD arguments (dict ki tarah)
# func.__name__ = function ka naam string mein
# return result = decorator original function ka return value wapas bhej sakta hai
# Real projects mein logging decorators bahut common hain (debugging ke liye)
# ============================================================

# Built a logger with decorator
from functools import wraps

# log_activity = decorator jo har function call log karta hai
def log_activity(func):
    @wraps(func)
    # *args, **kwargs = wrapper KISI bhi arguments wale function ko handle kar sakta hai
    def wrapper(*args, **kwargs):
        # func.__name__ = jis function ko wrap kiya uska naam (e.g. "brew_chai")
        print(f"🚀 Calling: {func.__name__}")
        result = func(*args, **kwargs)  # asli function chalao, result save karo
        print(f"✅ Finished: {func.__name__}")
        return result  # original function ka return value wapas do
    return wrapper

# @log_activity = brew_chai ko logging wrapper se wrap karo
@log_activity
# brew_chai = 2 arguments leta hai: type (required), milk (optional, default "no")
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai and milk status {milk}")

# brew_chai("Masala") call hoga to:
# 1. "🚀 Calling: brew_chai" print
# 2. brew_chai asli code chalega
# 3. "✅ Finished: brew_chai" print
brew_chai("Masala")
