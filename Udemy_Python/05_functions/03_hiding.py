# ============================================================
# FILE   : 03_hiding.py
# TOPIC  : Abstraction — andar ka kaam chhupana (hiding complexity)
# FOLDER : 05_functions
# ============================================================
# User ko andar ki details nahi dikhani — sirf ek simple function do.
# Jaise: register_user() call karo, baaki sab andar ho jayega.

# Step 1: User se input lena
def get_input():
    print("Getting user input")

# Step 2: Input sahi hai ya nahi check karna
def validate_input():
    print("Validating the user info")

# Step 3: Database mein save karna
def save_to_db():
    print("saving to database")

# Ye function sab steps ko ANDAR chhupa leta hai
# Bahar wala sirf register_user() call karega — baaki details nahi jaanni padengi
def register_user():
    get_input()          # pehle input lo
    validate_input()     # phir validate karo
    save_to_db()         # phir database mein save karo
    print("User registration complete")  # sab khatam — success message


# Ek line mein poora registration process — complexity hidden hai!
register_user()
