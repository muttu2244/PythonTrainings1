#set is a collection of items not in any particular order
#The elements in the set cannot be duplicates.
#The elements in the set are immutable(cannot be modified) but the set as a whole is mutable.
#There is no index attached to any element in a python set. So they do not support any indexing or slicing operation.
#The sets in python are typically used for mathematical operations like union, intersection, difference and complement etc.

def createSet():
    Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    Months = {"Jan", "Feb", "Mar"}
    Dates = {21, 22, 17}
    print(Days)
    print(Months)
    print(Dates)

def accessValuesinSet():
    Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

    for d in Days:
        print(d)

def additemstoSet():
    Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])

    Days.add("Sun")
    print(Days)

def removeItemFromSet():
    Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

    Days.discard("Sun")
    print(Days)

def unionofSets():
    DaysA = set(["Mon", "Tue", "Wed"])
    DaysB = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
    AllDays = DaysA | DaysB
    print(AllDays)

def intersectionofSets():
    DaysA = set(["Mon", "Tue", "Wed"])
    DaysB = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
    AllDays = DaysA & DaysB
    print(AllDays)

#The difference operation on two sets produces a new set containing only the elements from the first set and none from the second set.
def diffOfSets():
    DaysA = set(["Mon", "Tue", "Wed"])
    DaysB = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
    AllDays = DaysA - DaysB
    print(AllDays)

if __name__ == '__main__':
    removeItemFromSet()