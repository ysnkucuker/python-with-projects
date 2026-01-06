from employee import Employee

class Manager(Employee):
    def __init__(self, name, salary, department, team_size):
        super().__init__(name, salary, department)
        self.team_size = team_size

    def raise_salary(self, amount):
        self.salary += amount

    def show_info(self):
        print(f"""
Manager Info
-------------------------
Name        : {self.name}
Salary      : {self.salary}
Department  : {self.department}
Team Size   : {self.team_size}
""")
