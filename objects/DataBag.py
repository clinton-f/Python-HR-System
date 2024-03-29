
class DataBag(object):
    """A list-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = list()
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = DataBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other:
            return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True

    # Mutator methods
    def sortByName(self):
        return sorted(self.items, key=lambda x: x.getName(), reverse=False)

    def sortBySalary(self):
        return sorted(self.items, key=lambda x: x.getSalary(), reverse=False)

    def clear(self):
        """Makes self become empty."""
        self.items = list()

    def add(self, item):
        """Adds item to self."""
        self.items.append(item)

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""

        # Check precondition and raise KeyError if necessary
        if item not in self.items:
            raise KeyError("Item not in bag")
        else:
            self.items.remove(item)

    def deleteById(self, index):
        """Deletes item in DataBag based on position"""

        count = 0
        for i in self.items:
            if count == index:
                self.items.remove(i)
            count += 1
