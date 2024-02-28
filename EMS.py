
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
	def __init__(self, dept_name, emp_list: list):
		self.dept_name = dept_name
		self.employees = []

	def add_employee(self, emp_id, title, department):
		self.employee_details.append(
			)
		{
			"emp_id": emp_id,
			"title": title,
			"department": department
		}


	def rm_employee(self, emp_id):
		pass

	def list_employees(self):
		pass






emp1 = Employee("Aman Sharma", 1, "Software Engineer", "Engineering")
emp2 = Employee("Akash Sharma", 2, "Data Scientist", "Analytics")
Employee.show_emp_details(emp2)

# eng_dept = Department("Engineering")
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