class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks  # Protected member

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:  # Validation
            self._marks = new_marks
        else:
            print("Marks must be between 0 and 100.")

    def display_info(self):
        print(f"Name: {self.name}, Marks: {self._marks}")
class DerivedStudent(Student):
    def access_protected_marks(self):
        print(f"Accessing protected marks of {self.name}: {self._marks}")
student = DerivedStudent("Akshit", 85)
student.display_info()
student.update_marks(92)
student.display_info()
student.access_protected_marks()
