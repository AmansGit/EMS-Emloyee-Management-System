
class Employee:
	def __init__(self, name, emp_id, title, department):
		self.name = name
		self.emp_id = emp_id
		self.title = title
		self.department = department
		self.emp_detail = {
			"name": self.name,
			"emp_id": self.emp_id,
			"title": self.title,
			"department": self.department
		}

	def show_emp_details(self):
		print(f"Employee details:")
		print(f"{self.emp_detail}")

	def __str__(self):
		return f"{self.name} - ID: {self.emp_id}"


class Department:
	def __init__(self, dept_name):
		self.dept_name = dept_name
		self.employees = {}

	def add_employee(self, emp_name, emp_id, title, department):
		self.employees[emp_id] = {
			"name": emp_name,
			"emp_id": emp_id,
			"title": title,
			"department": department
			}
		print(f"Inside Add employee: {self.employees}")
# {
# 	1: {"emp_id": 1, "name": "Aman", "Dept": "engg"},
# 	2: {"emp_id": 2, "name": "Akash", "Dept": "Analytics"}
# }

	def rm_employee(self, emp_id):
		if emp_id in employees:
			del employees[emp_id]

		# If we initialize employee as dict and inserting data in List then:
		for employee in self.employees:
			if employee.emp_id == emp_id:
				self.employees.remove(employee)
				print(f"Employee with ID {employee_id} removed from {self.name}")
				return
		print(f"Employee with emp-id: {emp_id} not available")


	def list_employees(self):
		if not self.employees:
			print("No employees in this department.")
		else:
			print(f"Employees in {self.dept_name}")
			for employee in employees:
				print(employee)

class Company:
	def __init__(self):
		self.departments = {}

	def add_department(self, department):
		""" To add new department
		"""
		self.departments[department.dept_name] = department

	def rm_department(self, department_name):
		""" To remove any department based on name
		"""
		if department_name in self.departments:
			del self.departments[department_name]
			print(f"Department {department_name} successfully removed")

		else:
			print(f"Department {self.department_name} is not available")

	def show_departments(self):
		if not self.departments:
			print("No departments to show now")

		else:
			print("Departments: ")
			for depts in self.departments:
				print(f"- {depts}")



# Working with company directory
company = Company()

ece_dept = Department("ECE")
cse_dept = Department("CSE")

company.add_department(ece_dept)
company.add_department(cse_dept)


company.show_departments()

company.rm_department("ECE")

# Displaying departments after removal
company.show_departments()



emp1 = Employee("Aman Sharma", 1, "SDE", "ECE")
emp2 = Employee("Akash Sharma", 2, "Sr SDE", "CSE")
Employee.show_emp_details(emp2)


# print("OBJECT:: ", emp1)
# eng_dept = Department("Engineering")
ece_dept.add_employee(emp1)
print("AFTER ECE_DEPT")
# analytic_dept = Department("Analytics")


"""
Company directory:
===================
{
	"department_1": [
		"emp_1": {
			"emp_id": 1,
			"title": "ABCD",
		},
		"emp_2": {
			"emp_id": 2,
			"title": "ABCDE",
		}
	],

	"department_2": [
		"emp_3": {
			"emp_id": 3,
			"title": "ABCD",
		},
		"emp_4": {
			"emp_id": 4,
			"title": "ABCDE",
		}
	],

}

"""