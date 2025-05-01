class Student:
    def __init__(self, name, marks):
        self.name = name        # Initialize name using self
        self.marks = marks      # Initialize marks using self

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


# Example usage
student1 = Student("Ayesha", 92)
student1.display()
