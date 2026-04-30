class Chaicup:
    size = 150 #ml

    # self is a reference to the current instance of the class (method hai ye)
    def describe(self):
        return f"A {self.size}ml chai cup"
    

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))