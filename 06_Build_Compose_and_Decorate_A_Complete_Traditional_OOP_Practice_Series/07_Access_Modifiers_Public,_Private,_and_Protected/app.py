class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable (by convention)
        self.__ssn = ssn        # Private variable (name mangling)

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)


# Creating an object
emp = Employee("Ayesha", 50000, "123-45-6789")

# Accessing variables
print("Public - Name:", emp.name)            # ✅ Works
print("Protected - Salary:", emp._salary)    # ⚠️ Works, but not recommended (protected by convention)
# print("Private - SSN:", emp.__ssn)         # ❌ AttributeError: not directly accessible

# Accessing private variable using name mangling
print("Private - SSN (via name mangling):", emp._Employee__ssn)  # ✅ Works, but discouraged

# Showing all details via method
emp.show_details()
