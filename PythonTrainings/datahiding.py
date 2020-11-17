class fruit:
    __uname = "abc@xyz.com"     #data hiding by putting "_ _ (double underscore)"
    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity
        print("Object Created")

    def details(self):
        print("I am {}".format(self.fruitname))

    def __del__(self):
        print("Object Destroyed")

f = fruit("mango",5)
#print (f.__uname )# uname cannot be accessed directly from the fruit object (f)....
print(f._fruit__uname)  #  we have to use (_CLASSNAME__VARIABLENAME)


