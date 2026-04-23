class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai)) # class hai lekin internally ye ek object hai 

ginger_tea = Chai() # onject of chai class

print(type(ginger_tea))

print(type(ginger_tea) is Chai) # kya ye object h chai class ka ? true or false ? in this case its true

print(type(ginger_tea) is ChaiTime) # false