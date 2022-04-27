from objects.DataBag import DataBag
from objects.Employee import Employee
from objects.Manager import Manager
from objects.Executive import Executive

def loadData():

    bag = DataBag()

    for i in range(50):
        bag.add(Employee(i, "name" + str(i), "CSC", 500 + i * 5))

    for i in range(15):
        bag.add(Manager(i + 50, "name" + str(i + 50), "CSC", 750 + i * 5))

    for i in range(15):
        bag.add(Executive(i + 65, "name" + str(i + 65), "CSC", 825 + i * 5, 100 + i * 10))

    return bag