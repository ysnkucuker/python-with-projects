class Developer:
    def __init__(self, first_name, last_name, employee_id, salary, languages):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.languages = languages

    def show_info(self):
        print(f"""
Developer Info
-------------------------
Name       : {self.first_name}
Surname    : {self.last_name}
ID         : {self.employee_id}
Salary     : {self.salary}
Languages  : {self.languages}
""")

    def raise_salary(self, amount):
        self.salary += amount

    def add_language(self, language):
        self.languages.append(language)
