class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

#  In the above implementation, we have a base class `Chai` with an `__init__` method that initializes the `type` and `strength` attributes.

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level
        
# In the above implementation, we are not calling the base class constructor, which means that if there is any initialization logic in the base class, it will not be executed. This can lead to issues if the base class has important setup code.

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level

# Using super() is the recommended way to call the base class constructor, as it is more maintainable and works well with multiple inheritance.
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level