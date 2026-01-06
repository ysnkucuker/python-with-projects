class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def show_info(self):
        print(f"""
Employee Info
-------------------------
Name       : {self.name}
Salary     : {self.salary}
Department : {self.department}
""")

    def change_department(self, new_department):
        self.department = new_department
