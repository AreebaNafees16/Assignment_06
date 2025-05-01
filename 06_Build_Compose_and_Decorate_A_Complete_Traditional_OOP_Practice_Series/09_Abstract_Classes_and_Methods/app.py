from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method

# Subclass implementing the abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Example usage
rect = Rectangle(10, 5)
print("Area of rectangle:", rect.area())
