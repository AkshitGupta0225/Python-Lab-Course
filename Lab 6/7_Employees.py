class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self._name = name
        self.__salary = salary

    def display_employee(self):
        print(f"ID: {self.emp_id}, Name: {self._name}, Salary: {self.__salary}")

    def _update_name(self, new_name):
        self._name = new_name

    def __update_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary

    def update_salary(self, new_salary):
        self.__update_salary(new_salary)


class Manager(Employee):
    def promote_employee(self):
        print(f"Promoting: {self._name}")


emp = Manager(101, "Akshit Gupta", 50000)
emp.display_employee()
emp._update_name("Divit Gupta")
emp.update_salary(60000)
emp.display_employee()
emp.promote_employee()
