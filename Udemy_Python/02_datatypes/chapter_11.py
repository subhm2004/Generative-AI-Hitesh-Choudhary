import arrow
from collections import namedtuple

rome_time = arrow.utcnow().to("Europe/Rome")

print(f"Rome Brewing time: {rome_time}")

chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])

my_chai = chaiProfile(flavor="Ginger", aroma="Earthy")
print(f"Chai Profile -> Flavor: {my_chai.flavor}, Aroma: {my_chai.aroma}")