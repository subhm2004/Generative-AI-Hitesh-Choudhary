# ============================================================
# FILE   : 12_built_in.py
# TOPIC  : Function attributes, docstrings, default parameters, help()
# FOLDER : 05_functions
# ============================================================
# Functions ke special attributes hote hain (__doc__, __name__).
# Default parameters, docstrings, aur built-in help() bhi seekhenge.

# Ye function chai ka flavor return karta hai, default "masala" hai
# Default parameter: agar flavor na do toh "masala" use hoga automatically
def chai_flavor(flavor="masala"):
    """Return the flavor of chai."""
    # Upar wala triple-quote string = DOCSTRING — function ki description
    chai = "ginger"  # ye variable use nahi hua, bas pada hai yahan
    return flavor  # jo flavor diya usi ko wapas bhej do


# __doc__ = function ki docstring (description) access karo
print(chai_flavor.__doc__)  # "Return the flavor of chai."

# __name__ = function ka naam string mein
print(chai_flavor.__name__)  # "chai_flavor"

# help() = built-in function ki poori documentation terminal mein dikhao
help(len)  # len() function ka help page — kaise use karna hai sab likha hai


# Ye function chai aur samosa ka total bill calculate karta hai
# Dono parameters ke DEFAULT values 0 hain — agar na do toh 0 maan lega
def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa

    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    :return: (total amount, thank you message as string)
    """
    # Ek chai = 10 rupaye, ek samosa = 15 rupaye — dono multiply karke jodo
    total = chai * 10 + samosa * 15

    # Total aur ek thank you message dono ek saath return karo (tuple)
    return total, "Thank you for visiting chaicode.com"
