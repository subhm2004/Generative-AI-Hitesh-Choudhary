# Ye function chai ka flavor return karta hai, default "masala" hai
def chai_flavor(flavor="masala"):
    """Return the flavor of chai."""
    chai = "ginger"  # ye variable use nahi hua, bas pada hai yahan
    return flavor  # jo flavor diya usi ko wapas bhej do


# Function ka docstring print karo (triple quotes wala description)
print(chai_flavor.__doc__)

# Function ka naam print karo
print(chai_flavor.__name__)

# Built-in len() function ki puri help/documentation dikhao
help(len)


# Ye function chai aur samosa ka total bill calculate karta hai
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