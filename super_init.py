class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal.__init__ called on {id(self)}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # calls Animal.__init__ on THIS object
        # runs the parent's initialization code on the already-existing self
        self.breed = breed
        print(f"Dog.__init__ called on {id(self)}")

rex = Dog("Rex", "Labrador")
# Output:
# Animal.__init__ called on 140234567890  ← same id!
# Dog.__init__ called on 140234567890     ← same id!

print(rex.name)   # "Rex"   ← set by Animal.__init__
print(rex.breed)  # "Labrador" ← set by Dog.__init__
# meaning one object gets set up by multiple __init__ methods in the inheritance chain

