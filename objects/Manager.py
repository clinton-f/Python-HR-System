from objects.Employee import Employee


class Manager(Employee):

    def __init__(self, empID, name, dept, salary):
        Employee.__init__(self, empID, name, dept, salary)

    def getType(self):
        return "Manager"

    def toString(self):
        return "Manager [ID: " + str(self.id) + ", Name: " + self.name + ", Dept: " + self.dept + ", Salary: " + str(self.salary) + "]"
