class Employee:

    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department

    def calculate_emp_salary(self, worked_hours):
        overtime_amount = 0
        if worked_hours > 50:
            overtime = worked_hours -50
            overtime_amount = (overtime * (self.salary / 50))

        return self.salary + overtime_amount

    def emp_assign_department(self,new_department):
        self.department = new_department

    def print_employee_details(self):

        for attr,value in self.__dict__.items():
            print(f'{attr} -> {value}')



employee1= Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2= Employee("JONES", "E7499", 45000, "RESEARCH")
employee3= Employee("MARTIN", "E7900", 50000, "SALES")
employee4= Employee("SMITH", "E7698", 55000, "OPERATIONS")

print("Employee's data:")
employee1.print_employee_details()
employee1.emp_assign_department("CEO")
print("Employee's data:")
employee1.print_employee_details()
print("Employee's salary: ",employee1.calculate_emp_salary(70))
