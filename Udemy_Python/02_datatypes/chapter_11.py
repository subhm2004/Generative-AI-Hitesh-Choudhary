# ============================================================
# FILE: chapter_11.py
# TOPIC: Advanced types - arrow (datetime) + namedtuple
# FOLDER: 02_datatypes
# ============================================================
# arrow = datetime library (time zones ke saath easy)
# namedtuple = tuple jisme fields ke NAAM hote hain (dot se access)
# Ye optional/advanced topics hain - baad mein aur seekhoge
# ============================================================

import arrow  # pip install arrow - time/date ke liye popular library
from collections import namedtuple  # Python ki built-in module

# UTC time leke Rome timezone mein convert karo
rome_time = arrow.utcnow().to("Europe/Rome")
print(f"Rome Brewing time: {rome_time}")

# namedtuple = lightweight class jaisa, immutable
# "chaiProfile" = type ka naam, ["flavor", "aroma"] = field names
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])

# Object banao - positional ya keyword arguments se
my_chai = chaiProfile(flavor="Ginger", aroma="Earthy")

# Dot notation se access - tuple se zyada readable!
print(f"Chai Profile -> Flavor: {my_chai.flavor}, Aroma: {my_chai.aroma}")
