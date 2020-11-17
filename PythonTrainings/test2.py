def print_name(prefix):
    print("Searching prefix: {}".format(prefix))

    while True:
        name = (yield)
        if prefix in name:
            print(name)
            

corou =  print_name("Dear")
print("******After 1*******")

corou.__next__()
print("******2*******")
corou.send("Atul")
print("******3*******")
corou.send("Dear Atul")
print("******4*******")