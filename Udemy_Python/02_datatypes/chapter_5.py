import sys
from fractions import Fraction
from decimal import Decimal as deci

ideal_temp = 95.5
current_temp = 95.49999999999999
print("\n")

print(f"Ideal temp { ideal_temp }")
print("\n")

print(f"Current temp { current_temp }")
print("\n")

print(f"Difference temp { ideal_temp - current_temp }")
print("\n")
print(sys.float_info) # package h ye ek 
print("\n")

print(deci(175)/deci(18))
