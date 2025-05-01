# Class decorator definition
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Add greet method to the class
    return cls

# Applying the class decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
p = Person("Ayesha")
print(p.greet())  # Calling the dynamically added method
