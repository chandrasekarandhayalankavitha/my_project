
class User:
    users = []  # Maintains user list

    def __init__(self, username):
        self.username = username
        self.blocked = False
        User.users.append(self)

    def login(self):
        if self.blocked:
            print(f"{self.username} is blocked and cannot log in.")
        else:
            print(f"{self.username} logged in.")


class Student(User):
    def __init__(self, username):
        super().__init__(username)
        self.enrolled_courses = []

    def login(self):
        print(f"Student {self.username} logged in.")

    def enroll_course(self, course_name, instructor):
        self.enrolled_courses.append(course_name)
        instructor.add_student(course_name, self.username)
        print(f"{self.username} enrolled in {course_name}")

    def pay_fee(self, amount):
        print(f"{self.username} paid fee: {amount}")


class Instructor(User):
    def __init__(self, username):
        super().__init__(username)
        self.courses = {}  # course_name -> list of students

    def login(self):
        print(f"Instructor {self.username} logged in.")

    def create_course(self, course_name):
        self.courses[course_name] = []
        print(f"{self.username} created course: {course_name}")

    def add_student(self, course_name, student_name):
        if course_name in self.courses:
            self.courses[course_name].append(student_name)

    def show_enrollments(self):
        print(f"Enrollments for instructor {self.username}:")
        for course, students in self.courses.items():
            print(f"{course}: {students}")


class Admin(User):
    def login(self):
        print(f"Admin {self.username} logged in.")

    def block_user(self, user):
        user.blocked = True
        print(f"{user.username} has been blocked.")

    def generate_report(self):
        print("User Report:")
        for user in User.users:
            status = "Blocked" if user.blocked else "Active"
            print(f"{user.username} - {status}")


# ---------------- MAIN ----------------

if __name__ == "__main__":
    instructor = Instructor("Alice")
    student1 = Student("Bob")
    student2 = Student("Charlie")
    student3 = Student("David")
    admin = Admin("Root")

    instructor.create_course("Python")

    student1.enroll_course("Python", instructor)
    student2.enroll_course("Python", instructor)
    student3.enroll_course("Python", instructor)

    instructor.show_enrollments()

    admin.block_user(student2)
    admin.generate_report()
