
class Employee:

    def __init__(self, empID, name, dept, salary):
        self.id = empID
        self.name = name
        self.dept = dept
        self.salary = salary

    def getID(self):
        return self.id

    def setID(self, inID):
        self.id = inID

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getDept(self):
        return self.dept

    def setDept(self, dept):
        self.dept = dept

    def getSalary(self):
        return self.salary

    def setSalary(self, salary):
        self.salary = salary

    def getMeasure(self):
        return self.salary

    def getType(self):
        return "Employee"

    def toString(self):
        return "Employee [ID: " + str(self.id) + ", Name: " + self.name + ", Dept: " + self.dept + ", Salary: " + str(self.salary) + "]"
