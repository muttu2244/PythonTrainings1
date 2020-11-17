#singleton class is a class which can have only one instance at any given point of time
#even if there are 2 objects, both are pointing to the same Object memory location(so they both are one)

class MySingleton(object):
    _instance = None                #Class variable
    def __init__(self):
        if not self._instance:      #if the instance is not created already by some object
            self._instance = super(MySingleton,self).__init__()         #then the self constructor is called and the new instance is created
            self.y = 10                                                     # and y gets assigned as 10
        return (self._instance)     #else if the instance is already created by some Objects (Ex: x = MySingleton() ) , then it just returns the x instance


x = MySingleton()
print(x.y)
x.y = 20
z = MySingleton()
print(z.y)      #------ This should have been 20, but it will be 10, as in the constructor, since the instance is already created (x) , it does not create
                #the instance once again, when z= MySingleton() object is created.. Therefore the self.y =10 will not get assigned.. therefore z.y remains as 20