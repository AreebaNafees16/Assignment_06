class A:
    def show(self):
        print("A's show() method")

class B(A):
    def show(self):
        print("B's show() method")

class C(A):
    def show(self):
        print("C's show() method")

class D(B, C):  # Inherits from both B and C
    pass


# Example usage
obj = D()
obj.show()  # Observe which show() is called

# Display MRO
print("Method Resolution Order:", [cls.__name__ for cls in D.__mro__])
