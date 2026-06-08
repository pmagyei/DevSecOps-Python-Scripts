class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.fn = first_name
        self.ln = last_name
        self.an = annual_salary

    def employee_raise(self, raise_salary=5000):
        self.an += raise_salary
        return f"{self.fn} {self.ln} has a salary of {self.an}"