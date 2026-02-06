
class Person:
    def __init__(self,name):
        self.name = name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

class Manager(Employee):
    def __init__(self, name, employee_id,team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

    def show_details(self):
        print(f"Name: {self.name}, Employee ID: {self.employee_id}, Team Size: {self.team_size}")
    
manager = Manager("Alice", "E123", 10)
manager.show_details()
