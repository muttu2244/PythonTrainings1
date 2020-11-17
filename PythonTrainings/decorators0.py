#changing the way the function behaves without even touching the source code is decorator
#it decorates the untoucable (supposing we do not have the access to the source code) function
#Dynamically Alter The Functionality Of Your Functions

#Decorators are almost similar to Closures in python
#Decorators are kind of Wrappers
#
"""
def div(a,b):
    print(a/b)


def smartFunc(func):            #here the func = div(2,4)
    def inner_function(a,b):    #a becomes 2 and b becomes 4
        if (a < b):
            a,b=b,a             #a=4, b=2
        return(func(a,b))       # here the actual div function above is being called with swapped a and b values
    return(inner_function)

div = smartFunc(div)

div(2,4)        #This is equal to "smartFunc(div(2,4))"
"""
#---------------------------------------------------------------------------------------------------------------------------
#The above code is similar to below code


def smartFunc(func):            #here the func = div(2,4)
    def inner_function(a,b):    #a becomes 2 and b becomes 4
        if (a < b):
            a,b=b,a             #a=4, b=2
        return(func(a,b))       # here the actual div function above is being called with swapped a and b values
    return(inner_function)

@smartFunc
def div(a,b):
    print(a/b)

div(2,4)        #This is equal to "smartFunc(div(2,4))"




