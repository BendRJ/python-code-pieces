class User:
    # Class variable - shared across all instances
    role = "user"
    
    def __init__(self, name, custom_role=None):
        # Instance variables - unique to each instance
        self.name = name
        if custom_role:
            self.custom_role = custom_role
    
    # INSTANCE METHOD: Can access both instance state (self.name) and class state (self.__class__.role or User.role)
    def describe(self):
        role_to_use = getattr(self, 'custom_role', self.__class__.role)
        return f"{self.name} ({role_to_use})"
    
    # CLASS METHOD: Can access class state (cls.role) but NOT instance state
    # Receives the class (cls) as first parameter, not the instance
    @classmethod
    def get_role(cls):
        return cls.role
    
    @classmethod
    def change_default_role(cls, new_role):
        cls.role = new_role
    
    # STATIC METHOD: Cannot access class state or instance state
    # Just a regular function that belongs to the class namespace
    # Doesn't receive self or cls automatically
    @staticmethod
    def validate_name(name):
        return len(name) >= 3


print("=== Demonstrating Class Variable ===")
print(f"Class variable User.role: {User.role}")

print("\n=== Demonstrating Instance Method ===")
user1 = User("Alice")
print(f"Instance method (user1.describe()): {user1.describe()}")

print("\n=== Demonstrating Class Method ===")
print(f"Class method (User.get_role()): {User.get_role()}")
print(f"Class method can be called on instance too: {user1.get_role()}")

print("\n=== Demonstrating Static Method ===")
print(f"Static method (User.validate_name('Al')): {User.validate_name('Al')}")
print(f"Static method (User.validate_name('Alice')): {User.validate_name('Alice')}")
print(f"Static method can be called on instance too: {user1.validate_name('Bob')}")


print("\n=== Demonstrating Instance-Specific State ===")
user2 = User("Bob", custom_role="admin")
print(f"user1: {user1.describe()}")
print(f"user2: {user2.describe()}")

print("\n=== Demonstrating Class Method Modifying Class State ===")
print(f"Before: Default role is '{User.role}'")
User.change_default_role("member")
print(f"After: Default role is '{User.role}'")
user3 = User("Charlie")
print(f"New instance (user3): {user3.describe()}")
print(f"Existing instance (user1): {user1.describe()}")  # also affected by class variable change