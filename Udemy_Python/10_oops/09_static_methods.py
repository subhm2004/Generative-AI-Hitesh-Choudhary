# ============================================================
# FILE: 09_static_methods.py
# TOPIC: @staticmethod - bina self/cls ke utility methods
# FOLDER: 10_oops
# ============================================================
# STATIC METHOD = class ke saath juda function jo na self leta hai na cls
# Instance banane ki zaroorat nahi - class se directly call karo
# Utility/helper functions ke liye useful jo object state par depend nahi karte
# ============================================================

class ChaiUtils:
    # @staticmethod decorator - ye method class ka hai par instance se bind nahi
    @staticmethod
    def clean_ingredients(text):
        # text ko comma se split karke har item ki spaces hata do
        return [item.strip() for item in text.split(",")]
    

# Raw string jisme ingredients comma se separated hain, extra spaces ke saath
raw = " water , milk , ginger , honey "

# Class se directly call - object banane ki zaroorat nahi (staticmethod)
cleaned = ChaiUtils.clean_ingredients(raw)  # static method call
print(cleaned)  # ['water', 'milk', 'ginger', 'honey'] - saaf list
