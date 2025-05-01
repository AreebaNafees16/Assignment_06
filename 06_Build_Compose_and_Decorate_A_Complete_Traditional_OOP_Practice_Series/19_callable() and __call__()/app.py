class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


# Create an instance
m = Multiplier(3)

# Test with callable()
print("Is m callable?", callable(m))  # ✅ Should return True

# Call the object like a function
result = m(10)  # Equivalent to m.__call__(10)
print("Result of m(10):", result)
