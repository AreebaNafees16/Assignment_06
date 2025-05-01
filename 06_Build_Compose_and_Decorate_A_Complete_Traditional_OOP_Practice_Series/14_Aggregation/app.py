class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Employee Name: {self.name}")


class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: storing reference to existing Employee

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()  # Accessing Employee's method


# Example usage
emp1 = Employee("Ayesha")             # Employee exists independently
dept1 = Department("HR", emp1)        # Aggregated into Department

dept1.show_details()
