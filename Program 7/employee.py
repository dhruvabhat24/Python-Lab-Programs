class Employee:
    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
def update_salary_by_department(self, department, new_salary):
        self.slary = new_salary
e1= Employee("John", 101, "HR", 45000)
e2= Employee("Jane", 102, "Finance", 50000)
e3= Employee("Jack", 103, "HR", 55000)
employees = [e1, e2, e3]
for emp in employees:
    emp.update_salary_by_department("HR", 60000)
for emp in employees:
     print(emp.name, emp.employee_id, emp.department, emp.salary)