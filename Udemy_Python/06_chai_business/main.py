# ek ye method h 
import recipes.flavors

print(recipes.flavors.ginger_chai())
print(recipes.flavors.elachai_chai())

# ek ye hai
from recipes import flavors

print(flavors.ginger_chai())
print(flavors.elachai_chai())

# or ek ye hai 
from recipes.flavors import elachai_chai, ginger_chai

print(ginger_chai())

