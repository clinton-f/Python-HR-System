from objects.Employee import Employee


class Executive(Employee):

    def __init__(self, empID, name, dept, salary, bonus):
        super().__init__(empID, name, dept, salary)
        self.bonus = bonus

    def getMeasure(self):
        return self.salary + self.bonus

    def getType(self):
        return "Executive"

    def toString(self):
        return "Executive [ID: " + str(self.id) + ", Name: " + self.name + ", Dept: " + self.dept + ", Salary: " + str(self.salary) + ", Bonus: " + str(self.bonus) + "]"
