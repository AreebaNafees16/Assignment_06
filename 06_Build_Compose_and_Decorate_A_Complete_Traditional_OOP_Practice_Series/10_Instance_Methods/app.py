class Dog:
    def __init__(self, name, breed):
        self.name = name      # Instance variable
        self.breed = breed    # Instance variable

    def bark(self):           # Instance method
        print(f"{self.name} is barking! Woof woof!")


# Example usage
dog1 = Dog("Bruno", "Labrador")
dog1.bark()
