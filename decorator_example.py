# A decorator is a function that adds behavior to another function without changing its code.

# Step 1: define a decorator
def my_decorator(func):
    def wrapper():
        print("Before the function runs...")
        func()  # call the original function
        print("After the function runs...")
    return wrapper

# Step 2: decorate a function
@my_decorator
def say_hello():
    print("Hello!")

# Step 3: call the decorated function
say_hello()