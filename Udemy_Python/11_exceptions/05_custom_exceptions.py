# ============================================================
# FILE: 05_custom_exceptions.py
# TOPIC: raise se khud error throw karna (built-in exceptions)
# FOLDER: 11_exceptions
# ============================================================
# raise = program mein khud exception trigger karo
# ValueError = jab value galat ho (supported list mein nahi)
# Function validation ke baad raise kar sakta hai
# ============================================================

def brew_chai(flavor):
    # sirf ye teen flavors allowed hain
    if flavor not in ["masala", "ginger", "elaichai"]:
        # unsupported flavor par ValueError raise - program yahan rukega ya except pakdega
        raise ValueError("Unsupported chai flavor...")
    # valid flavor ho to chai banane ka message
    print(f"brewing {flavor} chai...")


# "mint" allowed list mein nahi - ValueError raise hoga, crash ya except
brew_chai("mint")
