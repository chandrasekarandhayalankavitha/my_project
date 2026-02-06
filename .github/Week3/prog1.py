
class Employee:
    def __init__(self, name):
        self.name = name

class AutomationSkills:
    def write_script(self):
        print("writing selenium scripts")

class AutomationTester(Employee, AutomationSkills):
    def execute_tests(self):
        print("Executing automated test cases")

tester = AutomationTester("John Doe")
tester.write_script()
tester.execute_tests()