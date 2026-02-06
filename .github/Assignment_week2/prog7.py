
class student:
    def __init__(self, name, grade, department):
        self.name = name
        self.grade = grade
        self.department = department

    def print_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}, Department: {self.department}")

    def update_grade(self, new_grade):
        self.grade = new_grade

student1 = student("Alice", "A", "Computer Science")
student2 = student("Bob", "B", "Mathematics")
student3 = student("Charlie", "C", "Physics")
students = [student1, student2, student3]
student1.print_info()
student2.print_info()
student3.print_info()
student1.update_grade("A+")
student1.print_info()
