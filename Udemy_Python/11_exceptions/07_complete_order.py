# ============================================================
# FILE: 07_complete_order.py
# TOPIC: Complete example - custom + built-in exceptions, try/except/finally
# FOLDER: 11_exceptions
# ============================================================
# Custom InvalidChaiError + TypeError dono ek function mein
# except Exception = koi bhi error pakad lo (broad catch)
# finally = hamesha thank you message
# ============================================================

# Custom exception - chai menu mein nahi milne par
class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}  # available chai aur price
    try:
        # flavor menu mein nahi to custom error raise
        if flavor not in menu:
            raise InvalidChaiError("that chai is not available")
        # cups integer nahi to TypeError raise
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        # sab sahi to bill calculate karo
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")
    except Exception as e:
        # koi bhi error (InvalidChaiError, TypeError, etc.) - message print
        print("Error: ", e)
    finally:
        # success ya fail - ye hamesha chalega
        print("Thank you for visiting chaicode!")


# mint menu mein nahi - InvalidChaiError
bill("mint", 2)
# masala hai par cups string "three" - TypeError
bill("masala", "three")
# sab valid - bill print, phir finally
bill("ginger", 3)
