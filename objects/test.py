from DataBag import DataBag
from Employee import Employee
from Manager import Manager
from Executive import Executive


def test():
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    bag = DataBag()

    emp0 = Employee(0, "name", "dept", 100)
    print(emp0.toString())

    man0 = Manager(00, "name", "dept", 1000)
    print(man0.toString())

    exec0 = Executive(000, "name", "dept", 1000, 100)
    print(exec0.toString())

    print()
    print("add()")
    bag.add(emp0)
    bag.add(man0)
    bag.add(exec0)
    print(bag)

    print()
    print("remove()")
    bag.remove(emp0)
    print(bag)

    print()
    print("isEmpty()")
    print(bag.isEmpty())

    print()
    print("__len__")
    print(len(bag))

    print()
    print("__str__")
    print(bag)

    print()
    print("__iter__ and __eq__")
    for i in bag:
        if i == man0:
            print("__iter__ and __eq__ are working")

    print()
    print("__add__")
    bag2 = DataBag()
    bag2.add(emp0)
    bag3 = bag + bag2
    print(bag3)

    print()
    print("clear()")
    bag.clear()
    if bag.isEmpty():
        print("clear working")


test()
