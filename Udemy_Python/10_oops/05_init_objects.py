class ChaiOrder:
    
    # constructor method, it is called when we create an instance of the class
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
order = ChaiOrder("Masala", 200)
print(order.summary())

print("\nCreating another order:")
order_two = ChaiOrder("Ginger", 220)
print(order_two.summary())