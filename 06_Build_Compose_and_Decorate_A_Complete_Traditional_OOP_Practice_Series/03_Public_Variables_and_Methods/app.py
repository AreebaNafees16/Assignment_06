class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):        # Public method
        print(f"The {self.brand} car has started.")


# Example usage
my_car = Car("Toyota")

# Accessing public variable
print("Car Brand:", my_car.brand)

# Calling public method
my_car.start()
